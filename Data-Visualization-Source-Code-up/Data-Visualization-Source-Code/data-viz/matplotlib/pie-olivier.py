# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:29:37 2021

@author: obareau
"""
import matplotlib.pyplot as plt
import pickle

# Load data thanks to StackOverflow 
with open ('devs-outside-time.pickle', 'rb') as f:
    data = pickle.load(f)
    
# Print(data)

# Split into two listes

time, responses = zip(*data)

plt.pie(responses, labels=time, autopct='%.2d%%') # Default Python format specifier %2d%% or for a flot %2f%%
# force the x/y to have the same scale
# circle instead of an oval
plt.axis('equal')
plt.title('Daily Time Developer Spend Outside')
plt.show