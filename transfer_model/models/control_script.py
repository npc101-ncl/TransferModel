"""
This script defines a model of the PI3K/Akt system. Some flags that change the scripts behaviour
are at the bottom. 


"""
import numba
import os, glob, re
import pickle
from pathlib import Path
from scipy.spatial.distance import euclidean
import pandas as pd
import numpy as np
from collections import OrderedDict
import tellurium as te
import site
from sys import platform
import matplotlib.pyplot as plt
import seaborn
import matplotlib
from pyDOE import lhs
from scipy.stats.distributions import uniform
import fastdtw
import multiprocessing as mp

#site.addsitedir('/Users/peter/opt/anaconda3/envs/ver3p6/lib/python3.6/site-packages/pycotools3')
copasiBinPath = "/Applications/copasi"

if not re.search(copasiBinPath, os.environ["PATH"]):
    os.environ["PATH"] += os.pathsep + copasiBinPath

# from data.data_analysis import
wd = os.path.dirname(os.path.dirname(os.path.abspath('')))
site.addsitedir(wd)
from transfer_model import *
from transfer_model.data.data_analysis import GetData

import site

site.addsitedir('/home/ncw135/Documents/pycotools3')
from pycotools3 import tasks, viz, model

try:
    matplotlib.use('Qt5Agg')
except ImportError:
    matplotlib.use('TkAgg')
seaborn.set_context('talk')


class TheModel:
    from transfer_model.models.akt_model_with_mm_rate_laws import model_string
    model_string = model_string

    def __init__(self, ic_parameters=None):
        self.ic_parameters = ic_parameters
        self.rr = self._load_rr()
        self.rr = self._insert_parameters()

    def _load_rr(self):
        return te.loada(self.model_string)

    def _insert_parameters(self):
        if self.ic_parameters is None:
            return self.rr
        if not isinstance(self.ic_parameters, dict):
            raise ValueError

        for k, v in self.ic_parameters.items():
            if not hasattr(self.rr, k):
                print('Model does not have a initial conc. parameter called {}'.format(k))
                continue
            if not isinstance(v, (int, float)):
                raise ValueError('bad')
            print('inserting parameter "{}"={}'.format(k, v))
            setattr(self.rr, k, v)
        return self.rr

    def simulate(self, start, stop, num):
        data = self.rr.simulate(start, stop, num)
        data = pd.DataFrame(data, columns=data.colnames).set_index('time')
        data.columns = [i.replace('[', '').replace(']', '') for i in data.columns]
        return data

    def plot(self, ncols=3, plot_selection={}, filename=None):
        if plot_selection == {}:
            plot_selection = {
                'IRS1': ['IRS1', 'IRS1a', 'IRS1pS636_639']
            }
        data = self.simulate(0, 150, 151)

        # work out nrows and cols
        nplots = len(plot_selection)
        if nplots == 1:
            ncols = 1
        nrows = int(nplots / ncols)
        remainder = nplots % ncols
        if remainder > 0:
            nrows += 1
        seaborn.set_context(context='talk')
        fig = plt.figure()
        for i, (title, selection) in enumerate(plot_selection.items()):
            ax = plt.subplot(nrows, ncols, i + 1)
            plot_data = data[selection]
            for specie in selection:
                plt.plot(plot_data.index, plot_data[specie], label=specie)
            seaborn.despine(ax=ax, top=True, right=True)
            plt.title(title)
            plt.legend(loc='best')
        if filename is None:
            plt.show()
        else:
            plt.savefig(filename, dpi=300, bbox_inches='tight')

    def plot_best_fit(self, which_data_file='T47D', which_cell_line='MCF7',
                      ncols=3, plot_selection={}, filename=None,
                      hspace=0.25, wspace=0.25):
        if which_data_file not in ['T47D', 'ZR75']:
            raise ValueError
        if plot_selection == {}:
            plot_selection = {
                'IRS1pS636_639': ['IRS1pS636_639'],
                'AktpT308': ['AktpT308'],
                'TSC2pT1462': ['TSC2pT1462'],
                'FourEBP1pT37_46': ['FourEBP1pT37_46'],
                'PRAS40pT246': ['PRAS40pT246'],
                'S6KpT389': ['S6KpT389'],
            }
        data = self.simulate(0, 150, 151)
        from transfer_model.data.data_analysis import GetData
        exp_data = GetData(which_data_file).normalised_to_coomassie_blue()
        exp_data = exp_data.stack().groupby(['cell_line', 'time'])
        avg_data = exp_data.mean()
        sem_data = exp_data.sem()

        # work out nrows and cols
        nplots = len(plot_selection)
        if nplots == 1:
            ncols = 1
        nrows = int(nplots / ncols)
        remainder = nplots % ncols
        if remainder > 0:
            nrows += 1

        import matplotlib.lines as mlines
        seaborn.set_context(context='talk')
        fig = plt.figure(figsize=(15, 15))
        for i, (title, selection) in enumerate(plot_selection.items()):
            ax = plt.subplot(nrows, ncols, i + 1)
            sim_plot_data = data[selection]
            exp_plot_data = avg_data.loc[(which_cell_line), (selection)]
            exp_plot_data_err = sem_data.loc[(which_cell_line), (selection)]
            lines = []
            for species in selection:
                ax.errorbar(
                    exp_plot_data.index, exp_plot_data[species], yerr=exp_plot_data_err[species],
                    label=species, ls='--', marker='.', color='red'
                )
                ax.plot(sim_plot_data.index, sim_plot_data[species], label=species, ls='-', color='blue')
                # legend1 = plt.legend(loc='best', fontsize=10)
                # ax.add_artist(legend1)
            plt.title(title)
            seaborn.despine(ax=ax, top=True, right=True)
            plt.subplots_adjust(wspace=wspace, hspace=hspace)
            plt.suptitle(which_cell_line)
        fig.legend(
            handles=[
                mlines.Line2D([], [], color='red', label='Experimental data'),
                mlines.Line2D([], [], color='blue', label='Simulated data'),
            ],
            bbox_to_anchor=(0.05, -0.05, 0.7, 0.102),
            ncol=2, mode='expand',
            borderaxespad=0.0,
        )
        if filename is None:
            plt.show()
        else:
            plt.savefig(filename, dpi=300, bbox_inches='tight')

    def randomize_initial_conc_simulations(
            self, mod, n=10, lower_bound=0.1, upper_bound=10,
            plot=False, end_time=100, num_simulation_points=101,
            hspace=0.5, wspace=0.3, ncols=5, filename=None, **kwargs):
        """
        Randomize initial concentration parameters using latin hypercube sampling
        and run a time course
        Args:
            model: a roadrunner model

        Returns:
            pd.DataFrame

        """
        ics = [i.replace('[', '').replace(']', '') for i in mod.getFloatingSpeciesConcentrationIds()]

        original_ics = dict(zip(ics, mod.getFloatingSpeciesConcentrations()))
        sample = lhs(n=len(original_ics), samples=n, iterations=1, criterion=None)
        sample = uniform(lower_bound, upper_bound).ppf(sample)

        print('Simulating time series data')
        simulations = {}
        for i in range(sample.shape[0]):
            print('Percent Complete: {}%'.format(round(i / sample.shape[0] * 100, 2)))
            mod.reset()
            for j in range(sample.shape[1]):
                setattr(mod, ics[j], sample[i, j])
            data = mod.simulate(0, end_time, num_simulation_points)
            df = pd.DataFrame(data)
            df.columns = [i.replace('[', '').replace(']', '') for i in data.colnames]
            simulations[i] = df.set_index('time')

        df = pd.concat(simulations)
        dct = {}
        for label, df2 in df.groupby(level=0):
            dct[label] = df2.subtract(df2.iloc[0])

        df = pd.concat(dct)
        df.index = df.index.droplevel(0)

        if plot:
            print('plotting time series data')
            nplots = df.shape[1]
            if nplots == 1:
                ncols = 1
            nrows = int(nplots / ncols)
            remainder = nplots % ncols
            if remainder > 0:
                nrows += 1

            fig = plt.figure(figsize=(20, 10))
            for i, species in enumerate(df.columns):
                plot_data = df[[species]].reset_index()
                plot_data.columns = ['iterations', 'time', species]
                # print(plot_data)
                ax = plt.subplot(nrows, ncols, i + 1)
                seaborn.lineplot(
                    x='time', y=species, hue='iterations',
                    data=plot_data, ax=ax, **kwargs, legend=False,
                    palette='Blues'
                )

                seaborn.despine(ax=ax, top=True, right=True)
                plt.title(species)
                plt.xlabel('')
                plt.ylabel('')
            plt.subplots_adjust(hspace=hspace, wspace=wspace)

            if filename is None:
                plt.show()
            else:
                fig.savefig(filename, dpi=300, bbox_inches='tight')
        return df

    def calculate_dtw(self, simulations, which=['IRS1'],
                      plot=False, filename=None, from_pickle=False, pickle_file=RANDOM_ICS_DTW_PICKLE):
        if os.path.isfile(pickle_file) and from_pickle:
            distance = pd.read_pickle(pickle_file)
        else:
            simulations = simulations.unstack()
            if not isinstance(which, list):
                which = [which]
            simulation = simulations[which[0]]

            distance = np.zeros((simulation.shape[0], simulation.shape[0]))
            path = {}

            print('Running DTW comparisons')
            for i in range(simulation.shape[0]):
                print('Percent Complete: {}%'.format(round(i / simulation.shape[0] * 100, 2)))
                for j in range(simulation.shape[0]):
                    if i != j:
                        x = simulation.loc[i].values
                        y = simulation.loc[j].values
                        x = x - x[0]
                        y = y - y[0]
                        d, p = fastdtw.fastdtw(x, y, dist=euclidean)
                        distance[i, j] = d
                        path[(i, j)] = p
            pd.DataFrame(distance).to_pickle(pickle_file)

        if plot:
            fig = plt.figure()
            seaborn.clustermap(distance)

            if filename is not None:
                plt.savefig(filename, bbox_inches='tight', dpi=300)
            else:
                plt.show()

    def calculate_dtw_parallel(self, simulations, which=['IRS1'],
                               plot=False, filename=None, from_pickle=False, pickle_file=RANDOM_ICS_DTW_PICKLE):

        import ray
        import itertools
        ray.init(num_cpus=7, num_gpus=1)

        @ray.remote
        def inner_loop(x, y):
            d, p = fastdtw.fastdtw(x, y, dist=euclidean)
            return d, p

        if os.path.isfile(pickle_file) and from_pickle:
            distance = pd.read_pickle(pickle_file)
        else:
            simulations = simulations.unstack()
            if not isinstance(which, list):
                which = [which]
            simulation = simulations[which[0]]
            N = simulation.shape[0]

            distance = np.zeros((N, N))
            jobs = np.zeros((N, N), dtype=ray._raylet.ObjectID)

            count = 0
            size = len(list(itertools.combinations(range(N), 2)))
            print('Running DTW comparisons')
            for i, j in itertools.combinations(range(N), 2):
                count += 1
                print('Percent complete: {}%'.format(round(count / size * 100, 2)))
                x = simulation.loc[i].values
                y = simulation.loc[j].values
                x = x - x[0]
                y = y - y[0]
                jobs[i, j] = inner_loop.remote(x, y)

            for i, j in itertools.combinations(range(N), 2):

                d, p = ray.get(jobs[i, j])
                distance[i, j] = distance[j, i] = d
            df = pd.DataFrame(distance)
            df.to_pickle(pickle_file)

        if plot:
            fig = plt.figure()
            seaborn.clustermap(distance)

            if filename is not None:
                plt.savefig(filename, bbox_inches='tight', dpi=300)
            else:
                plt.show()

        return distance


    @staticmethod
    def time_series_kmeans(simulations, which=None, from_pickle=False,
                           pickle_file=TIMESERIES_KMEANS_DATA_PICKLE, **kwargs):

        from tslearn.utils import to_time_series, to_time_series_dataset
        from tslearn.clustering import TimeSeriesKMeans
        if os.path.isfile(pickle_file) and from_pickle:
            with open(pickle_file, 'rb') as f:
                return pickle.load(f)

        if which is None:
            which = list(simulations.columns)

        simulations = simulations[which]
        simulations = simulations.unstack(level=0)
        clusters = {}
        for i in which:
            simulation = simulations[i]
            print(simulation)
            ts_list = []
            for j in simulation:
                ts_list.append(to_time_series(simulation[j]))

            ts_dataset = to_time_series_dataset(ts_list)
            tskm = TimeSeriesKMeans(**kwargs)
            tskm.fit(ts_dataset)
            clusters[i] = {'labels': tskm.labels_,
                           'inertia': tskm.inertia_,
                           # 'cluster_centers': tskm.cluster_centers_,
                           }
        with open(pickle_file, 'wb') as f:
            pickle.dump(clusters, f)

        return clusters

    @staticmethod
    def features_extractions(data, from_pickle=False, pickle_file=EXTRACTED_FEATURES_PICKLE):
        from tsfresh import extract_features, select_features
        from tsfresh.utilities.dataframe_functions import impute
        # remember that data is already scaled by the - time point

        if from_pickle and os.path.isfile(pickle_file):
            features = pd.read_pickle(pickle_file)
        else:
            features = extract_features(data, column_id='level_0', column_sort='time')

        from sklearn.model_selection import train_test_split
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
        from scipy.stats import entropy
        features = impute(features)

        def calculate_entropy(data):
            e = {}
            for i in data.columns:
                e[i] = entropy(data[i])
            return pd.DataFrame(e, index=[0])

        # features = features.replace.dropna(how='any', axis=0)
        features = features.replace(0, np.nan).dropna(how='all', axis=1)



        fname = os.path.join(DATA_DIRECTORY, 'featuresdf.csv')
        print(fname)
        features.to_csv(fname)
        # total_entropy = calculate_entropy(features)
        # print(features)
        # print(total_entropy.sum(axis=1))

        features = features.loc[:, features.ne(1).all()]
        print(features)


        # sscore = {}
        # sh_score = {}
        # db_score = {}
        # for i in range(2, 20):
        #     print('i is: ', i)
        #     kmeans = KMeans(n_clusters=i, n_init=20)
        #     kmeans.fit_transform(features)
        #     labels = kmeans.labels_
        #     sscore[i] = silhouette_score(features, labels, metric='euclidean')
        #     sh_score[i] = calinski_harabasz_score(features, labels)
        #     db_score[i] = davies_bouldin_score(features, labels)
        #
        # plt.figure()
        # plt.plot(list(sscore.keys()), [i/max(list(sscore.values())) for i in  list(sscore.values())], marker='.')
        # plt.plot(list(sh_score.keys()),[i/max(list(sh_score.values())) for i in list(sh_score.values())], marker='.')
        # plt.plot(list(db_score.keys()), [i/max(list(db_score.values())) for i in list(db_score.values())], marker='.')
        # plt.show()



        # features.to_pickle(pickle_file)






if __name__ == '__main__':

    # these flags are set in the init file for transfer_model
    if CLUSTER:
        # on krutik's cluster
        WORKING_DIRECTORY = '/mnt/nfs/home/b7053098/ciaran/TransferModel'

        # on my new cluster
        WORKING_DIRECTORY = '/mnt/nfs/home/ncw135/TransferModel'

    py_mod = model.loada(TheModel.model_string, copasi_file=COPASI_FILE)
    py_mod = tasks.TimeCourse(py_mod, start=0, end=150).model

    if WRITE_COPASI_FORMATTED_DATA:
        from transfer_model.data.data_analysis import SteadyStateData

        gd_zr75 = GetData('ZR75', 'mean').to_copasi_format(prefix='interpolated', kind='cubic', num=12)
        gd_t47d = GetData('T47D', 'mean').to_copasi_format(prefix='interpolated', kind='cubic', num=12)
        # gd_ss = SteadyStateData().to_copasi_format()

    if OPEN_WITH_COPASI:
        py_mod.open()

    if CONFIGURE_PARAMETER_ESTIMATION:
        params = ['IRS1', 'Akt', 'PRAS40', 'TSC2', 'FourEBP1', 'S6K']

        if WHICH_CELL_LINE == 'ZR75':
            exp_files = glob.glob(os.path.join(ZR75_COPASI_FORMATED_DATA, '*.csv'))
        else:
            exp_files = glob.glob(os.path.join(T47D_COPASI_FORMATED_DATA, '*.csv'))

        # exp_files = exp_files + glob.glob(os.path.join(STEADTSTATE_COPASI_FORMATED_DATA, '*.csv'))

        # swap middle files so they are in the same order
        exp_files[1], exp_files[2] = exp_files[2], exp_files[1]

        with tasks.ParameterEstimation.Context(py_mod, exp_files, parameters='g', context='s') as context:
            context.set('run_mode', False)
            context.set('copy_number', 1)
            context.set('separator', ',')
            context.set('prefix', '_')
            context.set('lower_bound', 0.001)
            context.set('upper_bound', 10)
            context.set('randomize_start_values', True)
            # context.set('method', 'genetic_algorithm')
            context.set('method', 'particle_swarm')
            context.set('number_of_generations', 400)
            context.set('population_size', 80)
            context.set('swarm_size', 100)
            context.set('iteration_limit', 2000)
            context.set('problem', 'Problem4')
            context.set('fit', 1)
            config = context.get_config()

        # print(config)
        # config = tasks.ParameterEstimation.Config.from_yaml(yml=PARAMETER_ESTIMATION_CONFIG_YAML)
        pe = tasks.ParameterEstimation(config)
        py_mod = pe.models['simple_akt_model'].model
        # py_mod.open()

        PLOT_PE = False
        if PLOT_PE:
            # pl = viz.WaterfallPlot(pe, savefig=True)
            pl = viz.PlotParameterEstimation(pe, savefig=True)

    if CONFIGURE_PARAMETER_ESTIMATION_SS:
        params = ['IRS1', 'Akt', 'PRAS40', 'TSC2', 'FourEBP1', 'S6K']

        exp_files = glob.glob(os.path.join(STEADTSTATE_COPASI_FORMATED_DATA, '*.csv'))

        with tasks.ParameterEstimation.Context(py_mod, exp_files, parameters='g', context='s') as context:
            context.set('run_mode', 'slurm')
            context.set('separator', ',')
            context.set('lower_bound', 0.01)

            context.set('pe_number', 1)
            config = context.get_config()

        # print(config)
        # config = tasks.ParameterEstimation.Config.from_yaml(yml=PARAMETER_ESTIMATION_CONFIG_YAML)
        pe = tasks.ParameterEstimation(config)
        py_mod = pe.models['simple_akt_model'].model
        py_mod.open()

    if PLOT_SIMULATION:
        te_mod = TheModel()
        te_mod.plot()

    if PLOT_BEST_FIT_MCF7_AND_T47D:
        estimated_mcf7_ics = {}
        estimated_t47d_ics = {}
        estimated_mcf7_ics['Akt'] = 1.2818062896268356
        estimated_t47d_ics['Akt'] = 1.7892466007955992
        estimated_mcf7_ics['FourEBP1'] = 0.7126284151168799
        estimated_t47d_ics['FourEBP1'] = 0.9270973665507092
        estimated_mcf7_ics['IRS1'] = 3.0781723004869344
        estimated_t47d_ics['IRS1'] = 1.7683077110052192
        estimated_mcf7_ics['PRAS40'] = 1.798018487973172
        estimated_t47d_ics['PRAS40'] = 1.0734662309797296
        estimated_mcf7_ics['S6K'] = 1.9731430564400243
        estimated_t47d_ics['S6K'] = 0.43090753855592484
        estimated_mcf7_ics['TSC2'] = 1.34699754501788
        estimated_t47d_ics['TSC2'] = 1.0281188142591413

        ics = GetData('T47D').get_initial_conc_params()
        ics['MCF7'].update(estimated_mcf7_ics)
        ics['T47D'].update(estimated_t47d_ics)

        te_mod_mcf7 = TheModel(ic_parameters=ics['MCF7'])
        te_mod_t47d = TheModel(ic_parameters=ics['T47D'])
        mod = model.loada(TheModel('MCF7').model_string)

        t47d_mcf7_fname = os.path.join(SIMULATION_DIRECTORY, 'MCF7_from_T47D_experiment.png')
        t47d_t47d_fname = os.path.join(SIMULATION_DIRECTORY, 'T47D_from_T47D_experiment.png')
        # te_mod_mcf7.plot_best_fit(which_data_file='T47D', which_cell_line='MCF7', filename=t47d_mcf7_fname)
        # te_mod_t47d.plot_best_fit(which_data_file='T47D', which_cell_line='T47D', filename=t47d_t47d_fname)

        # produce a barplot comparing measured and simulated ics
        tots = ['Akt', 'FourEBP1', 'IRS1', 'PRAS40', 'S6K', 'TSC2']
        experimental_MCF7_ics = \
            GetData('T47D').normalised_to_coomassie_blue().stack().groupby(['cell_line', 'time']).mean()[tots].loc[
                'MCF7', 0].to_dict()
        experimental_T47D_ics = \
            GetData('T47D').normalised_to_coomassie_blue().stack().groupby(['cell_line', 'time']).mean()[tots].loc[
                'T47D', 0].to_dict()

        # collate into df
        df_mcf7 = pd.DataFrame([experimental_MCF7_ics, estimated_mcf7_ics],
                               index=['exp', 'sim'])
        df_mcf7 = pd.DataFrame(df_mcf7.stack()).reset_index()
        df_mcf7.columns = ['cell_line', 'parameter', 'value']

        # collate into df
        df_t47d = pd.DataFrame([experimental_T47D_ics, estimated_t47d_ics],
                               index=['exp', 'sim'])
        df_t47d = pd.DataFrame(df_t47d.stack()).reset_index()
        df_t47d.columns = ['cell_line', 'parameter', 'value']

        # print(df_mcf7)
        # and plot
        fig = plt.figure(figsize=(20, 10))
        ax = plt.subplot(121)
        seaborn.barplot(ax=ax, x='parameter', hue='cell_line', y='value', data=df_mcf7)
        plt.xlabel('')
        plt.legend()
        plt.title('MCF7')

        seaborn.despine(fig=fig, top=True, right=True)
        ax = plt.subplot(122)
        seaborn.barplot(ax=ax, x='parameter', hue='cell_line', y='value', data=df_t47d)
        plt.legend(loc=(0.1, 1))
        plt.title('T47D')
        seaborn.despine(fig=fig, top=True, right=True)

        fname = os.path.join(SIMULATION_DIRECTORY, 't47d_sheet_barplot_comparing_estimated_and_total_ics.png')
        plt.savefig(fname, dpi=300, bbox_inches='tight')

    if PLOT_BEST_FIT_MCF7_AND_ZR75:
        estimated_mcf7_ics = {}
        estimated_zr75_ics = {}
        # these were estimated.
        estimated_mcf7_ics['Akt'] = 1.766284542044498
        estimated_zr75_ics['Akt'] = 1.6169901853946649
        estimated_mcf7_ics['FourEBP1'] = 0.7528736731703629
        estimated_zr75_ics['FourEBP1'] = 1.5644306858467456
        estimated_mcf7_ics['IRS1'] = 3.4224381192249163
        estimated_zr75_ics['IRS1'] = 2.1371092389267043
        estimated_mcf7_ics['PRAS40'] = 1.7317272261472434
        estimated_zr75_ics['PRAS40'] = 1.968537005784804
        estimated_mcf7_ics['S6K'] = 1.6916492798629466
        estimated_zr75_ics['S6K'] = 0.7380178584075135
        estimated_mcf7_ics['TSC2'] = 1.909861364242059
        estimated_zr75_ics['TSC2'] = 1.1657935902247676

        ics = GetData('ZR75').get_initial_conc_params()

        ics['MCF7'].update(estimated_mcf7_ics)
        ics['ZR75'].update(estimated_zr75_ics)

        te_mod_mcf7 = TheModel(ic_parameters=ics['MCF7'])
        te_mod_zr75 = TheModel(ic_parameters=ics['ZR75'])

        zr75_mcf7_fname = os.path.join(SIMULATION_DIRECTORY, 'MCF7_from_ZR75_experiment.png')
        zr75_zr75_fname = os.path.join(SIMULATION_DIRECTORY, 'ZR75_from_ZR75_experiment.png')
        # te_mod_mcf7.plot_best_fit(which_data_file='ZR75', which_cell_line='MCF7', filename=zr75_mcf7_fname)
        # te_mod_zr75.plot_best_fit(which_data_file='ZR75', which_cell_line='ZR75', filename=zr75_zr75_fname)

        # produce a barplot comparing measured and simulated ics
        tots = ['Akt', 'FourEBP1', 'IRS1', 'PRAS40', 'S6K', 'TSC2']
        experimental_MCF7_ics = \
            GetData('ZR75').normalised_to_coomassie_blue().stack().groupby(['cell_line', 'time']).mean()[tots].loc[
                'MCF7', 0].to_dict()
        experimental_ZR75_ics = \
            GetData('ZR75').normalised_to_coomassie_blue().stack().groupby(['cell_line', 'time']).mean()[tots].loc[
                'ZR75', 0].to_dict()

        # collate into df
        df_mcf7 = pd.DataFrame([experimental_MCF7_ics, estimated_mcf7_ics],
                               index=['exp', 'sim'])
        df_mcf7 = pd.DataFrame(df_mcf7.stack()).reset_index()
        df_mcf7.columns = ['cell_line', 'parameter', 'value']

        # collate into df
        df_zr75 = pd.DataFrame([experimental_ZR75_ics, estimated_zr75_ics],
                               index=['exp', 'sim'])
        df_zr75 = pd.DataFrame(df_zr75.stack()).reset_index()
        df_zr75.columns = ['cell_line', 'parameter', 'value']

        # and plot
        fig = plt.figure(figsize=(20, 10))
        ax = plt.subplot(121)
        seaborn.barplot(ax=ax, x='parameter', hue='cell_line', y='value', data=df_mcf7)
        plt.xlabel('')
        plt.legend()
        plt.title('MCF7')

        seaborn.despine(fig=fig, top=True, right=True)
        ax = plt.subplot(122)
        seaborn.barplot(ax=ax, x='parameter', hue='cell_line', y='value', data=df_zr75)
        plt.title('ZR75')
        seaborn.despine(fig=fig, top=True, right=True)

        fname = os.path.join(SIMULATION_DIRECTORY, 'zr75_sheet_barplot_comparing_estimated_and_total_ics.png')
        plt.savefig(fname, dpi=300, bbox_inches='tight')

    if TRANSFER_BETWEEN_MCF7_FROM_ZR75_AND_T47D:
        # Calibrated with MCF7 and ZR75 (from same blot).
        # Transfer: T47D
        estimated_zr75_ics = {}
        estimated_zr75_ics['Akt'] = 1.6169901853946649
        estimated_zr75_ics['FourEBP1'] = 1.5644306858467456
        estimated_zr75_ics['IRS1'] = 2.1371092389267043
        estimated_zr75_ics['PRAS40'] = 1.968537005784804
        estimated_zr75_ics['S6K'] = 0.7380178584075135
        estimated_zr75_ics['TSC2'] = 1.1657935902247676

        estimated_mcf7_ics = {}
        estimated_mcf7_ics['Akt'] = 1.766284542044498
        estimated_mcf7_ics['FourEBP1'] = 0.7528736731703629
        estimated_mcf7_ics['IRS1'] = 3.4224381192249163
        estimated_mcf7_ics['PRAS40'] = 1.7317272261472434
        estimated_mcf7_ics['S6K'] = 1.6916492798629466
        estimated_mcf7_ics['TSC2'] = 1.909861364242059

        ics = GetData('T47D').get_initial_conc_params()
        print(ics['T47D'])
        # ics['MCF7'].update(MCF7)
        # ics['T47D'].update(estimated_zr75_ics)
        print(ics)
        te_mod_zr75 = TheModel(ic_parameters=ics['T47D'])
        mod = model.loada(te_mod_zr75.rr.getCurrentAntimony(), COPASI_FILE)
        mod.open()

        transfer_fname = os.path.join(SIMULATION_DIRECTORY, 'zr75_t47d_transfer.png')
        te_mod_zr75.plot_best_fit(which_data_file='T47D', which_cell_line='T47D', filename=transfer_fname)

    if RANDOM_ICS_SIMULATIONS:
        the_model = TheModel()
        mod = the_model.rr

        fname = os.path.join(RANDOM_ICS_DIR, 'random_initial_concentration_results.png')
        simulation = the_model.randomize_initial_conc_simulations(
            mod, plot=False, filename=fname, n=50, estimator=None,
        )


        simulation = simulation.reset_index()
        TheModel.features_extractions(
            simulation, from_pickle=True
        )
        # print(simulation)







# q learning for feature selection












