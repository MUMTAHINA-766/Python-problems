def find_odds(list):
    new_list = []

    for i in range(len(list)):
        if list[i] % 2 != 0:
            new_list.append(list[i])

    return new_list
    
a = [2,4,65,6,8,3,15,11,77]
print(find_odds(a))
    
