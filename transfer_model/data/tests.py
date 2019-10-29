import os
import unittest

from .data_analysis import GetData, SteadyStateData
from transfer_model import *


class ExperimentalDataProcessingTests(unittest.TestCase):

    def test_antibody_names(self):
        gd = GetData()
        expected = ['Akt', 'AktpT308', 'AktpS473', 'PRAS40', 'PRAS40pT246', 'PRAS40pS183',
                    'S6K', 'S6KpT389', 'S6KpT229', 'TSC2', 'TSC2pT1462', 'IRS1', 'IRS1pS636/639',
                    '4E-BP1', '4E-BP1pT37/46', 'GAPDH', 'ERK', 'Coomassie staining', 'ERK-pT202/Y204',
                    'p38', 'p38-pT180/Y182', 'ER alpha']
        expected = [i.replace('-', '_') for i in expected]
        expected = [i.replace('/', '_') for i in expected]
        expected = [i.replace(' ', '_') for i in expected]
        expected = [REPLACEMENT_NAMES[i] for i in expected]
        actual = gd.get_antibody_names()
        self.assertListEqual(expected, actual)

    def test_get_raw_data_top_left_zr7(self):
        gd = GetData('ZR75')
        data = gd.get_raw_data()
        expected = 249053803
        print(sorted(list(data.columns)))
        actual = data.loc[('MCF7', 0), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_raw_has_no_empty_cells(self):
        import numpy as np
        gd = GetData('ZR75')
        data = gd.get_raw_data()
        nulls = False
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if data.iloc[i, j] in ['', np.nan]:
                    nulls = True
        self.assertFalse(nulls)

    def test_get_raw_data_bottom_left_zr75(self):
        gd = GetData('ZR75')
        data = gd.get_raw_data()
        expected = 230554096
        actual = data.loc[('ZR75', 120), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_top_right_t47d(self):
        gd = GetData('T47D')
        data = gd.get_raw_data()
        expected = 76100
        actual = data.loc[('MCF7', 0), ('ER_alpha', 3)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_bottom_right_zr75(self):
        gd = GetData()
        data = gd.get_raw_data()
        expected = 17577
        actual = data.loc[('ZR75', 120), ('ER_alpha', 3)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_top_left_t47d(self):
        gd = GetData('T47D')
        data = gd.get_raw_data()
        expected = 2599775
        actual = data.loc[('MCF7', 0), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_bottom_left_t47d(self):
        gd = GetData('T47D')
        data = gd.get_raw_data()
        expected = 1503056
        actual = data.loc[('T47D', 120), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_top_right_t47d(self):
        gd = GetData('T47D')
        data = gd.get_raw_data()
        expected = 76100
        actual = data.loc[('MCF7', 0), ('ER_alpha', 3)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_bottom_right_t47d(self):
        gd = GetData('T47D')
        data = gd.get_raw_data()
        expected = 20282
        actual = data.loc[('T47D', 120), ('ER_alpha', 3)]
        self.assertEqual(expected, actual)

    def test_mean(self):
        gd = GetData()
        mean_data = gd.normed_to_average()
        expected = 1.016194808
        actual = mean_data.loc[('MCF7', 120), ('Akt', 1)]
        self.assertAlmostEqual(expected, actual)

    def test_median(self):
        gd = GetData()
        mean_data = gd.normed_to_median()
        expected = 1.0503351898195283
        actual = mean_data.loc[('MCF7', 120), ('Akt', 1)]
        self.assertAlmostEqual(expected, actual)

    def test_coomassie(self):
        gd = GetData()
        expected = 1.207326625
        actual = gd.normalised_to_coomassie_blue().loc[('MCF7', 0), ('Akt', 0)]
        self.assertAlmostEqual(expected, actual)

    def test_offset_func(self):
        gd = GetData()
        print(gd.add_offset_to_total_proteins())

    def test_interpolate(self):
        gd = GetData()
        df = gd.interpolate()
        actual = df.shape
        expected = (24, 88)
        self.assertEqual(actual, expected)

    def test_plot1(self):
        gd = GetData('ZR75', )
        gd.plot()

    def test_plot2(self):
        gd = GetData('T47D')
        gd.plot()

    def test_plot_mcf7(self):
        import pandas as pd
        gd1 = GetData('T47D')
        gd2 = GetData('ZR75')
        data1 = gd1.normalised_to_coomassie_blue()
        data2 = gd2.normalised_to_coomassie_blue()
        df = pd.concat({
            'MCF7_T47D': data1.loc['MCF7'],
            'MCF7_ZR75': data2.loc['MCF7']
        })
        fname = os.path.join(DATA_DIRECTORY, 'MCF7_overlayed.png')
        gd1.plot(data=df, fname=fname)
        self.assertTrue(os.path.isfile(fname))


    def test_to_copasi_format(self):
        gd = GetData('T47D')
        gd.to_copasi_format()

    def test_Get_ic(self):
        gd = GetData('T47D')
        ics = gd.get_initial_conc_params()
        ic = ics['MCF7']['PRAS40pT246']
        expected = 0.3871902936254561
        actual = ic
        self.assertEqual(expected, actual)

    def test_Get_ic2(self):
        gd = GetData('ZR75')
        data = gd.normalised_to_coomassie_blue()
        data = data.stack().groupby(level=['cell_line', 'time']).mean()
        print(data.loc['ZR75', 0])
        # ics = gd.get_initial_conc_params()
        # for k, v in ics['ZR75'].items():
        #     print(k, v)

        # ic = ics['MCF7']['PRAS40pT246']
        # expected = 0.3871902936254561
        # actual = ic
        # self.assertEqual(expected, actual)

    def test_median_norm(self):
        gd = GetData('T47D')
        data = gd.get_raw_data()
        data = gd.normed_to_average(data)
        data = gd.normalised_to_coomassie_blue(data)
        data = gd.median_normalisation(data)

        gd = GetData('ZR75')
        data = gd.get_raw_data()
        data = gd.normed_to_average(data)
        data = gd.normalised_to_coomassie_blue(data)
        data = gd.median_normalisation(data)
        print(data)


class SteadyStateDataTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_read_raw_data(self):
        ss = SteadyStateData()
        expected = 2554873.0
        data = ss.read_data()
        actual = data.loc[('FourEBP1', 1), 'ZR75']
        self.assertEqual(expected, actual)

    def test_normed_to_average(self):
        ss = SteadyStateData()
        exepected = 0.9209925042031529
        data = ss.normed_to_average()
        actual = data.loc[('Akt', 0), 'ZR75']
        self.assertAlmostEqual(exepected, actual)

    def test_normed_to_coomas(self):
        ss = SteadyStateData()
        mcf70_coom = 0.979734

        exepected = 0.9209925042031529
        data = ss.normalised_to_coomassie_blue()

        # actual = data.loc[('Akt', 0), 'ZR75']
        # self.assertAlmostEqual(exepected, actual)

    def test_plot(self):
        ss = SteadyStateData()
        ss.plot()

    def test_ttests(self):
        ss = SteadyStateData()
        t, p, passed = ss.t_tests('Akt', 'MCF7', 'T47D')

        print(t, p, passed)

    def test_to_Copasi_format(self):
        ss = SteadyStateData()
        ss.to_copasi_format()





if __name__ == '__main__':
    unittest.main()
