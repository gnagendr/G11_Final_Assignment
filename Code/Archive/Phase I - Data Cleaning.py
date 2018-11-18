# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:07:46 2018

@author: willi
"""

import pandas as pd
import numpy as np

d = 'https://raw.github.com/gnagendr/G11_Final_Assignment/master/Data/Breast-Cancer-Wisconsin.csv'
data = pd.read_csv(d, index_col=0, sep = ',')

#Replace '?' with NaN in column A7
data['A7'] = data['A7'].astype(str)
data['A7'] = data['A7'].replace('?',np.NaN)
data['A7'] = pd.to_numeric(data['A7'])

#Check the number of NaN values
print("Number of NaN Values in column A7: ",sum(pd.isnull(data['A7'])), "\n")

#Replace NaN values in whole dataset with the mean of column A7
if data.isnull().values.any():
    data = data.fillna(data['A7'].mean(skipna=True))

#Print Summary Statistics
print("Summary Statistics:\n",data.describe(),"\n")

#Number of columns in data
print("Number of columns in data:\n",data.shape[1], "\n")

#Number of observations/rows
print("Number of observations/rows in data:\n",data.shape[0], "\n")

#Number of Unique Values
print("Number of unique id values:\n", len(data.index.get_level_values(0).unique()),"\n")


print("Variable Standard Deviation", "\n", data.std(axis = 0), "\n")

print("Variable Variation", "\n", data.var(axis = 0), "\n")

print("Boxplot of Variables:", "\n", data.boxplot())