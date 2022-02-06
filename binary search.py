#perform a binary search on a list
#first sort the list of numbers,then if the number asked to find is greater then the last element on sorted list then the number doesn't exist
# else do the follwing
#  1. check the element is equal to the middle element ,if it is then found
# 2. check it's smaller , then the number is must be in the left sublist of the middle number
# 3. if larger then the number must be in right sublist 
# do this untill the left sublist is smaller than the right one.

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item  < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 13


print(binary_search(sequence_a, item_a))