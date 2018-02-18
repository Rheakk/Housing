'''
    $Id$
    Author Rhea
    Created 1/Feb/2018
'''
import numpy as np
from FetchData import load_housing_data

def split_train_test (data, test_ratio):
    shuffled_indices = np.random.permutation (len(data))
    test_set_size = int (len(data) * test_ratio)
    test_indices = shuffled_indices [:test_set_size]
    train_indices = shuffled_indices [test_set_size:]
    return data.iloc [train_indices], data.iloc [test_indices]

def train_test_split (data):
    from sklearn import model_selection as skm
    
    return skm.train_test_split (data, test_size=0.2, random_state=42)

if __name__ == "__main__":
    housing = load_housing_data ()
    train_set, test_set = split_train_test (housing, 0.2)
    print (len (train_set), "train + ", len(test_set), "test")
    train_set, test_set = train_test_split (housing)
    print (len (train_set), "train + ", len(test_set), "test")
    
    

    