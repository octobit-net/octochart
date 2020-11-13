# Import packages
import os 
import configparser
import pickle

# Load config
parser = configparser.ConfigParser()
if 'config.ini' in os.listdir():
    parser.read('config.ini')
else:
    parser.read('../config.ini')

# Create path for project use
DATA_PATH = parser['path']['data']
RAW_PATH = DATA_PATH + 'raw/'
PICKLE_PATH = DATA_PATH + 'pickle/'

### Serialization of the Map with Pickle (saved in data/pickle/) ###
# load the preprocessed map 
def load_pickle(file_name):
    file_path = PICKLE_PATH + file_name
    with open(file_path, 'rb') as pfile:
        my_pickle = pickle.load(pfile)
    return my_pickle

# save the Map in create_dataset.py
def save_pickle(object_, file_name):
    file_path = PICKLE_PATH + file_name
    with open(file_path, 'wb') as pfile:
        pickle.dump(object_, pfile, protocol=2)