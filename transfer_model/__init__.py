import os

# Some important global parameters for use in sub packages
WORKING_DIRECTORY = os.path.dirname(__file__)
DATA_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'data')
ZR_75_DATA = os.path.join(DATA_DIRECTORY, 'zr75_data.xlsx')
T47D_DATA = os.path.join(DATA_DIRECTORY, 't47d_data.xlsx')
STEADY_STATE_DATA = os.path.join(DATA_DIRECTORY, 'steadystate_data.csv')

COPASI_FORMATTED_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'CopasiFormattedData')
T47D_COPASI_FORMATED_DATA = os.path.join(COPASI_FORMATTED_DATA_DIRECTORY, 'T47DSheet')
ZR75_COPASI_FORMATED_DATA = os.path.join(COPASI_FORMATTED_DATA_DIRECTORY, 'ZR75Sheet')
STEADTSTATE_COPASI_FORMATED_DATA = os.path.join(COPASI_FORMATTED_DATA_DIRECTORY, 'steadystate')
MODELS_DIRECTORY = os.path.join(WORKING_DIRECTORY, 'models')
SIMULATION_DIRECTORY = os.path.join(MODELS_DIRECTORY, 'simulation_data')
PARAMETER_ESTIMATION_CONFIG_YAML = os.path.join(MODELS_DIRECTORY, 'param_est_config.yaml')

# some important filenames that are used in subdirectories
EXPERIMENTAL_DATA_FILE = os.path.join(DATA_DIRECTORY, 'experimental_data_with_norm_to_max.xlsx')
COPASI_FILE = os.path.join(MODELS_DIRECTORY, 'simple_akt_model.cps')

# an offset parameter to ensure total proteins are not present in greater
#  amounts than their phospho counterparts
OFFSET_PARAMETER = 0


REPLACEMENT_NAMES = {
    '4E_BP1': 'FourEBP1',
    '4E_BP1pT37_46': 'FourEBP1pT37_46',
    'Akt': 'Akt',
    'AktpS473': 'AktpS473',
    'AktpT308': 'AktpT308',
    'Coomassie_staining': 'Coomassie_staining',
    'Coomassie_blue': 'Coomassie_blue',
    'ER_alpha': 'ER_alpha',
    'ERK': 'ERK',
    'ERK_pT202_Y204': 'ERKpT202_Y204',
    'GAPDH': 'GAPDH',
    'IRS1': 'IRS1',
    'IRS1pS636_639': 'IRS1pS636_639',
    'PRAS40': 'PRAS40',
    'PRAS40pS183': 'PRAS40pS183',
    'PRAS40pT246': 'PRAS40pT246',
    'S6K': 'S6K',
    'S6KpT229': 'S6KpT229',
    'S6KpT389': 'S6KpT389',
    'TSC2': 'TSC2',
    'TSC2pT1462': 'TSC2pT1462',
    'p38': 'p38',
    'p38_pT180_Y182': 'p38_pT180_Y182'
}

# todo consider dividing z75 by mcf7 and t47d by mcf7 and only using these two
#  i.e. express these two cell lines as amounts relative to MCF7











