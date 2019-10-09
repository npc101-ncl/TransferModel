import unittest

from .data_analysis import GetData
from transfer_model import REPLACEMENT_NAMES
class ExperimentalDataProcessingTests(unittest.TestCase):

    def test_sheet_names(self):
        gd = GetData()
        expected = ['MCF-7 vs ZR-75-1', 'MCF-7 vs T47D', 'Normalized to Maximum for MCF-7']
        actual = gd.get_sheet_names()
        self.assertEqual(expected, actual)

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

    def test_get_raw_data_top_left_zr75(self):
        gd = GetData()
        data = gd.get_raw_data()
        expected = 249053803
        # print(data['Akt'])
        actual = data.loc[('MCF7', 0), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_bottom_left_zr75(self):
        gd = GetData()
        data = gd.get_raw_data()
        expected = 230554096
        print(data)
        actual = data.loc[('ZR75', 120), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_top_right_zr75(self):
        gd = GetData()
        data = gd.get_raw_data()
        expected = 128217
        actual = data.loc[('MCF7', 0), ('ER_alpha', 3)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_bottom_right_zr75(self):
        gd = GetData()
        data = gd.get_raw_data()
        expected = 17577
        actual = data.loc[('ZR75', 120), ('ER_alpha', 3)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_top_left_t47d(self):
        gd = GetData()
        data = gd.get_raw_data('T47D')
        expected = 2599775
        actual = data.loc[('MCF7', 0), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_bottom_left_t47d(self):
        gd = GetData()
        data = gd.get_raw_data('T47D')
        expected = 1503056
        actual = data.loc[('T47D', 120), ('Akt', 0)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_top_right_t47d(self):
        gd = GetData()
        data = gd.get_raw_data('T47D')
        expected = 76100
        actual = data.loc[('MCF7', 0), ('ER_alpha', 3)]
        self.assertEqual(expected, actual)

    def test_get_raw_data_bottom_right_t47d(self):
        gd = GetData()
        data = gd.get_raw_data('T47D')
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
        gd = GetData()
        gd.plot()

    def test_plot2(self):
        gd = GetData('T47D')
        gd.plot()

    def test_to_copasi_format(self):
        gd = GetData('T47D')
        gd.to_copasi_format()








if __name__ == '__main__':
    unittest.main()
