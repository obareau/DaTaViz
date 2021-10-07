# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:41:55 2021

@author: obareau
"""
import matplotlib.pyplot as plt
import pickle

# Load data
with open ('coding-exp-by-dev-type.pickle', 'rb' ) as f:
    data = pickle.load(f)
    
print(data)

# Split into 2 lists
dev_types, years_exp = zip(*data)

bar_coords = range(len(dev_types))

plt.barh(bar_coords, years_exp)
plt.xlabel('years')
plt.title('Years of Coding Experience by Developer Type', fontsize=8)
plt.yticks(bar_coords, dev_types, fontsize=8)
plt.tight_layout()

plt.show

