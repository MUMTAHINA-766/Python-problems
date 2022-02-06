import copy as cp 

def centered_average(list):
    sum = 0
    count = 0
    
    temp_list = list.sort()
    sorted = list.copy()
    print(sorted)

    for i in range(1,len(list)-1):
        sum = sum + list[i]
        count = count+1

    return sum/count
a = [2,4,3,6,8,5]
print(centered_average(a))