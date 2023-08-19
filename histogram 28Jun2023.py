#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:55:02 2023

@author: dimitardimitrov
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Read the Excel file and extract the desired column
data_frame = pd.read_excel('Book1 tau pff sizes TEM.xlsx', sheet_name='Sheet1')
first_column_data = data_frame.iloc[:, 0]
SaveAs='Book1 tau pff sizes TEM.png'
def SaveFile(): 
  plt.savefig(SaveAs, dpi=300, bbox_inches='tight')
# Create a histogram using matplotlib
sns.histplot(first_column_data, bins=100,stat='percent')  # Adjust the number of bins as per your preference
plt.xlim(0, 500)  
x_ticks = np.arange(0, 500, 50)  # Ticks from 0 to 100 with 20 interval
x_ticks = np.concatenate([x_ticks, np.arange(100, 501, 500)])  # Additional ticks from 100 to 500 with 100 interval
plt.xticks(x_ticks)
# Customize the plot
plt.xlabel('Tau pff length (nm)')
plt.ylabel('Counts (%)')
sns.despine (top=True, right=True)
# Display the histogram
plt.show()

Save = input('Save file? y/n')
if Save in ['y']:
    SaveFile()
    print ("Yay! Saved!")
else:
    print ("Not saved!")