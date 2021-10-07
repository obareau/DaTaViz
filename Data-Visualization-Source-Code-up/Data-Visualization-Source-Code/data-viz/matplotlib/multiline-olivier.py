# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:48:02 2021

@author: obareau
"""
import matplotlib.pyplot as plt
import pickle

# Load data thanks to StackOverflow 
with open ('prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)
    
print(data)

# Split into 2 lists
languages , rankings = zip(*data)

# Iterate over all the language and call "plot" on their data

for i in range (len(languages)):
    # for each languages, split their data into years and ranking lists
    years, ranks = zip(*rankings[i])
    plt.plot(years, ranks)
 
plt.title('Rankings of Programming Languages')
plt.xlabel("Years")
plt.ylabel("Ranking")
plt.legend(languages)
plt.show()