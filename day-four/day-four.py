# i need to get over  my aversion to regex

with open('day4.txt') as f:
    l = f.read()
l = l.split('\n\n')
l = [k.replace('\n',' ') for k in l]

# question one

def check(pwd):
    master_keys = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'])
    min_keys = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
    fields = pwd.split(' ')
    keys = [k.split(':')[0].strip() for k in fields]
    if '' in keys:
        print('weird')
    if len(keys) == 8:
        if set(keys) == master_keys:
            return True
    if len(keys) == 7:
        if set(keys) == min_keys:
            return True
    return False

total = 0
for pwd in l:
    #print(pwd)
    result = check(pwd)
    #print(result)
    if result:
        total += 1
print(total + 1)

# question two - this is terribly verbose and inefficient
hex_allowed = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def check_height(h):
    if not 'cm' in h and not 'in' in h:
        return False
    if 'cm'  in h:
        if int(h[:-2]) < 150 or int(h[:-2]) > 193:
            return False

    if 'in' in h:
        if int(h[:-2]) < 59 or int(h[:-2]) > 76:
            return False
    return True

def check_hex(s):
    if len(s) != 7 or s[0]!= '#':
        return False
    if not all(c in hex_allowed for c in s[1:]):
        return False
    return True

def check_further(pwd):
    if check(pwd):
        fields = pwd.split(' ')
        keys = [k.split(':')[0].strip() for k in fields]
        dic = {}
        for thing in fields:
            k,v = thing.split(':')
            dic[k] = v

        if 1920 <= int(dic['byr']) <= 2002 and \
            2010 <= int(dic['iyr']) <= 2020 and \
            2020 <= int(dic['eyr']) <= 2030 and \
            check_height(dic['hgt']) and \
            check_hex(dic['hcl']) and \
            dic['ecl']  in ['amb', 'blu','brn','gry','grn','hzl','oth'] and \
            dic['pid'].isnumeric() and len(dic['pid']) == 9:
                return True
        else:
            return False

total = 0
for pwd in l:
    if check_further(pwd):
        total+= 1
print(total + 1)
