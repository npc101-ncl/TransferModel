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
from transfer_model import WORKING_DIRECTORY, MODELS_DIRECTORY, SIMULATION_DIRECTORY, \
    EXPERIMENTAL_DATA_FILE, COPASI_FILE, DATA_DIRECTORY, OFFSET_PARAMETER, \
    COPASI_FORMATTED_DATA_DIRECTORY, PARAMETER_ESTIMATION_CONFIG_YAML

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
        kIRS1Act                =0.1;
        kIRS1Inact              =0.1;
        kIRS1Phos               =0.1;
        kIRS1Dephos             =0.1;
        kPI3KPhos               =0.1;
        kPI3KDephos             =0.1;
        kAktPhos                =0.1;
        kAktDephos              =0.1;
        kTSC2Phos               =0.1;
        kTSC2Dephos             =0.1;
        kmTORC1cytToLys         =0.1;
        kmTORC1LysToCyt         =0.1;
        kmTORC1Phos             =0.1;
        kmTORC1Dephos           =0.1;
        kPras40Phos             =0.1;
        kPras40Dephos           =0.1;
        kFourEBP1Phos           =0.1;
        kFourEBP1Dephos         =0.1;
        kS6KPhos                =0.1;
        kS6KDephos              =0.1;
        kmTORC1cytToLys         =0.1;
        kmTORC1LysToCyt         =0.1;
    
    
    
        // reactions // MMWithKcat(km, kcat, S, E)
        // function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
        // function MM(km, Vmax, S)
        // function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
        R1f     : IRS1 => IRS1a                         ; Cell * kIRS1Act*IRS1*Insulin;
        R2f     : IRS1a => IRS1pS636_639                ; Cell * kIRS1Phos*IRS1a*S6KpT389
        R2b     : IRS1pS636_639 => IRS1                 ; Cell * kIRS1Inact*IRS1pS636_639
        R3f     : PI3K => pPI3K                         ; Cell * kPI3KPhos*PI3K*IRS1a
        R3b     : pPI3K => PI3K                         ; Cell * kPI3KDephos*pPI3K
        R4f     : Akt => AktpT308                       ; Cell * kAktPhos*Akt*pPI3K
        R4b     : AktpT308 => Akt                       ; Cell * kAktDephos*pPI3K*AktpT308
        R5f     : TSC2 => TSC2pT1462                    ; Cell * kTSC2Phos*TSC2*AktpT308
        R5b     : TSC2pT1462 => TSC2                    ; Cell * kTSC2Dephos*TSC2pT1462
        R6f     : mTORC1cyt => mTORC1lys                ; Cell * kmTORC1cytToLys*mTORC1cyt*AA
        R6b     : mTORC1lys => mTORC1cyt                ; Cell * kmTORC1LysToCyt*mTORC1lys
        R7f     : mTORC1lys => pmTORC1                  ; Cell * kmTORC1Phos*mTORC1lys*TSC2
        R7b     : pmTORC1 => mTORC1lys                  ; Cell * kmTORC1Dephos*pmTORC1
        R8f     : PRAS40 => PRAS40pT246                 ; Cell * kPras40Phos*PRAS40*AktpT308
        R8b     : PRAS40pT246 => PRAS40                 ; Cell * kPras40Dephos*PRAS40pT246
        R9f     : FourEBP1 => FourEBP1pT37_46           ; Cell * kFourEBP1Phos*FourEBP1*pmTORC1
        R9b     : FourEBP1pT37_46 => FourEBP1           ; Cell * kFourEBP1Dephos*FourEBP1pT37_46
        R10f    : S6K => S6KpT389                       ; Cell * kS6KPhos*S6K*pmTORC1
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

        #     plot_data = data[selection]
        #     for specie in selection:
        #         plt.plot(plot_data.index, plot_data[specie], label=specie)
        #     seaborn.despine(ax=ax, top=True, right=True)
        #     plt.title(title)
        #     plt.legend(loc='best')
        # if filename is None:
        #     plt.show()
        # else:
        #     plt.savefig(filename, dpi=300, bbox_inches='tight')
        #


if __name__ == '__main__':

    OPEN_WITH_COPASI = False

    CONFIGURE_PARAMETER_ESTIMATION = False

    PLOT_SIMULATION = False

    PLOT_BEST_FIT = True

    # ========================================
    py_mod = model.loada(TheModel.model_string, copasi_file=COPASI_FILE)
    py_mod = tasks.TimeCourse(py_mod, start=0, end=150).model

    if OPEN_WITH_COPASI:
        py_mod.open()

    if CONFIGURE_PARAMETER_ESTIMATION:
        params = ['IRS1', 'Akt', 'PRAS40', 'TSC2', 'FourEBP1', 'S6K']
        exp_files = glob.glob(os.path.join(COPASI_FORMATTED_DATA_DIRECTORY, '*.csv'))
        with tasks.ParameterEstimation.Context(py_mod, exp_files, parameters='m', context='s') as context:
            context.set('run_mode', False)
            context.set('separator', ',')
            context.set('lower_bound', 0.1)
            context.set('upper_bound', 10)
            config = context.get_config()

        # print(config)
        config = tasks.ParameterEstimation.Config.from_yaml(yml=PARAMETER_ESTIMATION_CONFIG_YAML)
        pe = tasks.ParameterEstimation(config)
        py_mod = pe.models['simple_akt_model'].model
        # py_mod.open()

    if PLOT_SIMULATION:
        te_mod = TheModel()
        te_mod.plot()

    if PLOT_BEST_FIT:
        MCF7 = {}
        T47D = {}
        MCF7['Akt'] = 1.2818062896268356
        T47D['Akt'] = 1.7892466007955992
        MCF7['FourEBP1'] = 0.7126284151168799
        T47D['FourEBP1'] = 0.9270973665507092
        MCF7['IRS1'] = 3.0781723004869344
        T47D['IRS1'] = 1.7683077110052192
        MCF7['PRAS40'] = 1.798018487973172
        T47D['PRAS40'] = 1.0734662309797296
        MCF7['S6K'] = 1.9731430564400243
        T47D['S6K'] = 0.43090753855592484
        MCF7['TSC2'] = 1.34699754501788
        T47D['TSC2'] = 1.0281188142591413

        from transfer_model.data.data_analysis import GetData

        ics = GetData('T47D').get_initial_conc_params()
        ics['MCF7'].update(MCF7)
        ics['T47D'].update(T47D)

        te_mod_mcf7 = TheModel(ic_parameters=ics['MCF7'])
        te_mod_t47d = TheModel(ic_parameters=ics['T47D'])

        t47d_mcf7_fname = os.path.join(SIMULATION_DIRECTORY, 'MCF7_from_T47D_experiment.png')
        t47d_t47d_fname = os.path.join(SIMULATION_DIRECTORY, 'T47D_from_T47D_experiment.png')
        zr75_mcf7 = os.path.join(SIMULATION_DIRECTORY, 'MCF7_from_ZR75_experiment.png')
        zr75_zr75 = os.path.join(SIMULATION_DIRECTORY, 'ZR75_from_ZR75_experiment.png')
        te_mod_mcf7.plot_best_fit(which_data_file='T47D', which_cell_line='MCF7', filename=t47d_mcf7_fname)
        te_mod_t47d.plot_best_fit(which_data_file='T47D', which_cell_line='T47D', filename=t47d_t47d_fname)
        # te_mod.plot_best_fit(which_data_file='ZR75', which_cell_line='MCF7', filename=zr75_mcf7)
        # te_mod.plot_best_fit(which_data_file='ZR75', which_cell_line='ZR75', filename=zr75_zr75)
