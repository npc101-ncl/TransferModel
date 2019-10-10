import pandas
import numpy as np
from functools import reduce
import os, glob
import xlrd
import matplotlib.pyplot as plt
import seaborn
from scipy.interpolate import interp1d
from matplotlib.gridspec import GridSpec

import site
from pathlib import Path

from transfer_model import *


class GetData:
    """
    Extract data from excel file. Preprocess the data.

    """
    zr75_sheet = 'MCF-7 vs ZR-75-1'
    t47d_sheet = 'MCF-7 vs T47D'

    def __init__(self, cell_line='ZR75', mean_or_median='mean'):
        self.workbook = xlrd.open_workbook(EXPERIMENTAL_DATA_FILE)
        self.cell_line = cell_line
        self.mean_or_median = mean_or_median

    def get_sheet_names(self):
        return self.workbook.sheet_names()

    def get_antibody_names(self):
        """
        gets list of antibody names
        Returns:

        """
        sheet = self.workbook.sheet_by_name(self.zr75_sheet)
        columns = sheet.row_slice(0)
        columns = [i.value for i in columns]
        columns = [i for i in columns if i not in ['', 'values']]
        # get rid of python unfriendly names
        columns = [i.replace('-', '_') for i in columns]
        columns = [i.replace('/', '_') for i in columns]
        columns = [i.replace(' ', '_') for i in columns]
        columns = [REPLACEMENT_NAMES[i] for i in columns]
        return columns

    def get_raw_data(self):
        """
        Retrieve the raw data from file named 'experimental_data_with_norm_to_max.xlsx.
        This corresponds to the first row of data - i.e. the unnormalised data.
        Args:
            cell_line: either ZR75 or T47D. Switch between the data sets.

        Returns:

        """
        if self.cell_line == 'T47D':
            sheet = self.t47d_sheet
        elif self.cell_line == 'ZR75':
            sheet = self.zr75_sheet
        else:
            raise ValueError
        sheet = self.workbook.sheet_by_name(sheet)

        data = [sheet.col_slice(i, 2, 14) for i in range(1, 89)]
        new_data = []
        for i in data:
            new_data.append([j.value for j in i])

        df = pandas.DataFrame(new_data).transpose()
        df['cell_line'] = ['MCF7'] * 6 + [self.cell_line] * 6
        df['time'] = [0, 15, 30, 60, 90, 120] * 2
        df = df.set_index(['cell_line', 'time'])

        df = df.transpose()
        antibody = [[i] * 4 for i in self.get_antibody_names()]
        antibody = reduce(lambda x, y: x + y, antibody)
        df['antibody'] = antibody

        repeats = [0, 1, 2, 3] * len(self.get_antibody_names())
        df['repeats'] = repeats
        df = df.set_index(['antibody', 'repeats'])

        df = df.transpose()

        # drop empty columns
        df = df.replace('None', np.nan, regex=True)
        df = df.dropna(axis=1, how='all')

        return df

    def normed_to_average(self, data=None):
        """
        First step in the normalisation process is normalisation to the average of each column.
        This process includes averaging the data from the different cell lines (not completly sure why
        but this is how they have done it).

        I would also like to explore the median
        Returns:

        """
        if data is None:
            data = self.get_raw_data()
        series_list = []
        for i in data:
            series_list.append(data[i] / data[i].mean())
        return pandas.concat(series_list, axis=1)

    def normed_to_median(self, data=None):
        """
        Replacement function for the first step in the normalisation process. The experiemntal
        guys use normalisatio of the average, even across cell lines. however, what if you
        have some very high and very low on one blot. Perhaps we can mitigate this by using median

        Returns:

        """
        if data is None:
            data = self.get_raw_data()
        series_list = []
        for i in data:
            series_list.append(data[i] / data[i].median())
        return pandas.concat(series_list, axis=1)

    def normalised_to_coomassie_blue(self, data=None, ):
        """
        Second step in normalisation process is to normalise for coomassie blue staining. This stain
        provides a metric for the total amount of protein loaded onto a gel.
        """
        if data is None:
            if self.mean_or_median == 'mean':
                data = self.normed_to_average()
            elif self.mean_or_median == 'median':
                data = self.normed_to_median()
            else:
                raise ValueError
        # we have added the offset parameter!
        df_dct = {}
        for ab in self.get_antibody_names():
            df = data[ab]
            df_dct[ab] = df / data['Coomassie_staining']

        return pandas.concat(df_dct, axis=1)

    def add_offset_to_total_proteins(self, data=None, total_proteins=None):
        """
        To prevent phospho proteins being present in a quantity greater than
        total proteins, add offset to the total proteins
        Args:
            data:

        Returns:

        """
        if data is None:
            data = self.normalised_to_coomassie_blue()
        # first normalise to average
        print(self.get_antibody_names())
        # if total_proteins is None:
        #     total_proteins = ['4E_BP1_obs', 'Akt_obs', 'ERK_obs', 'IRS1_obs',
        #                       'PRAS40_obs', 'S6K_obs', 'TSC2_obs']
        #     total_proteins = [i.replace('_obs', '') for i in total_proteins]
        #     print('Warning. We have added and OFFSET of {} to the total'
        #           ' protein data sets ({}). Always remember this.'.format(
        #         OFFSET_PARAMETER, total_proteins))
        #
        # for tprotein in total_proteins:
        #     data[tprotein] = data[total_proteins] + OFFSET_PARAMETER
        # return data

    def interpolate(self, data=None, num=12, kind='linear', **kwargs):
        """
        Interpolate the dataset usingg scipy.interpolate.interp1d. **kwargs get passed on to interp1d
        Args:
            data:
            num:
            kind:

        Returns:

        """
        if data is None:
            data = self.normalised_to_coomassie_blue()

        def interpolate1(x, y):
            f = interp1d(x, y, kind=kind, **kwargs)
            new_x = np.linspace(x[0], x[-1], num)
            new_y = f(new_x)
            return (new_x, new_y)

        outer_dct = {}
        for cell_line in list(set(data.index.get_level_values(0))):
            df = data.loc[cell_line]
            middle_dct = {}
            for antibody in list(set(df.columns.get_level_values(0))):
                df2 = df[antibody]
                inner_dct = {}
                for repeat in df2.columns:
                    df3 = df2[[repeat]]
                    x = list(df3.index)
                    y = df3.values
                    # flatten
                    y = [item for sublist in y for item in sublist]
                    newx, newy = interpolate1(x, y)
                    new_df = pandas.DataFrame(newx, newy)
                    new_df.index.name = 'time'
                    new_df.columns = [repeat]
                    inner_dct[repeat] = newy
                df2_new = pandas.DataFrame(inner_dct, index=newx)
                df2_new.index.name = 'time'
                middle_dct[antibody] = df2_new
            outer_dct[cell_line] = pandas.concat(middle_dct, axis=1)
        df = pandas.concat(outer_dct)
        df.index.names = ['cell_line', 'time']
        return df

    def plot(self, data=None, plot_selection={}, subplot_titles={},
             ncols=3, wspace=0.25, hspace=0.3, **kwargs):

        if plot_selection == {}:
            plot_selection = {
                'IRS1': ['IRS1', 'IRS1pS636_639'],
                'Akt': ['Akt', 'AktpT308', 'AktpS473'],
                'TSC2': ['TSC2', 'TSC2pT1462'],
                'S6K': ['S6K', 'S6KpT229', 'S6KpT389'],
                '4EBP': ['FourEBP1', 'FourEBP1pT37_46'],
                'Pras40': ['PRAS40', 'PRAS40pT246', 'PRAS40pS183'],
                'p38': ['p38', 'p38_pT180_Y182'],
                'Erk': ['ERK', 'ERKpT202_Y204'],
            }
        _nplots = len(plot_selection)
        if _nplots == 1:
            ncols = 1
        nrows = int(_nplots / ncols)
        _remainder = _nplots % ncols
        if _remainder > 0:
            nrows += 1

        if data is None:
            data = self.normalised_to_coomassie_blue()
        data = data.stack()
        data.index.names = ['cell_line', 'time', 'repeat']

        avg = data.groupby(['cell_line', 'time']).mean()
        sem = data.groupby(['cell_line', 'time']).sem()
        line_styles = {'MCF7': '-', 'ZR75': '--', 'T47D': '-.'}

        import matplotlib.lines as mlines
        import matplotlib.patches as mpatch
        seaborn.set_context(context='talk')
        fig = plt.figure(figsize=(12, 12))
        for i, (title, antibodies) in enumerate(plot_selection.items()):
            ax = plt.subplot(nrows, ncols, i + 1)
            # print(i, title, antibodies)
            cell_lines = []
            for cell_line in list(set(avg.index.get_level_values(0))):
                # colours = iter(seaborn.color_palette("hls", len(antibodies)))
                colours = iter(['red', 'green', 'blue', 'black', 'purple', 'yellow'])
                legend_markers = []
                for ab in antibodies:
                    c = next(colours)
                    plot_data = avg.loc[cell_line]
                    plt.errorbar(
                        list(plot_data.index),
                        plot_data[ab], yerr=sem.loc[(cell_line), (ab)],
                        marker='.', ls=line_styles[cell_line],
                        capsize=2, color=c
                    )
                    legend_markers.append(
                        mpatch.Patch(color=c, label=ab)
                    )
                plt.title(title)
                legend1 = plt.legend(handles=legend_markers, loc='best', fontsize=10)
                seaborn.despine(ax=ax, top=True, right=True)
                plt.gca().add_artist(legend1)
                cell_lines.append(cell_line)
        fig.legend(bbox_to_anchor=(0.85, 0.2), handles=[
            mlines.Line2D([], [], color='black', linestyle=line_styles[i],
                          label=i) for i in cell_lines
        ], title='Cell Line')
        plt.show()
        # plt.gca().annotate('Time (min)', xy=(0.1, 0.5), xytext=(0.1, 0.5), xycoords='figure fraction')
        # plt.suptitle('Insulin Stimulation: {}'.format(cell_line))
        fname = os.path.join(DATA_DIRECTORY,
                             'experimental_data_ZR75.png' if 'ZR75' in cell_lines else 'experimental_data_T47D.png')
        fig.savefig(fname, dpi=300, bbox_inches='tight')

    def to_copasi_format(self, prefix='not_interpolated', interpolation_num=None):
        total_proteins = ['IRS1', 'Akt', 'TSC2', 'S6K', 'FourEBP1',
                          'PRAS40', 'p38', 'ERK']
        data = self.normalised_to_coomassie_blue()
        if interpolation_num is not None:
            data = self.interpolate(data, num=interpolation_num)
        data = data.stack()
        avg = data.groupby(['cell_line', 'time']).mean()
        df_dct = {}
        for label, df in avg.groupby(level=['cell_line']):
            ics = df.iloc[[0]]
            ics = pandas.concat([ics] * df.shape[0], axis=0)
            ics.index = df.index
            ics = ics.drop(total_proteins, axis=1)
            ics.columns = [f'{i}_indep' for i in ics.columns]
            ics['Insulin_indep'] = 1
            ics['AA_indep'] = 1

            df2 = pandas.concat([df, ics], axis=1)
            df2 = df2.loc[label]

            df2 = df2.dropna(how='all', axis=1)
            fname = os.path.join(
                T47D_COPASI_FORMATED_DATA if self.cell_line == 'T47D' else ZR75_COPASI_FORMATED_DATA,
                f'{prefix}_{label}.csv'
            )
            df2 = df2.drop(total_proteins, axis=1)
            df2.to_csv(fname)
            df_dct[label] = df2
        return df_dct

    def get_initial_conc_params(self):
        """
        Return dict of initial concentration parameters. (i.e. indep vars)
        Returns:

        """
        df_dct = self.to_copasi_format()
        ic_dct = {}
        for k, df in df_dct.items():
            cols = [i for i in df if 'indep' in i]
            ic_dct[k] = df[cols].iloc[0].to_dict()
        for cell_line, dct in ic_dct.items():
            ic_dct[cell_line] = {k.replace('_indep', ''): v for k, v in dct.items() if '_indep' in k}
        return ic_dct
