with open('day2.txt') as f:
    l = f.read().splitlines()

# question  1
total = 0
for code in l:
    elements = code.split()
    lower = int(elements[0].split('-')[0])
    upper = int(elements[0].split('-')[1])
    letter = elements[1][0]
    st = elements[2]
    n_letter = st.count(letter)
    if n_letter < lower or n_letter > upper:
        total+= 1

print(1000-total)

# question 2

total = 0
for code in l:
    elements = code.split()
    first_position = int(elements[0].split('-')[0])
    second_position = int(elements[0].split('-')[1])
    letter = elements[1][0]
    st = elements[2]

    cond_one = st[first_position-1] == letter
    cond_two = st[second_position-1] == letter
    if cond_one + cond_two == 1:
        total+=1
print(total)
