import numpy as np #imported numpy library
import pandas as pd #imported pandas library

#exercise 1
print(np.__version__) # printed version

#exercise 2
array_1d = np.array([0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]) # created array with numbers from 0 to 9
print(array_1d)

#exercise 3 
data = pd.read_csv('iris.data.txt', sep = ',', header=None) # imported dataset / I added "header = None", because from data set we were given I think first row should not be treated as a header
print(data)

#ecercise 4
myrow = data[data[3] > 1.0].head(1) # prints the first row where value on the 4th column is > 1 / since the columns start their count from 0, I assumed that the 4th column is the 3rd.
print(myrow)

#exersice 5
np.random.seed(100)
a = np.random.uniform(1,50, 20)
for i in range(len(a)):
    if a[i] > 30:
        a[i] = 30
    elif a[i] < 10:
        a[i] = 10
print(a)
