# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:00:58 2021

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

print(languages)
print(rankings)
# Get the Java years and  (split java datas into 2 lists)
java_years, java_ranks = zip(*rankings[0])

plt.plot(java_years, java_ranks)
plt.xticks(java_years)
# x-axis : year, y-axis : ranking, title : Java ranking
plt.xlabel('years')
plt.ylabel('Ranking')
plt.title('Java Ranking')
plt.show()


