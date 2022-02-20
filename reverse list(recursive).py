#reverse a list using recursion

# reverse in normal way-1
from hashlib import new


data = ["a","b","c","d","e","f","g","h"]
#index = 1
#print(data[index], data[-index-1])
for index in range(len(data)//2):
    data[index], data[-index-1] = data[-index-1], data[index]
print(data)

# reverse in normal way-2
user = [1,2,3,4,5,6]
user.reverse()
print(user)

# reverse in normal way-3
def reverse_list(A):
    new_list = []

    for i in range(0, len(A)):
        new_list.append(0)

    for i in range(len(A)-1, -1, -1):
        new_list[len(A)-1-i] = A[i]

    return new_list

lists = ['one','two','three','four']
print(reverse_list(lists))

#reverse a list way - 4

def reverse_list(A):
    new_list = []

    for i in range(0, len(A)):
        new_list.append(0)
    for i in range(len(A)-1, -1, -1):
        new_list[len(A)-1-i] = A[i]
    return new_list
lists = [1,2,3,4]
print(reverse_list(lists))

#reverse a list way - 5

def reverse_list_recursive(some_list):
    if len(some_list) == 0:
        return []

    return [some_list[-1]]+reverse_list_recursive(some_list[:-1])

#some_list = [1,2,3,4]
print(reverse_list_recursive(lists))