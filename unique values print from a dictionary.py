#write a program to print the unique values of a dictionary. you must use to dictionary
#1,2,3,4,4>>>1,2,3

from itertools import count


a = {1: 1,2: 4,3: 5,4: 1,5: 9,6: 4}
b = {}

count = {}
for i in a.values():
    count.setdefault(i, 0)
    count[i] = count[i]+1
print(count)

i = 0
for k, v in count.items():
    if v == 1:
        b.update({i: k})
        i = i + 1
print('unique values: ',end=" ")
for i in b.values():
    print(i,end=" ")