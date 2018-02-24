'''
    $Id$
    Author Rhea
    Created 1/Feb/2018
'''
import os
import logging
import tarfile
from six.moves import urllib  # @UnresolvedImport
import pandas as pd

DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml/raw/master"
HOUSING_PATH = "datasets/housing"

HOUSING_FILE_NAME = "housing"
HOUSING_TGZ = "%s.tgz" % HOUSING_FILE_NAME
HOUSING_CSV = "%s.csv" % HOUSING_FILE_NAME

HOUSING_URL = "%s/%s/%s" % (DOWNLOAD_ROOT, HOUSING_PATH, HOUSING_TGZ)

OUT_DIR = os.environ.get ("DATA_DIR", "")
if not OUT_DIR:
    logging.error ("'DATA_DIR' must be set before fetching data")
    exit(1)

def makeDir (dir_name):
    ''' will create a dir if dir_name does not exist
        returns Boolean
            True - if it actually creates the directory
            False - if the dir already exists
    '''
    if not os.path.isdir (dir_name):
        os.makedirs (dir_name)
        logging.info ("created missing dir - %s", dir_name)
        return True

    logging.debug ("dir alrady exists - %s", dir_name)
    return False

def archive_files (out_dir, *argv):
    ''' will create a directory by the name out_dir/'archive'
        and move all files passed as subsequent arguments into that
        directory
        return 
            True - if all files were successfully archived.
            False - on the first failure of archiving
    '''
    archive_dir = os.path.join (out_dir, "archive")

    # check to make sure to create dir if not present
    makeDir (archive_dir)
    
    for file in argv:
        # get the file name from the file
        file_name = os.path.basename (file)
        new_path = os.path.join (archive_dir, file_name)
        logging.debug ("Moving %s to %s", file, new_path)
        if os.rename (file, new_path):
            logging.error ("Could not rename %s to %s", file, new_path)
            return False
        logging.info ("Renamed %s to %s", file, new_path)
    return True

def fetch_housing_data (housing_file=HOUSING_TGZ, housing_url=HOUSING_URL, out_dir=OUT_DIR):
    ''' fetch housing data and take optionally
            housing_file - file that needs to be downlaoded (defaul will use HOUSING_TGZ)
            houing_url - url to download from (defaul will use HOUSING_URL)
            out_dir - dir where the downloaded file needs to be saved in (default: OUT_DIR)
        returns Boolean value
            True - when downloads the file successfully
            False - if it fails to download (and also logs an error)
    '''
    makeDir (out_dir)

    tgz_path = os.path.join (out_dir, housing_file)
    out_file_name = os.path.join(out_dir, HOUSING_CSV)

    # first moe all the old files out  so that we can make sure that the new download
    # gives us new files
    if not archive_files (out_dir, tgz_path, out_file_name):
        logging.error("Could not archive files - %s, %s", tgz_path, out_file_name)
        return None 
    
    logging.debug ("Cleared downloaded files - %s, %s", tgz_path, out_file_name)
    # now all downloaded files are cleared

    logging.info ("downloading using %s", housing_url)
    urllib.request.urlretrieve (housing_url, tgz_path)
    if not tarfile.is_tarfile (tgz_path):
        logging.error ("could not download valid tar file - %s", tgz_path)
        return None
        
    logging.info ("downloaded %s", tgz_path)
    
    logging.info ("Uncompressing - %s", tgz_path)
    housing_tgz = tarfile.open (tgz_path)
    housing_tgz.extractall (path=out_dir)
    housing_tgz.close()
    logging.info ("Uncompressed in - %s", out_dir)
    
    if not os.path.isfile (out_file_name):
        logging.error ("File downloaded and uncompressed but missing - %s", out_file_name)
        return None

    return out_file_name

def load_housing_data (housing_file=HOUSING_CSV, in_dir=OUT_DIR):
    csv_path = os.path.join (in_dir, housing_file)
    logging.info ("loading in pandas - %s", csv_path)
    pd.set_option('display.width', 1000)
    return pd.read_csv (csv_path)
    
if __name__ == "__main__":

    logging.getLogger().setLevel (logging.DEBUG)
    fetch_housing_data ()
    housing = load_housing_data ()
    print (housing.head ())
    housing.info ()
    print (housing["ocean_proximity"].value_counts())
    print (housing.describe())
    
    logging.info ("Showing housing as histogram.. will show a separate window")

    import matplotlib.pyplot as plt
    housing.hist (bins=50, figsize=(20,15))
    plt.show()