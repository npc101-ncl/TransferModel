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
from transfer_model import WORKING_DIRECTORY, MODELS_DIRECTORY, SIMULATION_DIRECTORY, EXPERIMENTAL_DATA_FILE, COPASI_FILE, DATA_DIRECTORY

matplotlib.use('Qt5Agg')
seaborn.set_context('talk')

# model_string = f"""
#
# function MM(km, Vmax, S)
#     Vmax * S / (km + S)
# end
#
# function MMWithKcat(km, kcat, S, E)
#     kcat * E * S / (km + S)
# end
#
# function NonCompetitiveInhibition(km, ki, Vmax, n, I, S)
#     Vmax * S / ( (km + S) * (1 + (I / ki)^n ) )
# end
#
# function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
#     kcat * E * S / ( (km + S) * (1 + (I / ki)^n ) )
# end
#
# function NonCompetitiveInhibitionWithKcatAndExtraActivator(km, ki, kcat, E1, E2, n, I, S)
#     kcat * E1 * E2 * S / ( (km + S) * (1 + (I / ki)^n ) )
# end
#
#
# function MA1(k, S)
#     k * S
# end
#
# function MA2(k, S1, S2)
#     k * S1 * S2
# end
#
# function MA1Mod(k, S, M)
#     k * S * M
# end
#
# function MA2Mod(k, S1, S2, M)
#     k * S1 * S2 * M
# end
#
# function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
#     kcat * E * S / (km + S + ((km * I )/ ki)  )
# end
#
# function CompetitiveInhibition(Vmax, km, ki, I, S)
#     Vmax * S / (km + S + ((km * I )/ ki)  )
# end
#
# function Hill(km, kcat, L, S, h)
#     kcat * L * (S / km)^h  /   1 + (S / km)^h
# end
#
# model SimpleAktModel()
#     compartment             Cell = 1;
#     var IRS1                in Cell;
#     var IRS1a               in Cell;
#     var IRS1pS636_639       in Cell;
#     var Akt                 in Cell;
#     var AktpT308            in Cell;
#     var TSC2                in Cell;
#     var TSC2pT1462          in Cell;
#     var PRAS40              in Cell;
#     var PRAS40pT246         in Cell;
#     var S6K                 in Cell;
#     var S6KpT389            in Cell;
#     var S6KpT229            in Cell;
#     var FourEBP1            in Cell;
#     var FourEBP1pT37_46     in Cell;
#     var PI3K                in Cell;
#     var pPI3K               in Cell;
#     var mTORC1              in Cell;
#     var pmTORC1             in Cell;
#     var mTORC1i             in Cell;
#     const Insulin           in Cell;
#     const AA               in Cell;
#
#     // global variables
#     Insulin = 1;
#
#     // Offset is added onto total proteins in order to prevent phospho being present in
#     //  greater quantity than total
#     // offset_amount                  = {OFFSET_PARAMETER}
#
#     // FourEBP1_tot                  := 1.593687 + offset_amount;
#     // Akt_tot                       := 0.736138 + offset_amount;
#     // IRS1_tot                      := 0.458843 + offset_amount;
#     // TSC2_tot                      := 0.816176 + offset_amount;
#     // PRAS40_tot                    := 0.954775 + offset_amount;
#     // S6K_tot                       := 0.487419 + offset_amount;
#     // PI3K_tot                      := 1          + offset_amount;
#
#     // we do not need to fit total proteins
#     // IRS1_obs                   := IRS1_tot;
#     // Akt_obs                    := Akt_tot;
#     // TSC2_obs                   := TSC2_tot;
#     // PRAS40_obs                 := PRAS40_tot;
#     // S6K_obs                    := S6K_tot ;
#
#     // IRS1pS636_639_obs             := IRS1pS636_639;
#     // AktpT308_obs                  := AktpT308;
#     // TSC2pT1462_obs                := TSC2pT1462;
#     // PRAS40pT246_obs               := PRAS40pT246;
#     // S6KpT389_obs                  := S6KpT389;
#     // S6KpT229_obs                  := S6KpT229;
#     // FourEBP1pT37_46_obs           := FourEBP1pT37_46;
#
#     //initial conditions
#     // FourEBP1pT37_46    = 0.644677;
#     // AktpT308           = 0.585251;
#     // IRS1pS636_639      = 0.458843;
#     // PRAS40pT246        = 0.537742;
#     // S6KpT229           = 0.241475;
#     // S6KpT389           = 0.177316;
#     // TSC2pT1462         = 0.654499;
#     // pPI3K              = 0.1;
#
#     IRS1            = 10;
#     IRS1a           = 0;
#     IRS1pS636_639   = 0;
#     PI3K            = 10;
#     pPI3K           = 0;
#     AktpT308        = 0;
#     Akt             = 10;
#     TSC2pT1462      = 10;
#     TSC2            = 0;
#     pmTORC1         = 0;
#     mTORC1cyt       = 10;
#     mTORC1lys       = 0;
#     PRAS40          = 0;
#     PRAS40pT246     = 0;
#     FourEBP1pT37_46 = 0;
#     FourEBP1        = 10;
#     S6KpT389        = 0;
#     S6K             = 10;
#
#
#     // IRS1               := IRS1_tot       -     IRS1pS636_639             ;
#     // Akt                := Akt_tot        -     AktpT308                  ;
#     // TSC2               := TSC2_tot       -     TSC2pT1462                ;
#     // PRAS40             := PRAS40_tot     -     PRAS40pT246               ;
#     // FourEBP1           := FourEBP1_tot   -     FourEBP1pT37_46           ;
#     // S6K                := S6K_tot        -     S6KpT389   - S6KpT229     ;
#     // PI3K               := PI3K_tot       -     pPI3K                    ;
#
#     // kinetic parameters
#     kIRS1Act                =0.1;
#     kIRS1Inact              =0.1;
#     kIRS1Phos               =0.1;
#     kIRS1Dephos             =0.1;
#     kPI3KPhos               =0.1;
#     kPI3KDephos             =0.1;
#     kAktPhos                =0.1;
#     kAktDephos              =0.1;
#     kTSC2Phos               =0.1;
#     kTSC2Dephos             =0.1;
#     kmTORC1cytToLys         =0.1;
#     kmTORC1LysToCyt         =0.1;
#     kmTORC1Phos             =0.1;
#     kmTORC1Dephos           =0.1;
#     kPras40Phos             =0.1;
#     kPras40Dephos           =0.1;
#     kFourEBP1Phos           =0.1;
#     kFourEBP1Dephos         =0.1;
#     kS6KPhos                =0.1;
#     kS6KDephos              =0.1;
#     kmTORC1cytToLys         =0.1;
#     kmTORC1LysToCyt         =0.1;
#
#
#
#     // reactions // MMWithKcat(km, kcat, S, E)
#     // function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
#     // function MM(km, Vmax, S)
#     // function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
#     R1f     : IRS1 => IRS1a                         ; Cell * kIRS1Act*IRS1*Insulin;
#     R1b     : IRS1a => IRS1                         ; Cell * kIRS1Inact*IRS1a;
#     R2f     : IRS1a => IRS1pS636_639                ; Cell * kIRS1Phos*IRS1a*S6KpT389
#     R2b     : IRS1pS636_639 => IRS1                 ; Cell * kIRS1Dephos*IRS1pS636_639
#     R3f     : PI3K => pPI3K                         ; Cell * kPI3KPhos*PI3K*IRS1a
#     R3b     : pPI3K => PI3K                         ; Cell * kPI3KDephos*pPI3K
#     R4f     : Akt => AktpT308                       ; Cell * kAktPhos*Akt*pPI3K
#     R4b     : AktpT308 => Akt                       ; Cell * kAktDephos*pPI3K
#     R5f     : TSC2 => TSC2pT1462                    ; Cell * kTSC2Phos*TSC2*AktpT308
#     R5b     : TSC2pT1462 => TSC2                    ; Cell * kTSC2Dephos*TSC2pT1462
#     R6f     : mTORC1cyt => mTORC1lys                ; Cell * kmTORC1cytToLys*mTORC1cyt*AA
#     R6b     : mTORC1lys => mTORC1cyt                ; Cell * kmTORC1LysToCyt*mTORC1lys
#     R7f     : mTORC1lys => pmTORC1                  ; Cell * kmTORC1Phos*mTORC1lys*TSC2
#     R7b     : pmTORC1 => mTORC1lys                  ; Cell * kmTORC1Dephos*pmTORC1
#     R8f     : PRAS40 => PRAS40pT246                 ; Cell * kPras40Phos*PRAS40*AktpT308
#     R8b     : PRAS40pT246 => PRAS40                 ; Cell * kPras40Dephos*PRAS40pT246
#     R9f     : FourEBP1 => FourEBP1pT37_46           ; Cell * kFourEBP1Phos*FourEBP1*pmTORC1
#     R9b     : FourEBP1pT37_46 => FourEBP1           ; Cell * kFourEBP1Dephos*FourEBP1pT37_46
#     R10f    : S6K => S6KpT389                       ; Cell * kS6KPhos*S6K*pmTORC1
#     R10b    : S6KpT389 => S6K                       ; Cell * kS6KDephos*S6KpT389
#
#     //R1f : IRS1 => IRS1pS636_639           ; Cell*   MMWithKcat(_kIRS1Phos_km, _kIRS1Phos_kcat, IRS1, S6KpT389);
#     //R1b : IRS1pS636_639 => IRS1           ; Cell*   MMWithKcat(_kIRS1Dephos_km, _kIRS1Dephos_kcat, IRS1pS636_639, Insulin );
#     //R2f : PI3K => pPI3K                   ; Cell*   MMWithKcat(_kPI3KPhos_km, _kPI3KPhos_kcat, PI3K, IRS1);
#     //R2b : pPI3K => PI3K                   ; Cell*   _kPI3KDephos*pPI3K;
#     //R3f : S6K => S6KpT229                 ; Cell*   MMWithKcat(_kS6KPhosS229_km, _kS6KPhosS229_kcat, S6K, pPI3K);
#     //R3b : S6KpT229 => S6K                 ; Cell*   kS6KDephosS229*S6KpT229;
#     //R4f : Akt => AktpT308                 ; Cell*   MMWithKcat(_kAktPhos_km, _kAktPhos_kcat, Akt, pPI3K);
#     //R4b : AktpT308 => Akt                 ; Cell*   _kAktDephos*AktpT308;
#     //R5f : TSC2 => TSC2pT1462              ; Cell*   MMWithKcat(_kTSC2Phos_km, _kTSC2Phos_kcat, TSC2, AktpT308);
#     //R5b : TSC2pT1462 => TSC2              ; Cell*   _kTSC2Dephos*TSC2pT1462;
#     //R6f : PRAS40 => PRAS40pT246           ; Cell*   MMWithKcat(_kPras40PhosByAkt_km, _kPras40PhosByAkt_kcat, PRAS40, AktpT308);
#     //R6b : PRAS40pT246 => PRAS40           ; Cell*   kPras40Dephos*PRAS40pT246;
#     //R7f : FourEBP1 => FourEBP1pT37_46     ; Cell*   MMWithKcat(_kFourEBP1Phos_km, _kFourEBP1Phos_kcat, FourEBP1, TSC2pT1462);
#     //R7b : FourEBP1pT37_46 => FourEBP1     ; Cell*   kFourEBP1Dephos*FourEBP1pT37_46;
#     //R8f : S6K => S6KpT389                 ; Cell*   MMWithKcat(_kS6KT389Phos_km, _kS6KT389Phos_kcat, S6K, TSC2pT1462);
#     //R8b : S6KpT389 => S6K                 ; Cell*   _kS6KT389Dephos*S6KpT389;
# end
#
# """
#
#
# def plot_best_fit(problem):
#     """
#
#     :param problem: string. Used for filename only
#     :return:
#     """
#     data = viz.Parse(pe).data
#     data['simple_akt_model'].to_csv(os.path.join(DATA_DIRECTORY, 'parameter_estimation_data.csv'))
#     print(data['simple_akt_model'].iloc[0])
#     mod.insert_parameters(df=data['simple_akt_model'], index=0, inplace=True)
#     # simulate steady state condition
#     mod.set('global_quantity', 'Insulin', 0.05, match_field='name', change_field='initial_value')
#     ss_data = mod.simulate(0, 120, 1, variables='gm')
#     # simulate insulin stimulated condition
#     mod.set('global_quantity', 'Insulin', 1, match_field='name', change_field='initial_value')
#     data = mod.simulate(0, 120, 1, variables='gm')
#     exp = GetDataFromOldDataFile(EXPERIMENTAL_DATA_FILE).get_data_normalised_to_coomassie_blue(
#         offset_for_total_proetins=1)
#     # exp = GetDataNormedToMax()
#     exp = exp.stack()
#     exp = exp.loc['MCF7']
#     exp = exp.rename(columns={'4E_BP1': 'FourE_BP1',
#                               '4E_BP1pT37_46': 'FourEBP1pT37_46',
#                               'ERK': 'Erk',
#                               'ERK_pT202_Y204': 'Erk_pT202_Y204',
#                               })
#
#     phospho_species_that_were_fitted = ['AktpT308_obs', 'FourEBP1pT37_46_obs',
#                                         'IRS1pS636_639_obs', 'PRAS40pT246_obs',
#                                         'S6KpT389_obs', 'TSC2pT1462_obs',
#                                         'Erk_pT202_Y204']
#
#     ss_sim = ss_data[sorted(['IRS1_tot', 'Akt_tot', 'TSC2_tot',
#                              'PRAS40_tot', 'FourEBP1_tot', 'S6K_tot',
#                              'Erk_tot'])]
#
#     print(exp.columns)
#     ss_exp = exp[sorted(['FourE_BP1', 'Akt', 'IRS1',
#                          'PRAS40', 'S6K', 'TSC2', 'Erk'])]
#
#     # print(ss_sim.columns)
#     # print(ss_exp.columns)
#
#     ts_sim = data[sorted(phospho_species_that_were_fitted)]
#
#     ts_exp = exp[sorted([i.replace('_obs', '') for i in phospho_species_that_were_fitted])]
#
#     assert ss_sim.shape[1] == 7, ss_sim.shape[1]
#     assert ss_exp.shape[1] == 7, ss_exp.shape[1]
#     assert ts_sim.shape[1] == 7, ts_sim.shape[1]
#     assert ts_exp.shape[1] == 7, ts_exp.shape[1]
#
#     fig = plt.figure(figsize=(20, 10))
#     for i in range(ss_sim.shape[1]):
#         ax = plt.subplot(3, 3, i + 1)
#         ss_sim_var = ss_sim.columns[i]
#         ss_exp_var = ss_exp.columns[i]
#         ts_sim_var = ts_sim.columns[i]
#         ts_exp_var = ts_exp.columns[i]
#
#         ss_sim_plt = ss_sim[ss_sim.columns[i]]
#         # ss_exp_plt = ss_exp[ss_exp.columns[i]]
#         ts_sim_plt = ts_sim[ts_sim.columns[i]]
#         # ts_exp_plt = ts_exp[ts_exp.columns[i]]
#
#         # steady state stuff
#         total_color = 'green'
#         phos_color = 'blue'
#         seaborn.lineplot(x='time', y=ss_exp_var,
#                          data=ss_exp.reset_index(), label='Total protein, experimental',
#                          ax=ax, legend=False, color=total_color,
#                          markers=True)
#         ax.lines[0].set_linestyle("--")
#         ax.plot(ss_sim_plt.index, ss_sim_plt.values, label='Total protein, simulated',
#                 linestyle='-', color=total_color,
#                 )
#
#         # time series stuff
#         seaborn.lineplot(x='time', y=ts_exp_var, data=ts_exp.reset_index(),
#                          label='pProtein, experimental', ax=ax, legend=False, color=phos_color,
#                          markers=True
#                          )
#         ax.lines[2].set_linestyle("--")
#
#         ax.plot(ts_sim_plt.index, ts_sim_plt.values, label='pProtein, simulated',
#                 linestyle='-', color=phos_color)
#
#         plt.title(ss_exp_var)
#         seaborn.despine(fig=fig, top=True, right=True)
#         plt.xlabel('')
#         plt.ylabel('')
#     # plt.subplots_adjust(left=0.25, right=0.25, top=0.25, bottom=0.25)
#     plt.subplots_adjust(wspace=0.1, hspace=0.4)
#     plt.legend(loc=(1.35, 0.1))
#     # plt.show()
#     fname = os.path.join(SIMULATION_GRAPHS_DIR, '{}_simulations.png'.format(problem))
#     fig.savefig(fname, dpi=300, bbox_inches='tight')
#     print('figure saved to "{}"'.format(fname))
#
# def plot_best_fit2(mod, problem, features=None, cell_line='MCF7', savefig=False):
#     """
#
#     :param problem: string. Used for filename only
#     :return:
#     """
#     # Each of the three cell lines has different starting condition. You need to take averages
#     #  of the repeats and insert the ics before simulating each cell lines
#     variables_for_ic_change = {
#     'FourEBP1': 'FourEBP1_tot',
#     'FourEBP1pT37_46': 'FourEBP1pT37_46',
#     'Akt': 'Akt_tot',
#     'AktpT308': 'AktpT308',
#     'IRS1': 'IRS1_tot',
#     'IRS1pS636_639': 'IRS1pS636_639',
#     'PRAS40': 'PRAS40_tot',
#     'PRAS40pT246': 'PRAS40pT246',
#     'S6K': 'S6K_tot',
#     'S6KpT229': 'S6KpT229',
#     'S6KpT389': 'S6KpT389',
#     'TSC2': 'TSC2_tot',
#     'TSC2pT1462': 'TSC2pT1462',
#     }
#     data = viz.Parse(pe).data
#     data['simple_akt_model'].to_csv(os.path.join(DATA_DIRECTORY, 'parameter_estimation_data.csv'))
#     # print(data['simple_akt_model'].iloc[0])
#     mod.insert_parameters(df=data['simple_akt_model'], index=0, inplace=True)
#     # simulate steady state condition
#     # mod.set('global_quantity', 'Insulin', 0.05, match_field='name', change_field='initial_value')
#     # ss_data = mod.simulate(0, 120, 1, variables='gm')
#     # simulate insulin stimulated condition
#     gd = GetDataNormedToMax(DATA_FILE_NORMED_TO_MAX)
#     ics = gd.get_average_of_0_time_points(offset_for_inactive_species=OFFSET_PARAMETER)
#     ics = ics[list(variables_for_ic_change.keys())]
#     ics = ics.rename(columns=variables_for_ic_change)
#     ics = ics.loc[cell_line].to_dict()
#     # print(ics)
#     mod.insert_parameters(parameter_dict=ics)
#     mod = mod.set('global_quantity', 'Insulin', 1, match_field='name', change_field='initial_value')
#     data = mod.simulate(0, 120, 1, variables='gm')
#     # exp = GetDataFromOldDataFile(EXPERIMENTAL_DATA_FILE).get_data_normalised_to_coomassie_blue(
#     #     offset_for_total_proetins=1)
#     exp = gd.read_data(offset_for_inactive_species=OFFSET_PARAMETER)
#     exp = exp.stack()
#     exp = exp.loc[cell_line]
#     exp = pandas.DataFrame(exp)
#     exp.index.names = ['time', 'repeat', 'antibody']
#     exp.columns = ['signal']
#
#     if features is None:
#         features = [i for i in data.columns if '_obs' in i]
#
#     data = data[features]
#     data.columns = [i.replace('_obs', '') for i in data.columns]
#     data = data.stack()
#     data = pandas.DataFrame(data)
#     data.index.names = ['time', 'antibody']
#     data.columns = ['signal']
#
#     for i in sorted(list(set(data.index.get_level_values('antibody')))):
#         df = data.xs(level='antibody', key=i)
#         exp_df = exp.xs(level='antibody', key=i)
#         fig = plt.figure()
#         seaborn.lineplot(x='time', y='signal', data=df.reset_index(), label='simulation')
#         seaborn.lineplot(x='time', y='signal', data=exp_df.reset_index(), label='experiment', markers='.')
#         seaborn.despine(fig=fig, top=True, right=True)
#         plt.title(f'{cell_line}, {i}')
#         plt.legend(loc='best')
#         if savefig:
#             problem_dir = os.path.join(SIMULATION_GRAPHS_DIR, problem)
#             os.makedirs(problem_dir) if not os.path.isdir(problem_dir) else None
#             fname = os.path.join(problem_dir, f'{cell_line}_{i}.png')
#             plt.savefig(fname, dpi=300, bbox_inches='tight')
#             print(f'saved to {fname}')
#     if not savefig:
#         plt.show()
#
#
# def plotpl():
#     '/home/ncw135/Documents/MesiSTRAT2/BreastCancerModel/models/ProfileLikelihoods/Fit1/_kAktPhos_kcat/ParameterEstimationData'
#     print(WORKING_DIRECTORY)
#     pl_dir = os.path.join(MODELS_DIRECTORY, 'ProfileLikelihoods')
#     assert os.path.isdir(pl_dir)
#     files = glob.glob(os.path.join(pl_dir, '*/*/*/*.txt'))
#     names = [os.path.split(os.path.dirname(os.path.dirname(i)))[1] for i in files]
#     data_files = dict(zip(names, files))
#
#     def read1(f):
#         with open(f) as fle:
#             data = fle.read()
#         data = data.replace('(', '').replace(')', '')
#         data = data.split('\n')[1:]
#         from functools import reduce
#         data = '\n'.join(data)
#         from io import StringIO
#         df = pandas.read_csv(StringIO(data), sep='\t', header=None)
#         rss = df.iloc[:, -1]
#         return rss
#
#     rss = {k: read1(v) for k, v in data_files.items()}
#     for k, v in rss.items():
#         plt.figure()
#         plt.plot(v)
#         plt.title(k)
#     plt.show()
#
#
# def insert_parameters_from_dct_into_antimony(dct, model_string):
#     import re
#     for k, v in dct.items():
#         p = '^    ' + k + ' .*'
#         model_string = re.sub(p, '    ' + k + '\t\t=' + str(v) + ';', model_string, flags=re.MULTILINE)
#     return model_string
#
# def plot_likelihood_ranks(pe):
#     pass
#
#
# def simulation_with_t47d_ics(mod, t47d_data, problem):
#     # mod = te.loada(model_string)
#     # dct = {'FourEBP1': 3.2466649329564135, 'FourEBP1pT37_46': 0.7124890900275289, 'Akt': 2.8086251256904022, 'AktpT308': 0.7665804071985246, 'Erk_pT202_Y204': 0.39184126883631254, 'IRS1': 2.1221090610329165, 'IRS1pS636_639': 0.4200918742913655, 'PRAS40': 3.0166401225784516, 'PRAS40pT246': 1.1005998527632517, 'S6K': 2.394884041398308, 'S6KpT389': 0.5414110988836646, 'TSC2': 2.9584411371727395, 'TSC2pT1462': 1.1184222827344148}
#     replacement_names = {
#         'FourEBP1_obs': 'FourEBP1_tot',
#         'FourEBP1pT37_46_obs': 'FourEBP1pT37_46',
#         'Akt_obs': 'Akt_tot',
#         'AktpS473_obs': 'AktpS473',
#         'AktpT308_obs': 'AktpT308',
#         'ERK_obs': 'Erk_tot',
#         'ErkpT202_Y204': 'Erk_pT202_Y204',
#         'IRS1_obs': 'IRS1_tot',
#         'IRS1pS636_639_obs': 'IRS1pS636_639',
#         'PRAS40_obs': 'PRAS40_tot',
#         'PRAS40pS183_obs': 'PRAS40pS183',
#         'PRAS40pT246_obs': 'PRAS40pT246',
#         'S6K_obs': 'S6K_tot',
#         'S6KpT229_obs': 'S6KpT229',
#         'S6KpT389_obs': 'S6KpT389',
#         'TSC2_obs': 'TSC2_tot',
#         'TSC2pT1462_obs': 'TSC2pT1462',
#         'p38_obs': 'p38_tot',
#         'p38_pT180_Y182_obs': 'p38_pT180_Y182',
#     }
#     for label, df in t47d_data.groupby(level='repeats'):
#         df = df.reset_index()
#         # df['antibody'] = [i.replace('_obs', '') for i in df['antibody']]
#         df = df.drop('repeats', axis=1)
#         df = df.set_index('antibody')
#         df = df.transpose().iloc[0]
#         df = df.rename(replacement_names)
#         dct = df.to_dict()
#         dct = {k: v for k, v in dct.items() if k in mod}
#         mod.insert_parameters(parameter_dict=dct)
#         # mod.set('global_quantity', 'Insulin', 0.05, match_field='name', change_field='initial_value')
#         # ss_data = mod.simulate(0, 120, 1, variables='gm')
#         # simulate insulin stimulated condition
#         mod.set('global_quantity', 'Insulin', 1, match_field='name', change_field='initial_value')
#         mod.set('global_quantity', 'offset_amount', 1, match_field='name', change_field='initial_value')
#         data = mod.simulate(0, 120, 2, variables='gm')
#         exp = GetDataFromOldDataFile(EXPERIMENTAL_DATA_FILE).get_data_normalised_to_coomassie_blue(
#             offset_for_total_proetins=2)
#         exp = exp.stack()
#         exp = exp.loc['T47D']
#         exp = exp.rename(columns={'4E_BP1': 'FourE_BP1',
#                                   '4E_BP1pT37_46': 'FourEBP1pT37_46',
#                                   'ERK': 'Erk',
#                                   'ERK_pT202_Y204': 'Erk_pT202_Y204',
#                                   })
#
#         phospho_species_that_were_fitted = ['AktpT308_obs', 'FourEBP1pT37_46_obs',
#                                             'IRS1pS636_639_obs', 'PRAS40pT246_obs',
#                                             'S6KpT389_obs', 'TSC2pT1462_obs',
#                                             'Erk_pT202_Y204']
#
#         ss_sim = data[sorted(['IRS1_tot', 'Akt_tot', 'TSC2_tot',
#                               'PRAS40_tot', 'FourEBP1_tot', 'S6K_tot',
#                               'Erk_tot'])]
#
#         ss_exp = exp[sorted(['FourE_BP1', 'Akt', 'IRS1',
#                              'PRAS40', 'S6K', 'TSC2', 'Erk'])]
#
#         ts_sim = data[sorted(phospho_species_that_were_fitted)]
#
#         ts_exp = exp[sorted([i.replace('_obs', '') for i in phospho_species_that_were_fitted])]
#
#         assert ss_sim.shape[1] == 7, ss_sim.shape[1]
#         assert ss_exp.shape[1] == 7, ss_exp.shape[1]
#         assert ts_sim.shape[1] == 7, ts_sim.shape[1]
#         assert ts_exp.shape[1] == 7, ts_exp.shape[1]
#
#         fig = plt.figure(figsize=(20, 10))
#         for i in range(ss_sim.shape[1]):
#             ax = plt.subplot(3, 3, i + 1)
#             ss_sim_var = ss_sim.columns[i]
#             ss_exp_var = ss_exp.columns[i]
#             ts_sim_var = ts_sim.columns[i]
#             ts_exp_var = ts_exp.columns[i]
#
#             ss_sim_plt = ss_sim[ss_sim.columns[i]]
#             ts_sim_plt = ts_sim[ts_sim.columns[i]]
#
#             # steady state stuff
#             total_color = 'green'
#             phos_color = 'blue'
#             # seaborn.lineplot(x='time', y=ss_exp_var,
#             #                  data=ss_exp.reset_index(), label='Total protein, experimental',
#             #                  ax=ax, legend=False, color=total_color,
#             #                  markers=True)
#             # ax.lines[0].set_linestyle("--")
#             # ax.paired_plot(ss_sim_plt.index, ss_sim_plt.values, label='Total protein, simulated',
#             #         linestyle='-', color=total_color,
#             #         )
#
#             # time series stuff
#             seaborn.lineplot(x='time', y=ts_exp_var, data=ts_exp.reset_index(),
#                              label='pProtein, experimental', ax=ax, legend=False, color=phos_color,
#                              markers=True
#                              )
#             ax.lines[0].set_linestyle("--")
#
#             ax.plot(ts_sim_plt.index, ts_sim_plt.values, label='pProtein, simulated',
#                     linestyle='-', color=phos_color)
#
#             plt.title(ss_exp_var)
#             seaborn.despine(fig=fig, top=True, right=True)
#             plt.xlabel('')
#             plt.ylabel('')
#         # plt.subplots_adjust(left=0.25, right=0.25, top=0.25, bottom=0.25)
#         plt.subplots_adjust(wspace=0.1, hspace=0.4)
#         plt.legend(loc=(1.35, 0.1))
#         # plt.show()
#         fname = os.path.join(SIMULATION_GRAPHS_DIR, '{}_{}_simulations.png'.format(problem, label))
#         fig.savefig(fname, dpi=300, bbox_inches='tight')
#         print('figure saved to "{}"'.format(fname))
#
#
# if __name__ == '__main__':
#
#     # Build a new sbml model from scratch. When False, the existing model is worked on
#     BUILD_NEW = True
#     # indicates which problem we are on. Increment when you try something new
#     # PROBLEM = 2 #45 minute interpolation
#     PROBLEM = '1_first_try' # didn't get a fit with all of the data in the estimation.
#     PROBLEM = '2_individual_cell_lines'
#     PROBLEM = '3_individual_cell_lines' # Like 3. But with lower lower bound.
#     PROBLEM = '4_fix_backwards_parameters' # Like 3. But with S6K 4ebp and pras40 backwards parameters fixed to 1
#     PROBLEM = '5_fixed_more_parameters_based_on_MCF7_sims' # I fixed parameters for Akt, TSC and S6Kp based on MCF7 simulations
#     PROBLEM = '6_with_interpolation' # interpolated the data so that we have 20 data points per time series
#     PROBLEM = '7_TSC_to_s6k_roles_reversed' # Like 6. But TSC2pT1462 phosphorylates S6K rather than TSC.
#     PROBLEM = '8_OffsetForInactiveSpecies' # like 5. But I have added offest parameter to inactive proteins, rather than total proteins.
#     PROBLEM = '9_1000ParameterEstimationsPerModel' # same as 8 but running each model 1000 times with more stringent hyperparameters
#
#     # passed on to the run_mode in ParameterEstimation. Can be False, True, or 'slurm'
#     three = ['T47D', 'ZR-75', 'MCF7']
#     parameter_dfs = {}
#     for FIT in ['MCF7']:#three:
#     # FIT = 'MCF7'
#         if FIT == 'MCF7':
#             COPASI_DATA_FILES_SUBSET = [i for i in COPASI_DATA_FILES if 'MCF7' in i]
#         elif FIT == 'T47D':
#             COPASI_DATA_FILES_SUBSET = [i for i in COPASI_DATA_FILES if 'T47D' in i]
#         elif FIT == 'ZR-75':
#             COPASI_DATA_FILES_SUBSET = [i for i in COPASI_DATA_FILES if 'ZR-75' in i]
#
#         if COPASI_DATA_FILES_SUBSET == []:
#             raise ValueError('COPASI_DATA_FILES is empty')
#         if len(COPASI_DATA_FILES_SUBSET) != 4:
#             raise ValueError('Do not have 4 data files...you have {}'.format(len(COPASI_DATA_FILES_SUBSET)))
#         # FIT = 3 #current
#         RUN = False
#         # Open the sbml model in copasi
#         OPEN = True
#         # Parameter estimation copy number argument. Is automatically changed when RUN='slurm'
#         COPY_NUMBER = 1
#         # Open with copasi with best parameter set from PROBLEM
#         OPEN_WITH_BEST_PARAMETERS = False
#         # Run profile likelihoods
#         RUN_PROFIE_LIKELIHOOD = False
#         # paired_plot the best fits in presentable format
#         PLOT_BEST_FIT = False
#
#         PLOT_PL = False
#
#         # set to True to run a simulation from different initial conditions
#         RUN_SIMULATION_FROM_DIFFERENT_INITIAL_CONDITIONS = False
#
#         # paired_plot likelihood ranks
#         PLOT_LIKELIHOOD_RANKS = False
#
#         COMPARE_PARAMETERS = True
#
#         ###########################################
#
#         if PLOT_PL:
#             plotpl()
#
#         if BUILD_NEW:
#             mod = model.loada(model_string, copasi_file=COPASI_FILE)
#         else:
#             mod = model.Model(COPASI_FILE)
#
#         if RUN == 'slurm':
#             COPY_NUMBER = 1000
#         elif RUN == True:
#             COPY_NUMBER = 1
#         elif RUN == 'parallel':
#             COPY_NUMBER = 6
#
#         if COPY_NUMBER == 0:
#             raise ValueError
#
#         with tasks.ParameterEstimation.Context(mod, COPASI_DATA_FILES_SUBSET, parameters='gm') as context:
#             context.set('separator', ',')
#             context.set('run_mode', RUN)
#             context.set('problem', 'Problem{}'.format(PROBLEM))
#             context.set('fit', '{}'.format(FIT))
#             context.set('copy_number', COPY_NUMBER)
#             context.set('randomize_start_values', True)
#             context.set('method', 'particle_swarm')
#             context.set('population_size', 200)
#             context.set('swarm_size', 300)
#             context.set('iteration_limit', 4000)
#             context.set('lower_bound', 0.0001)
#             context.set('upper_bound', 10000)
#             context.set('weight_method', 'standard_deviation')
#             context.set('prefix', '_')
#             config = context.get_config()
#
#             pe = tasks.ParameterEstimation(config)
#             mod = pe.models['simple_akt_model'].model
#
#         if RUN_PROFIE_LIKELIHOOD:
#             with tasks.ParameterEstimation.Context(mod, [SS_DATA_FILE] + COPASI_INTERP_DATA_FILES,
#                                                    context='pl', parameters='g'
#                                                    ) as context:
#                 context.set('method', 'hooke_jeeves')
#                 context.set('pl_lower_bound', 1000)
#                 context.set('pl_upper_bound', 1000)
#                 context.set('pe_number', 10)
#                 context.set('run_mode', True)
#                 context.set('prefix', '_')
#                 context.set('weight_method', 'standard_deviation')
#
#                 context.set('separator', '\t')
#                 # context.set('method', 'particle_swarm')
#                 # context.set('swarm_size', 50)
#                 # context.set('iteration_limit', 2000)
#
#                 config = context.get_config()
#
#                 pl = tasks.ParameterEstimation(config)
#
#         if OPEN:
#             mod.open()
#
#         if OPEN_WITH_BEST_PARAMETERS:
#             data = viz.Parse(pe).data
#             print(data['simple_akt_model'].iloc[0])
#             mod.insert_parameters(df=data['simple_akt_model'], index=0, inplace=True)
#
#             print(mod.open())
#
#         if PLOT_BEST_FIT:
#             # plot_best_fit(PROBLEM)
#             plot_best_fit2(mod, PROBLEM, cell_line=FIT, savefig=True)
#
#         if RUN_SIMULATION_FROM_DIFFERENT_INITIAL_CONDITIONS:
#             t47d_data = GetDataFromOldDataFile(EXPERIMENTAL_DATA_FILE).get_ics_for_t47d(offset_for_total_proetins=1)
#             # print(simulation_with_t47d_ics(model_string, t47d_data))
#             print(simulation_with_t47d_ics(mod, t47d_data, 't47d'))
#
#         if PLOT_LIKELIHOOD_RANKS:
#             plot_likelihood_ranks(pe)
#
#         if COMPARE_PARAMETERS:
#             data = viz.Parse(pe).data
#             parameter_dfs[FIT] = data['simple_akt_model']
#
#     if COMPARE_PARAMETERS:
#         df = pandas.concat(parameter_dfs)
#         df = df.xs(key=0, level=1).transpose()
#         print(df)
#         df.to_csv(os.path.join(DATA_DIRECTORY, 'parameters_df.csv'))