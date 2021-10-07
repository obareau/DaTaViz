# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:42:55 2021

@author: obareau
"""
import matplotlib.pyplot as plt
import pickle

with open('iris.pickle', 'rb') as f:
    iris = pickle.load(f)

print(iris)
# Extract the first column from the data table (get all of the rows)
sepal_length = iris['data'][:,0] # Numpy Wizardy
sepal_width  = iris['data'][:,1]
classes = iris['target']

plt.scatter(sepal_length, sepal_width, c=classes)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.title('Iris data: sepal length v. width')
plt.show()

