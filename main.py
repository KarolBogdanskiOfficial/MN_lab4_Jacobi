from LoadData import *
import numpy as np

data = load_data("data.txt")

#sczytaj pierwszą liczbę
n = int(data[0][0])
#sczytaj ostanią liczbę 
iterations = int(data[-1][0])

#tworzymy tablicę
matrix = np.zeros((n, n))

for i in range (1, n+1):
    for j in range (n):
        matrix[i - 1, j] = float(data[i][j])
