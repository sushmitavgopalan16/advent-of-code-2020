import numpy as np

with open('day9.txt') as f:
    l = f.read().split('\n')[:-1]

l = [int(k) for k in l]

# question one
def get_anomaly(t,k):
    for i in range(k,len(t)):
        prev_k = t[i-k:i]
        all_sums = set([sum(k) for k in combinations(prev_k,2) if k[0]!=k[1]])
        if t[i] not in all_sums:
            print(t[i])
            return t[i]

get_anomaly(l,25)
# 105950735

# question two

def check_total(t,i,anomaly):
    total = 0
    while total < anomaly:
        total = total + t[i]
        i += 1
    return i, total

def get_weakness(t,anomaly):
    for i in range(len(t)):
        start = i
        end, total = check_total(t,i,anomaly)
        if total == anomaly:
            print(min(t[start:end]) + max(t[start:end]))
            break

get_weakness(l,105950735)
