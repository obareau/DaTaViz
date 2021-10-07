# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pickle

# load our data (rb means read binary data)
with open ('fruit-sales.pickle', 'rb') as f:
    data = pickle.load(f)
    
# Splitting a list of tuples into two lists
fruit, num_sold = zip(*data)

bar_coords = range(len(fruit))

plt.bar(bar_coords, num_sold)
# Replace the x coords with the fruit names
plt.xticks(bar_coords, fruit)
plt.ylabel('Numder of fruit (millions)')
plt.title('Number of fruit sold (2017)')
plt.show()
