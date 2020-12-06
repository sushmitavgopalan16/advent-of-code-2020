with open('day5.txt') as f:
    l = f.read().split('\n')

def get_seat_number(string, low, high):
    for char in string:
        if char in ['F','L']:
            high = (high - low)/2 + low
        if char in ['B','R']:
            low = high - (high - low)/2
    return min(low, high)

# question one
results = []

for id in l:
    row = id[:7]
    col = id[-3:]
    results.append(get_seat_number(row,0,128) * 8 + get_seat_number(col,0,8))

print(max(results))

# question two
for i in range(len(results)):
    if sorted(results)[i+1] - sorted(results)[i] != 1:
        print(sorted(results)[i])
        break
