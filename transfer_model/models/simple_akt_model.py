"""
This script defines a model of the PI3K/Akt system. Some flags that change the scripts behaviour
are at the bottom. 


"""

from pathlib import Path
import os, glob
import pandas, numpy
from collections import OrderedDict
import tellurium as te
import site
from sys import platform
import matplotlib.pyplot as plt
import seaborn
import matplotlib

# from data.data_analysis import
from transfer_model import *
from transfer_model.data.data_analysis import GetData

import site

site.addsitedir('/home/ncw135/Documents/pycotools3')
from pycotools3 import tasks, viz, model

matplotlib.use('Qt5Agg')
seaborn.set_context('talk')


class TheModel:
    model_string = f"""
    function MM(km, Vmax, S)
        Vmax * S / (km + S)
    end
    
    function MMWithKcat(km, kcat, S, E)
        kcat * E * S / (km + S)
    end
    
    function NonCompetitiveInhibition(km, ki, Vmax, n, I, S)
        Vmax * S / ( (km + S) * (1 + (I / ki)^n ) )
    end
    
    function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
        kcat * E * S / ( (km + S) * (1 + (I / ki)^n ) )
    end
    
    function NonCompetitiveInhibitionWithKcatAndExtraActivator(km, ki, kcat, E1, E2, n, I, S)
        kcat * E1 * E2 * S / ( (km + S) * (1 + (I / ki)^n ) )
    end
    
    
    function MA1(k, S)
        k * S
    end
    
    function MA2(k, S1, S2)
        k * S1 * S2
    end
    
    function MA1Mod(k, S, M)
        k * S * M
    end
    
    function MA2Mod(k, S1, S2, M)
        k * S1 * S2 * M
    end
    
    function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
        kcat * E * S / (km + S + ((km * I )/ ki)  )
    end
    
    function CompetitiveInhibition(Vmax, km, ki, I, S)
        Vmax * S / (km + S + ((km * I )/ ki)  )
    end
    
    function Hill(km, kcat, L, S, h)
        kcat * L * (S / km)^h  /   1 + (S / km)^h
    end
    
    model SimpleAktModel()
        compartment             Cell = 1;
        var IRS1                in Cell;
        var IRS1a               in Cell;
        var IRS1pS636_639       in Cell;
        var Akt                 in Cell;
        var AktpT308            in Cell;
        var TSC2                in Cell;
        var TSC2pT1462          in Cell;
        var PRAS40              in Cell;
        var PRAS40pT246         in Cell;
        var S6K                 in Cell;
        var S6KpT389            in Cell;
        var FourEBP1            in Cell;
        var FourEBP1pT37_46     in Cell;
        var PI3K                in Cell;
        var pPI3K               in Cell;
        var pmTORC1            in Cell;
        var mTORC1cyt          in Cell;
        var mTORC1lys          in Cell;
        const Insulin          in Cell;
        const AA               in Cell;
    
        // global variables
        Insulin = 1;
        AA = 1
    
        IRS1            = 10;
        IRS1a           = 0;
        IRS1pS636_639   = 0;
        PI3K            = 10;
        pPI3K           = 0;
        AktpT308        = 0;
        Akt             = 10;
        TSC2pT1462      = 10;
        TSC2            = 0;
        pmTORC1         = 0;
        mTORC1cyt       = 10;
        mTORC1lys       = 0;
        PRAS40          = 10;
        PRAS40pT246     = 0;
        FourEBP1pT37_46 = 0;
        FourEBP1        = 10;
        S6KpT389        = 0;
        S6K             = 10;
    
    
        // kinetic parameters
        _kIRS1Act                = 0.1;
        _kIRS1Inact              = 0.1;
        kIRS1Phos               = 0.1;
        _kPI3KPhos               = 0.1;
        kPI3KDephos             = 0.1;
        _kAktPhos                = 0.1;
        kAktDephos              = 0.1;
        kTSC2Phos               = 0.1;
        _kTSC2Dephos             = 0.1;
        _kmTORC1cytToLys         = 0.1;
        _kmTORC1LysToCyt         = 0.1;
        _kmTORC1Phos             = 0.1;
        kmTORC1Dephos           = 0.1;
        _kPras40Phos             = 0.1;
        kPras40Dephos           = 0.1;
        _kFourEBP1Phos           = 0.1;
        kFourEBP1Dephos         = 0.1;
        _kS6KPhos                = 0.1;
        kS6KDephos              = 0.1;
    
    
    
        // reactions // MMWithKcat(km, kcat, S, E)
        // function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
        // function MM(km, Vmax, S)
        // function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
        R1f     : IRS1 => IRS1a                         ; Cell * _kIRS1Act*IRS1*Insulin;
        R2f     : IRS1a => IRS1pS636_639                ; Cell * kIRS1Phos*IRS1a*S6KpT389
        R2b     : IRS1pS636_639 => IRS1                 ; Cell * _kIRS1Inact*IRS1pS636_639
        R3f     : PI3K => pPI3K                         ; Cell * _kPI3KPhos*PI3K*IRS1a
        R3b     : pPI3K => PI3K                         ; Cell * kPI3KDephos*pPI3K
        R4f     : Akt => AktpT308                       ; Cell * _kAktPhos*Akt*pPI3K
        R4b     : AktpT308 => Akt                       ; Cell * kAktDephos*pPI3K*AktpT308
        R5f     : TSC2 => TSC2pT1462                    ; Cell * kTSC2Phos*TSC2*AktpT308
        R5b     : TSC2pT1462 => TSC2                    ; Cell * _kTSC2Dephos*TSC2pT1462
        R6f     : mTORC1cyt => mTORC1lys                ; Cell * _kmTORC1cytToLys*mTORC1cyt*AA
        R6b     : mTORC1lys => mTORC1cyt                ; Cell * _kmTORC1LysToCyt*mTORC1lys
        R7f     : mTORC1lys => pmTORC1                  ; Cell * _kmTORC1Phos*mTORC1lys*TSC2
        R7b     : pmTORC1 => mTORC1lys                  ; Cell * kmTORC1Dephos*pmTORC1
        R8f     : PRAS40 => PRAS40pT246                 ; Cell * _kPras40Phos*PRAS40*AktpT308
        R8b     : PRAS40pT246 => PRAS40                 ; Cell * kPras40Dephos*PRAS40pT246
        R9f     : FourEBP1 => FourEBP1pT37_46           ; Cell * _kFourEBP1Phos*FourEBP1*pmTORC1
        R9b     : FourEBP1pT37_46 => FourEBP1           ; Cell * kFourEBP1Dephos*FourEBP1pT37_46
        R10f    : S6K => S6KpT389                       ; Cell * _kS6KPhos*S6K*pmTORC1
        R10b    : S6KpT389 => S6K                       ; Cell * kS6KDephos*S6KpT389
    
    end
    
    """

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
            setattr(self.rr, k, v)
        return self.rr

    def simulate(self, start, stop, num):
        data = self.rr.simulate(start, stop, num)
        data = pandas.DataFrame(data, columns=data.colnames).set_index('time')
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


if __name__ == '__main__':

    CLUSTER = True

    WRITE_COPASI_FORMATTED_DATA = False

    OPEN_WITH_COPASI = False

    CONFIGURE_PARAMETER_ESTIMATION = True
    if CONFIGURE_PARAMETER_ESTIMATION:
        WHICH_CELL_LINE = 'T47D'
        assert WHICH_CELL_LINE in ['T47D', 'ZR75']

    # configure the steady state data only
    CONFIGURE_PARAMETER_ESTIMATION_SS = False

    PLOT_SIMULATION = False

    PLOT_BEST_FIT_MCF7_AND_T47D = False

    PLOT_BEST_FIT_MCF7_AND_ZR75 = False

    TRANSFER_BETWEEN_MCF7_FROM_ZR75_AND_T47D = False

    # ========================================

    if CLUSTER:
        WORKING_DIRECTORY = ''

    py_mod = model.loada(TheModel.model_string, copasi_file=COPASI_FILE)
    py_mod = tasks.TimeCourse(py_mod, start=0, end=150).model

    if WRITE_COPASI_FORMATTED_DATA:
        gd_zr75 = GetData('ZR75', 'mean').to_copasi_format()
        gd_t47d = GetData('T47D', 'mean').to_copasi_format()

    if OPEN_WITH_COPASI:
        py_mod.open()

    if CONFIGURE_PARAMETER_ESTIMATION:
        params = ['IRS1', 'Akt', 'PRAS40', 'TSC2', 'FourEBP1', 'S6K']


        if WHICH_CELL_LINE == 'ZR75':
            exp_files = glob.glob(os.path.join(ZR75_COPASI_FORMATED_DATA, '*.csv'))
        else:
            exp_files = glob.glob(os.path.join(T47D_COPASI_FORMATED_DATA, '*.csv'))

        exp_files = exp_files + glob.glob(os.path.join(STEADTSTATE_COPASI_FORMATED_DATA, '*.csv'))


        with tasks.ParameterEstimation.Context(py_mod, exp_files, parameters='g', context='s') as context:
            context.set('run_mode', False)
            context.set('separator', ',')
            context.set('prefix', '_')
            context.set('lower_bound', 0.1)
            context.set('upper_bound', 10)
            config = context.get_config()

        # print(config)
        # config = tasks.ParameterEstimation.Config.from_yaml(yml=PARAMETER_ESTIMATION_CONFIG_YAML)
        pe = tasks.ParameterEstimation(config)
        py_mod = pe.models['simple_akt_model'].model
        py_mod.open()

    if CONFIGURE_PARAMETER_ESTIMATION_SS:
        params = ['IRS1', 'Akt', 'PRAS40', 'TSC2', 'FourEBP1', 'S6K']

        exp_files = glob.glob(os.path.join(STEADTSTATE_COPASI_FORMATED_DATA, '*.csv'))

        with tasks.ParameterEstimation.Context(py_mod, exp_files, parameters='m', context='s') as context:
            context.set('run_mode', False)
            context.set('separator', ',')
            context.set('lower_bound', 0.1)
            context.set('upper_bound', 10)
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
        df_mcf7 = pandas.DataFrame([experimental_MCF7_ics, estimated_mcf7_ics],
                                   index=['exp', 'sim'])
        df_mcf7 = pandas.DataFrame(df_mcf7.stack()).reset_index()
        df_mcf7.columns = ['cell_line', 'parameter', 'value']

        # collate into df
        df_t47d = pandas.DataFrame([experimental_T47D_ics, estimated_t47d_ics],
                                   index=['exp', 'sim'])
        df_t47d = pandas.DataFrame(df_t47d.stack()).reset_index()
        df_t47d.columns = ['cell_line', 'parameter', 'value']

        print(df_mcf7)
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
        df_mcf7 = pandas.DataFrame([experimental_MCF7_ics, estimated_mcf7_ics],
                                   index=['exp', 'sim'])
        df_mcf7 = pandas.DataFrame(df_mcf7.stack()).reset_index()
        df_mcf7.columns = ['cell_line', 'parameter', 'value']

        # collate into df
        df_zr75 = pandas.DataFrame([experimental_ZR75_ics, estimated_zr75_ics],
                                   index=['exp', 'sim'])
        df_zr75 = pandas.DataFrame(df_zr75.stack()).reset_index()
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
        estimated_mcf7_ics = {}
        estimated_zr75_ics = {}
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

        ics = GetData('T47D').get_initial_conc_params()
        print(ics['T47D'])
        # ics['MCF7'].update(MCF7)
        ics['T47D'].update(estimated_zr75_ics)

        te_mod_zr75 = TheModel(ic_parameters=ics['T47D'])

        transfer_fname = os.path.join(SIMULATION_DIRECTORY, 'zr75_t47d_transfer.png')
        te_mod_zr75.plot_best_fit(which_data_file='T47D', which_cell_line='T47D', filename=transfer_fname)
