import numpy as np

with open('day6.txt') as f:
    l = f.read().split('\n\n')

l = [k.replace('\n',' ') for k in l]

# question 1
total = 0
for pw in l:
    t = [list(k) for k in pw.split()]
    n = len(set([item for sublist in t for item in sublist]))
    total += n

print(total)

# question 2

total = 0
for pw in l:
    t = [list(k) for k in pw.split()]
    collapsed = [item for sublist in t for item in sublist]

    subtotal = 0
    for k,v in dict(Counter(collapsed)).items():
        if v == len(t):
            subtotal += 1
    total += subtotal

print(total)
