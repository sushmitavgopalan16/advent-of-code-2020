# option 1
###############################################
import numpy as np
l = list(np.recfromtxt('day1.txt'))

# question 1
for i in l:
    for j in l:
        if i + j == 2020:
            print(i*j)

# question 2
for i in l:
    for j in l:
        for k in l:
            if i + j + k == 2020:
                print(i*j*k)

# option 2
###############################################

import itertools

# question 1
for i in itertools.combinations(l,2):
    if i[0] + i[1] == 2020:
        print(i[0]*i[1])

# question 2
for i in itertools.combinations(l,3):
    if sum(list(i)) == 2020:
        print(i[0]*i[1]*i[2])
