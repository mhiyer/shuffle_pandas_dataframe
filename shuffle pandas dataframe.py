# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:21:14 2019

@author: mh iyer

Randomly shuffle a pandas dataframe

    Input: pandas dataframe
    Output: Shuffled pandas dataframe
"""

 

import pandas as pd
import random

# function to shuffle pandas dataframe
def shuffle_data(dataset):
    # create extra column which is basically the index shuffled
    dataset['shuffled_index'] = random.sample(range(0,len(dataset)), len(dataset))
    
    # sort this
    dataset = dataset.sort_values(by=['shuffled_index'])
    
    # set the new column (now sorted)
    dataset = dataset.set_index(['shuffled_index'])
    
    return dataset

# usage of this function in practice
if __name__ == "__main__":
    
    # open csv
    data = pd.read_csv(r'iris.csv')
    
    # shuffle data
    shuffled_data = shuffle_data(data)