# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:07:46 2018

@author: willi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
print("Number of unique id values:\n", len(data.index.get_level_values(0).unique()))


#Plotting 9 histograms, one for each column
fig1, axs = plt.subplots(3,3, tight_layout = True)

axs[0,0].hist(data.loc[:,'A2'])
axs[0,1].hist(data.loc[:,'A3'])
axs[0,2].hist(data.loc[:,'A4'])
axs[1,0].hist(data.loc[:,'A5'])
axs[1,1].hist(data.loc[:,'A6'])
axs[1,2].hist(data.loc[:,'A7'])
axs[2,0].hist(data.loc[:,'A8'])
axs[2,1].hist(data.loc[:,'A9'])
axs[2,2].hist(data.loc[:,'A10'])

plt.show()

#Plotting Bar Graph for CLASS
data['CLASS'].value_counts().plot.bar(color=['blue','red'],alpha=0.5)
plt.ylabel('Count')
plt.xlabel('Tumor Class')
plt.title('Number of Benign and Malignant Tumors')
plt.xticks(np.arange(2), ('Benign', 'Malignant'),rotation=0)
plt.show()

#Plotting ScatterPlot 
data.plot(kind='scatter',x='A2',y='A10',alpha=0.3,color='green')
plt.ylabel('Mitoses')
plt.xlabel('Clump Thickness')
plt.title('Mitoses vs Clump Thickness')
plt.show()



