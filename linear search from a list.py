#linear search in a list . search for number 

from logging.config import valid_ident


def linear_search(list,search_value):
    for i in range(len(list)):
        if list[i] == search_value:
            return 'Found'
    if i == len(list)-1:
        return 'Not found'

a = [1,2,3,4,5,6]
print(linear_search(a, 40))
print(linear_search(a, 4))
