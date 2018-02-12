import os
import logging
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml/raw/master"
HOUSING_PATH = "datasets/housing"
HOUSING_FILE = "housing.tgz"
HOUSING_URL = "%s/%s/%s" % (DOWNLOAD_ROOT, HOUSING_PATH, HOUSING_FILE)

OUT_DIR = "C:\Users\Soo\Documents\Krsp\Housing\datasets\housing"

def fetch_housing_data (housing_file=HOUSING_FILE, housing_url=HOUSING_URL, out_dir=OUT_DIR):
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
    
logging.getLogger().setLevel (logging.DEBUG)
fetch_housing_data ()