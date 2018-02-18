'''
    $Id$
    Author Rhea
    Created 1/Feb/2018
'''
import os
import logging
import tarfile
from six.moves import urllib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml/raw/master"
HOUSING_PATH = "datasets/housing"

HOUSING_FILE_NAME = "housing"
HOUSING_TGZ = "%s.tgz" % HOUSING_FILE_NAME
HOUSING_CSV = "%s.csv" % HOUSING_FILE_NAME

HOUSING_URL = "%s/%s/%s" % (DOWNLOAD_ROOT, HOUSING_PATH, HOUSING_TGZ)

OUT_DIR = "C:\Users\Soo\Documents\Krsp\Housing\datasets\housing"

def fetch_housing_data (housing_file=HOUSING_TGZ, housing_url=HOUSING_URL, out_dir=OUT_DIR):
    if not os.path.isdir (out_dir):
        os.makedirs (out_dir)
        logging.info ("created missing out dir - %s", out_dir)
    else:
        logging.info ("for out dir will use existing - %s ", out_dir)

    tgz_path = os.path.join (out_dir, housing_file)
    logging.info ("downloading using %s", housing_url)
    urllib.request.urlretrieve (housing_url, tgz_path)
    if not tarfile.is_tarfile (tgz_path):
        logging.error ("could not download valid tar file - %s", tgz_path)
        exit (1)
        
    logging.info ("downloaded %s", tgz_path)
    logging.info ("Uncompressing - %s", tgz_path)
    housing_tgz = tarfile.open (tgz_path)
    housing_tgz.extractall (path=out_dir)
    housing_tgz.close()
    logging.info ("Uncompressed in - %s", out_dir)

def load_housing_data (housing_file=HOUSING_CSV, in_dir=OUT_DIR):
    csv_path = os.path.join (in_dir, housing_file)
    logging.info ("loading in pandas - %s", csv_path)
    return pd.read_csv (csv_path)
    
logging.getLogger().setLevel (logging.DEBUG)
#fetch_housing_data ()
housing = load_housing_data ()
print housing.head ()
housing.info ()
print housing["ocean_proximity"].value_counts()
print housing.describe()
#housing.hist (bins=50, figsize=(20,15))
#plt.show()

def split_train_test (data, test_ratio):
    shuffled_indices = np.random.permutation (len(data))
    test_set_size = int (len(data) * test_ratio)
    test_indices = shuffled_indices [:test_set_size]
    train_indices = shuffled_indices [test_set_size:]
    return data.iloc [train_indices], data.iloc [test_indices]

train_set, test_set = split_train_test (housing, 0.2)
print (len (train_set), "train + ", len(test_set), "test")

    