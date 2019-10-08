import pandas, numpy
from functools import reduce
import os, glob
import xlrd
import matplotlib.pyplot as plt
import seaborn
from scipy.interpolate import interp1d
import site
from pathlib import Path

site.addsitedir(r'D:\pytseries')
from pytseries.core import TimeSeries, TimeSeriesGroup

WORKING_DIRECTORY = Path(os.path.abspath(__file__)).parents[1]
DATA_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'data')
DATA_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'data')
DATA_FILE = os.path.join(DATA_DIRECTORY, 'experimental_data.xlsx')
DATA_FILE_NORMED_TO_MAX =  os.path.join(DATA_DIRECTORY, 'experimental_data_with_norm_to_max.csv')

SS_DATA_FILE = fname = os.path.join(DATA_DIRECTORY, 'ss_data.csv')
SS_DATA_FILE = fname = os.path.join(DATA_DIRECTORY, 'steady_state_data_quantified.csv')
PLOTS_DIR = os.path.join(DATA_DIRECTORY, 'plots')
COPASI_DATA_FILES_DIR = os.path.join(DATA_DIRECTORY, 'CopasiDataFiles')

COPASI_DATA_FILES_DIR = os.path.join(DATA_DIRECTORY, 'CopasiDataFiles')
COPASI_DATA_FILES = glob.glob(os.path.join(COPASI_DATA_FILES_DIR, '*.csv'))

SIMULATION_GRAPHS_DIR = os.path.join(PLOTS_DIR, 'simulation_graphs')
if not os.path.isdir(SIMULATION_GRAPHS_DIR):
    os.makedirs(SIMULATION_GRAPHS_DIR)
OFFSET_PARAMETER = 0

total_proteins = ['4E_BP1_obs', 'Akt_obs', 'ERK_obs', 'IRS1_obs',
                  'PRAS40_obs', 'S6K_obs', 'TSC2_obs']
replacement_names = {
    '4E_BP1': 'FourEBP1_obs',
    '4E_BP1pT37_46': 'FourE_BP1pT37_46_obs',
    'Akt': 'Akt_obs',
    'AktpS473': 'AktpS473_obs',
    'AktpT308': 'AktpT308_obs',
    'Coomassie staining': 'Coomassie_obs',
    'ERK': 'ERK_obs',
    'GAPDH': 'GAPDH_obs',
    'IRS1': 'IRS1_obs',
    'IRS1pS636_639': 'IRS1pS636_639_obs',
    'PRAS40': 'PRAS40_obs',
    'PRAS40pS183': 'PRAS40pS183_obs',
    'PRAS40pT246': 'PRAS40pT246_obs',
    'S6K': 'S6K_obs',
    'S6KpT229': 'S6KpT229_obs',
    'S6KpT389': 'S6KpT389_obs',
    'TSC2': 'TSC2_obs',
    'TSC2pT1462': 'TSC2pT1462_obs',
    'ERK_pT202_Y204': 'Erk_pT202_Y204_obs',
    'p38': 'p38_obs',
    'p38_pT180_Y182': 'p38_pT180_Y182_obs',
    'ER alpha': 'ER_alpha'
}

replacement_names_2 = {
    '4E_BP1': 'FourEBP1_tot',
    '4E_BP1pT37_46': 'FourE_BP1pT37_46',
    'Akt': 'Akt_tot',
    'AktpS473': 'AktpS473',
    'AktpT308': 'AktpT308',
    'Coomassie staining': 'Coomassie_obs',
    'ERK': 'Erk_tot',
    'GAPDH': 'GAPDH_obs',
    'IRS1': 'IRS1_tot',
    'IRS1pS636_639': 'IRS1pS636_639',
    'PRAS40': 'PRAS40_tot',
    'PRAS40pS183': 'PRAS40pS183',
    'PRAS40pT246': 'PRAS40pT246',
    'S6K': 'S6K_tot',
    'S6KpT229': 'S6KpT229',
    'S6KpT389': 'S6KpT389',
    'TSC2': 'TSC2_tot',
    'TSC2pT1462': 'TSC2pT1462',
    'ERK_pT202_Y204': 'Erk_pT202_Y204',
    'p38': 'p38_tot',
    'p38_pT180_Y182': 'p38_pT180_Y182',
    'ER alpha': 'ER_alpha_tot'
}

replacement_names_3 = {
    '4E-BP1': 'FourEBP1',
    '4E-BP1pT37/46': 'FourEBP1pT37_46',
    'ERK': 'Erk',
    'ERK-pT202/Y204': 'pT202_Y204',
    'IRS1pS636/639': 'IRS1pS636_639',
    'p38-pT180/Y182': 'p38_pT180_Y182',
    'ER alpha': 'ER_alpha'
}


class GetDataFromOldDataFile:
    time = [0, 15, 30, 60, 90, 120]
    condition_names = ['MCF-7 0 minutes ins + aa', 'MCF-7 15 minutes ins + aa', 'MCF-7 30 minutes ins + aa',
                       'MCF-7 60 minutes ins + aa', 'MCF-7 90 minutes ins + aa', 'MCF-7 120 minutes ins + aa',
                       'T47D 0 minutes ins + aa', 'T47D 15 minutes ins + aa', 'T47D 30 minutes ins + aa',
                       'T47D 60 minutes ins + aa', 'T47D 90 minutes ins + aa', 'T47D 120 minutes ins + aa']
    condition_codes = [f'MCF{i}' for i in time] + [f'T47D{i}' for i in time]
    assert len(condition_names) == len(condition_codes)
    antibodies = ['Akt', 'AktpT308', 'AktpS473', 'PRAS40', 'PRAS40pT246',
                  'PRAS40pS183', 'S6K', 'S6KpT389', 'S6KpT229',
                  'TSC2', 'TSC2pT1462', 'IRS1', 'IRS1pS636/639', '4E-BP1',
                  '4E-BP1pT37/46', 'GAPDH',
                  'ERK', 'Coomassie staining', 'ERK-pT202/Y204', 'p38',
                  'p38-pT180/Y182', 'ER alpha']

    antibodies = [i.replace('/', '_') for i in antibodies]
    antibodies = [i.replace('-', '_') for i in antibodies]

    def __init__(self, workbook):
        self.workbook = xlrd.open_workbook(workbook)

    def get_sheet_names(self):
        return self.workbook.sheet_names()

    def get_antibody_names(self):
        sheet = 'Sheet2'
        sheet = self.workbook.sheet_by_name(sheet)
        columns = sheet.row_slice(0)
        columns = [i.value for i in columns]
        columns = [i for i in columns if i != '']
        return columns

    def get_raw_data(self):
        sheet = 'Sheet2'
        sheet = self.workbook.sheet_by_name(sheet)

        data = [sheet.col_slice(i, 2, 14) for i in range(1, 89)]
        new_data = []
        for i in data:
            new_data.append([j.value for j in i])

        df = pandas.DataFrame(new_data).transpose()

        # sanity checks
        top_left = 2599775
        bottom_left = 1503056
        top_right = 76100
        bottom_right = 20282

        assert top_left == df.loc[0, 0]
        assert bottom_left == df.loc[df.shape[0] - 1, 0], f'{bottom_left} is not {df.loc[df.shape[0] - 1, 0]}'
        assert top_right == df.loc[0, df.shape[1] - 1], f'{top_right} != {df.loc[0, df.shape[1] - 1]}'
        assert bottom_right == df.loc[df.shape[0] - 1,
                                      df.shape[1] - 1], f'{top_right} != {df.loc[df.shape[0] - 1, df.shape[1] - 1]}'
        # print(df.columns)
        # print(len(self.antibodies))
        # print(df.shape)
        assert df.shape[1] / 4 == len(self.antibodies)

        df['cell_line'] = ['MCF7'] * 6 + ['T47D'] * 6
        df['time'] = [0, 15, 30, 60, 90, 120] * 2
        df = df.set_index(['cell_line', 'time'])

        df = df.transpose()
        antibody = [[i] * 4 for i in self.antibodies]
        antibody = reduce(lambda x, y: x + y, antibody)
        df['antibody'] = antibody

        repeats = [0, 1, 2, 3] * len(self.antibodies)
        df['repeats'] = repeats
        df = df.set_index(['antibody', 'repeats'])

        df = df.transpose()

        return df

    def get_data_normed_to_average(self):
        data = self.get_raw_data()
        df = data / data.mean()
        return df

    def get_data_normalised_to_coomassie_blue(self, offset_for_total_proetins=0):
        """
        normalise data to coomassie blue
        :param offset_for_total_proetins: (numeric). This number is added to total protein levels so that the amount
                                            of total protein is always larger than the amount of phospho proteins.
        :return:
        """
        # first normalise to average
        total_proteins = ['4E_BP1_obs', 'Akt_obs', 'ERK_obs', 'IRS1_obs',
                          'PRAS40_obs', 'S6K_obs', 'TSC2_obs']
        total_proteins = [i.replace('_obs', '') for i in total_proteins]
        print('Warning. We have added 1 to the total protein data sets ({}). Always remember this. '.format(
            total_proteins))
        # we have added the offset parameter!
        data = self.get_data_normed_to_average()
        df_dct = {}
        for ab in self.antibodies:
            df = data[ab]
            df_dct[ab] = df / data['Coomassie staining']

        for tprotein in total_proteins:
            df_dct[tprotein] = df_dct[tprotein] + offset_for_total_proetins

        return pandas.concat(df_dct, axis=1)

    def to_copasi_format(self, fname, delimiter='\t', data=None):
        if data is None:
            data = self.get_data_normalised_to_coomassie_blue()
        data = data.stack()
        try:
            data = data.loc['MCF7']
        except KeyError:
            pass
        data['Insulin_indep'] = 1
        data.index = data.index.swaplevel(0, 1)
        data = data.sort_index(level='repeats')
        old_names = ['4E_BP1', '4E_BP1pT37_46', 'Akt',
                     'AktpS473', 'AktpT308',
                     'Coomassie staining', 'ERK',
                     'GAPDH', 'IRS1', 'IRS1pS636_639', 'PRAS40',
                     'PRAS40pS183', 'PRAS40pT246', 'S6K',
                     'S6KpT229', 'S6KpT389', 'TSC2',
                     'TSC2pT1462', 'Insulin_indep']

        data = data.rename(columns=replacement_names)
        repeats = list(set(data.index.get_level_values(0)))
        data = data.reset_index(level=1)

        # data = data[data['time'] < 60]
        # print(data)
        s = ''
        for name in data.columns:
            s += name + delimiter
        s = s.strip()
        s += '\n'
        count = 0
        for repeat in repeats:
            count += 1
            df = data.loc[repeat].values
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    s += str(round(df[i, j], 6)) + delimiter
                s = s.strip()
                s += '\n'
            s += '\n'
            if count == len(repeats):
                s = s.strip()

        with open(fname, 'w') as f:
            f.write(s)

        print('Written copasi formatted data to "{}"'.format(fname))

        return s

    def to_copasi_format_multiple_files(self, fname, delimiter='\t', data=None):
        if data is None:
            data = self.get_data_normalised_to_coomassie_blue()
        data = data.stack()
        try:
            data = data.loc['MCF7']
        except KeyError:
            pass
        data['Insulin_indep'] = 1
        data.index = data.index.swaplevel(0, 1)
        data = data.sort_index(level='repeats')
        old_names = ['4E_BP1', '4E_BP1pT37_46', 'Akt',
                     'AktpS473', 'AktpT308',
                     'Coomassie staining', 'ERK',
                     'GAPDH', 'IRS1', 'IRS1pS636_639', 'PRAS40',
                     'PRAS40pS183', 'PRAS40pT246', 'S6K',
                     'S6KpT229', 'S6KpT389', 'TSC2',
                     'TSC2pT1462', 'Insulin_indep']

        data = data.rename(columns=replacement_names)

        ic_dct = {}
        exclude = ['Insulin_indep', 'FourEBP1_obs', 'Akt_obs',
                   'ERK_obs', 'GAPDH_obs', 'IRS1_obs', 'PRAS40_obs',
                   'S6K_obs', 'TSC2_obs']
        for label, df in data.groupby(level='repeats'):
            ic_dct[label] = df.loc[label, 0]
        ic_df = pandas.concat(ic_dct).unstack(level=0)
        ic_df = ic_df.drop(exclude)
        print(ic_df)
        new_idx = [i[:-4] + '_indep' for i in ic_df.index]  # if i[:-4] not in exclude]
        ic_df.index = new_idx

        repeats = list(set(data.index.get_level_values(0)))
        data = data.reset_index(level=1)

        data = data[data['time'] < 75]

        # print('ic df', ic_df)

        fnames = []
        for r in range(len(repeats)):
            fnames.append(os.path.splitext(fname)[0] + str(r) + '.csv')

        for rep in repeats:
            s = ''
            for name in data.columns:
                s += name + delimiter
            s = s.strip()
            s += '\n'
            df = data.loc[rep]
            for ic in ic_df.index:
                ic_val = ic_df.loc[ic, rep]
                ic_val = round(ic_val, 4)
                df[ic] = ic_val
            df.reset_index(drop=True, inplace=True)

            df.to_csv(fnames[rep], sep='\t', index=False)
            print('data written to {}'.format(fnames[rep]))

    def interpolate_mcf7_data(self, num=12, offset_for_total_proetins=0):
        data = self.get_data_normalised_to_coomassie_blue(offset_for_total_proetins=offset_for_total_proetins)
        data = data.transpose()
        data.index.names = ['antibody', 'repeats']
        data = data.transpose()
        data = data.loc['MCF7']
        data = data.stack().unstack(level=0).stack(level=0)
        data.index = data.index.swaplevel(0, 1)
        tsg_dct = {}
        for label, df in data.groupby(level='repeats'):
            df.index = df.index.droplevel('repeats')
            tsg = TimeSeriesGroup(df).interpolate(kind='linear', num=num)
            tsg = tsg.as_df()
            tsg_dct[label] = tsg

        data2 = pandas.concat(tsg_dct)
        data2.index.names = ['repeats', 'antibody']
        data2.columns.names = data.columns.names
        data2 = data2.unstack(level=1).stack(level=0).unstack(level=0)
        # data2.index = [(round(i, 3) for i in data2.index)]
        # print(data2)
        return data2

    def get_ics_for_t47d(self, offset_for_total_proetins=0):
        data = self.get_data_normalised_to_coomassie_blue(offset_for_total_proetins=offset_for_total_proetins)
        data = data.transpose()
        data.index.names = ['antibody', 'repeats']
        data = data.transpose()
        data = data.loc['T47D', 0]
        data = data.rename(replacement_names)
        data = pandas.DataFrame(data)
        data.columns = [0]
        return (data)
        # data = data.stack().unstack(level=0).stack(level=0)
        # data.index = data.index.swaplevel(0, 1)
        # tsg_dct = {}
        # for label, df in data.groupby(level='repeats'):
        #     df.index = df.index.droplevel('repeats')
        #     tsg = TimeSeriesGroup(df).interpolate(kind='linear', num=num)
        #     tsg = tsg.as_df()
        #     tsg_dct[label] = tsg
        #
        # data2 = pandas.concat(tsg_dct)
        # data2.index.names = ['repeats', 'antibody']
        # data2.columns.names = data.columns.names
        # data2 = data2.unstack(level=1).stack(level=0).unstack(level=0)
        # # data2.index = [(round(i, 3) for i in data2.index)]
        # # print(data2)
        # return data2


class GetDataNormedToMax:
    replacement_names = {
        '4E-BP1': 'FourEBP1',
        '4E-BP1pT37/46': 'FourEBP1pT37_46',
        'ERK': 'Erk',
        'ERK-pT202/Y204': 'ErkpT202_Y204',
        'IRS1pS636/639': 'IRS1pS636_639',
        'p38-pT180/Y182': 'p38pT180Y182',
        'ER alpha': 'ER_alpha'
    }

    total_proteins = ['4E_BP1_obs', 'Akt_obs', 'ERK_obs', 'IRS1_obs',
                      'PRAS40_obs', 'S6K_obs', 'TSC2_obs']
    observable_names = {
        '4EBP1': 'FourEBP1_obs',
        '4EBP1pT37_46': 'FourEBP1pT37_46_obs',
        'Akt': 'Akt_obs',
        'AktpS473': 'AktpS473_obs',
        'AktpT308': 'AktpT308_obs',
        'ERK': 'ERK_obs',
        'GAPDH': 'GAPDH_obs',
        'IRS1': 'IRS1_obs',
        'IRS1pS636_639': 'IRS1pS636_639_obs',
        'PRAS40': 'PRAS40_obs',
        'PRAS40pS183': 'PRAS40pS183_obs',
        'PRAS40pT246': 'PRAS40pT246_obs',
        'S6K': 'S6K_obs',
        'S6KpT229': 'S6KpT229_obs',
        'S6KpT389': 'S6KpT389_obs',
        'TSC2': 'TSC2_obs',
        'TSC2pT1462': 'TSC2pT1462_obs',
        'ERKpT202Y204': 'ErkpT202Y204_obs',
        'p38': 'p38_obs',
        'p38pT180Y182': 'p38pT180Y182_obs',
        'ER alpha': 'ER_alpha_obs'
    }

    total_proteins = ['FourEBP1', 'Akt', 'ER_alpha', 'Erk',
                      'GAPDH', 'IRS1', 'PRAS40', 'S6K', 'TSC2', 'p38']

    inactive_species = [i for i in total_proteins if i not in ['IRS1', 'TSC2']] + ['IRS1pS636_639']

    def __init__(self, fname):
        self.fname = fname

    def read_data(self, offset_for_inactive_species=OFFSET_PARAMETER):
        data = pandas.read_csv(self.fname, index_col=[0, 1], header=[0, 1])
        data = data.stack()
        data.index.names = ['cell_line', 'time', 'repeat']
        data = data.rename(columns=self.replacement_names, level=0)
        for i in data:
            if i in self.inactive_species:
                data[i] = data[i] + offset_for_inactive_species
        return data

    def to_copasi_format(self, prefix='normed_to_max', interpolation_num=20):
        data = self.read_data(OFFSET_PARAMETER)
        data.index = data.index.swaplevel(1, 2)
        data = data.sort_index(level=[0, 1, 2])
        # print(data)
        dct = {}
        for label, df in data.groupby(level=[0, 1]):
            df = df.loc[label]
            tsg = TimeSeriesGroup(df.transpose()).interpolate(kind='linear', num=interpolation_num)
            df = tsg.as_df().transpose()
            df.index.name = 'time'
            dct[label] = df
        data = pandas.concat(dct)
        data.index.names = ['cell_line', 'repeat', 'time']
        for label, df in data.groupby(level=['cell_line', 'repeat']):
            ics = df.iloc[0]
            ics.name = None
            ics = pandas.DataFrame(ics).transpose()
            ics = ics.drop(self.total_proteins, axis=1)
            ics.columns = [f'{i}_indep' for i in ics.columns]
            ics = pandas.concat([ics] * df.shape[0], axis=0)
            insulin = pandas.DataFrame(pandas.Series([1.0] * df.shape[0]),
                                       columns=['Insulin_indep'])
            ics.index = df.index
            insulin.index = df.index

            df2 = pandas.concat([df, ics, insulin], axis=1)
            df2 = df2.loc[label]

            df2 = df2.dropna(how='all', axis=1)
            fname = os.path.join(COPASI_DATA_FILES_DIR, f'{prefix}_{label[0]}{label[1]}.csv')
            df2 = df2.drop(self.total_proteins, axis=1)
            df2 = df2.rename(columns=self.observable_names)
            df2.to_csv(fname)
        print(data.columns)

    def interpolate_mcf7_data(self, num=12, offset_for_total_proetins=0):
        data = self.get_data_normalised_to_coomassie_blue(offset_for_total_proetins=offset_for_total_proetins)
        data = data.transpose()
        data.index.names = ['antibody', 'repeats']
        data = data.transpose()
        data = data.loc['MCF7']
        data = data.stack().unstack(level=0).stack(level=0)
        data.index = data.index.swaplevel(0, 1)
        tsg_dct = {}
        for label, df in data.groupby(level='repeats'):
            df.index = df.index.droplevel('repeats')
            tsg = TimeSeriesGroup(df).interpolate(kind='linear', num=num)
            tsg = tsg.as_df()
            tsg_dct[label] = tsg

        data2 = pandas.concat(tsg_dct)
        data2.index.names = ['repeats', 'antibody']
        data2.columns.names = data.columns.names
        data2 = data2.unstack(level=1).stack(level=0).unstack(level=0)
        # data2.index = [(round(i, 3) for i in data2.index)]
        # print(data2)
        return data2

    def get_average_of_0_time_points(self, offset_for_inactive_species=0):
        data = self.read_data(offset_for_inactive_species=offset_for_inactive_species).xs(0, level=1)
        mean = data.mean(level=0)
        print(mean.transpose())
        return mean

    def ss_data_to_copasi_format(self):
        total_proteins = ['FourEBP1_obs', 'Akt_obs', 'ERK_obs', 'IRS1_obs',
                          'PRAS40_obs', 'S6K_obs', 'TSC2_obs']
        data = self.read_data(offset_for_inactive_species=OFFSET_PARAMETER)
        data = data.xs(key=0, level='time').mean(level='cell_line')
        print(data)
        # data = data.rename(columns=replacement_names_2)
        # data['Insulin_indep'] = 0.005
        # for i in total_proteins:
        #     data[i] = data[i] + 1
        # data.to_csv(SS_DATA_FILE, index=False, sep='\t')
        # return data

    def plot(self, cell_line, plot_selection={}, subplot_titles={},
             ncols=3, wspace=0.25, hspace=0.3, **kwargs):
        if plot_selection == {}:
            plot_selection = {
                0: ['IRS1', 'IRS1pS636_639'],
                1: ['Akt', 'AktpT308', 'AktpS473'],
                2: ['TSC2', 'TSC2pT1462'],
                3: ['S6K', 'S6KpT229', 'S6KpT389'],
                4: ['FourEBP1', 'FourEBP1pT37_46'],
                5: ['PRAS40', 'PRAS40pT246', 'PRAS40pS183'],
                6: ['p38', 'p38pT180Y182'],
                7: ['Erk', 'ErkpT202_Y204'],

            }
        if subplot_titles == {}:
            subplot_titles = {
                0: 'IRS1',
                1: 'Akt',
                2: 'TSC2',
                3: 'S6K',
                4: '4EBP',
                5: 'Pras40',
                6: 'p38',
                7: 'Erk'
            }
        from matplotlib.gridspec import GridSpec
        _nplots = len(plot_selection)
        if _nplots == 1:
            ncols = 1
        _num_rows = int(_nplots / ncols)
        _remainder = _nplots % ncols
        if _remainder > 0:
            _num_rows += 1
        data = self.read_data(offset_for_inactive_species=OFFSET_PARAMETER).loc[cell_line]
        avg = data.groupby(level='time').mean()
        sem = data.groupby(level='time').sem()
        fig = plt.figure(figsize=(12, 7))
        gs = GridSpec(_num_rows, ncols, wspace=wspace, hspace=hspace)
        for k, v in plot_selection.items():
            ax = fig.add_subplot(gs[k])
            for i in v:
                plt.errorbar(avg.index, avg[i], yerr=sem[i], marker='.', label=i,
                             ls='None', capsize=2)
            plt.legend(loc='best', fontsize=10)
            plt.title(subplot_titles[k])
            seaborn.despine(fig, top=True, right=True)
        plt.suptitle('Insulin Stimulation: {}'.format(cell_line))
        fname = os.path.join(PLOTS_DIR, 'experimental_data_{}.png'.format(cell_line))
        plt.savefig(fname, dpi=300, bbox_inches='tight')

class SteadyStateData(GetDataNormedToMax):

    def read_data(self, offset_for_inactive_species=OFFSET_PARAMETER):
        data = pandas.read_csv(self.fname, header=[0, 1], index_col=[0]).transpose()
        df_dct = {}
        for label, df in data.groupby(level=0):
            df = df.loc[label]
            new_idx = range(df.shape[0])
            df.index = new_idx
            df_dct[label] = df
        data = pandas.concat(df_dct)
        data.index.names = ['antibody', 'repeat']
        data = data.rename(level=0, index=self.replacement_names)
        return data

    def plot(self, hue='cell_line'):
        seaborn.set_context(context='talk')
        data = self.read_data(OFFSET_PARAMETER)
        data = data.stack()
        data = pandas.DataFrame(data)
        data.index.names = ['antibody', 'repeat', 'cell_line']
        data.columns = ['value']
        fig = plt.figure(figsize=(25, 10))
        other_args = dict(
            data=data.reset_index(), y='value',
            errcolor='black',
            edgecolor='black', linewidth=3,
            palette=['black', 'darkgrey', 'dimgrey'],
            units='repeat'
        )
        if hue == 'cell_line':
            seaborn.barplot(x='antibody', hue='cell_line', capsize=0.1,
                            **other_args)
        elif hue == 'antibody':
            seaborn.barplot(x='cell_line', hue='antibody', capsize=0,
                            **other_args)
        plt.legend(loc=(1, 0.1))
        plt.xticks(rotation=90)
        seaborn.despine(fig=fig, top=True, right=True)
        fname = os.path.join(PLOTS_DIR, 'steady_state_data_{}_hue.png'.format(hue))
        plt.savefig(fname, dpi=300, bbox_inches='tight')


def plot(data, prefix, savefig=False):
    data = data.stack().stack()
    data = pandas.DataFrame(data)
    for label, df in data.groupby(level=[3]):
        fig = plt.figure()

        seaborn.lineplot(x='time', y=0, data=df.reset_index(),
                         hue='cell_line', style='cell_line',
                         palette='bright', markers=True, ci=95, linestyle='-', estimator=None,
                         units='repeats')
        seaborn.despine(fig, top=True, right=True)
        plt.ylabel('AU')
        plt.title(label)
        fname = os.path.join(PLOTS_DIR, '{}_{}'.format(prefix, label))
        if savefig:
            plt.savefig(fname, dpi=200, bbox_inches='tight')

def plot2(data, prefix, savefig=False):
    data = data.stack()
    data = pandas.DataFrame(data)
    data.index.names = ['cell_line', 'time', 'repeat', 'antibody']
    for label, df in data.groupby(level=[3]):
        fig = plt.figure()

        seaborn.lineplot(x='time', y=0, data=df.reset_index(),
                         hue='cell_line', style='cell_line',
                         palette='bright', markers=True, ci=95, linestyle='-', estimator=None,
                         units='repeat')
        seaborn.despine(fig, top=True, right=True)
        plt.ylabel('AU')
        plt.title(label)
        fname = os.path.join(PLOTS_DIR, '{}_{}'.format(prefix, label))
        if savefig:
            plt.savefig(fname, dpi=200, bbox_inches='tight')


def principle_component_analysis(data, colourby='cell_line', savefig=False):
    data = data.stack()
    if colourby not in data.index.names:
        raise ValueError(f'colourby variable "{colourby}" not in "{data.index.names}"')
    from sklearn.decomposition import PCA
    from itertools import cycle
    pca = PCA(2)
    x = pca.fit_transform(data)
    explained_variance = pca.explained_variance_ratio_

    df = pandas.DataFrame(x, index=data.index)
    colourby_values = sorted(list(set(df.index.get_level_values(level=colourby))))
    colours = seaborn.color_palette("hls", len(colourby_values))

    fig = plt.figure()
    for i in colourby_values:
        df2 = df.xs(i, level=colourby)
        plt.scatter(df2[0], df2[1], label=i)
    seaborn.despine(fig=fig, top=True, right=True)
    plt.legend(loc='best')
    plt.title('PCA coloured by {}'.format(colourby))
    plt.xlabel('PC1 {}%'.format(round(explained_variance[0], 2) * 100))
    plt.ylabel('PC2 {}%'.format(round(explained_variance[1], 2) * 100))
    plt_dir = os.path.join(PLOTS_DIR, 'PCAPlots')
    if not os.path.isdir(plt_dir):
        os.makedirs(plt_dir)
    fname = os.path.join(plt_dir, 'PCAColouredBy{}.png'.format(colourby))
    if savefig:
        plt.savefig(fname, dpi=200, bbox_inches='tight')


def get_initial_conc():
    data = GetDataFromOldDataFile(DATA_FILE).get_data_normalised_to_coomassie_blue()
    data = data.stack()
    average = data.groupby(level=['cell_line', 'time']).mean()
    mcf70 = average.loc['MCF7', 0]
    return pandas.DataFrame(mcf70).transpose()


def ss_data_to_copasi_format():
    total_proteins = ['FourEBP1_obs', 'Akt_obs', 'ERK_obs', 'IRS1_obs',
                      'PRAS40_obs', 'S6K_obs', 'TSC2_obs']
    data = get_initial_conc()
    data = data.rename(columns=replacement_names_2)
    data['Insulin_indep'] = 0.005
    # for i in total_proteins:
    #     data[i] = data[i] + 1
    data.to_csv(SS_DATA_FILE, index=False, sep='\t')
    return data


if __name__ == '__main__':
    gd = GetDataFromOldDataFile(DATA_FILE)


