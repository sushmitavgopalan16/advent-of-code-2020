import numpy as np

with open('day3.txt') as f:
    l = f.read().splitlines()

def get_answer(l,row_step, col_step):
    k = [k * 3200 for k in l]

    trees = 0
    row = 0
    col = 0
    for line in k:
        row = row + row_step
        col = col + col_step
        try:
            if k[row][col] == '#':
                trees += 1
        except:
            break
    print(trees)
    return(trees)


# question 1
get_answer(l,1,3)

# question 2
get_answer(l,1,1) * get_answer(l,1,3) * get_answer(l,1,5) * get_answer(l,1,7) * get_answer(l,2,1)
