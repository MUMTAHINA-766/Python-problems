#Reading a text file , consisting of some number . convert the number to a list, check to see if the list is palindromic or not
#if it is then append 'Yes' to the list . if not then rewrite the list with '0' equal to this length. close the file
# 123321 - same if read from front or back.


file = open('D:\Soft\Documents\Django projects\Python basics\example.txt','w')
file.write('123456789987654321')
file.close()


f = open('D:\Soft\Documents\Django projects\Python basics\example.txt','r')
some_list = list(f.read())
f.close

is_palendromic = True

for i in range(int(len(some_list)/2)):
    if some_list[i] != some_list[len(some_list)-i-1]:
        is_palendromic = False

if is_palendromic:
    f = open('D:\Soft\Documents\Django projects\Python basics\example.txt','a')
    f.write(' -Yes, This is Palendromic')
    f.close()

else:
    f = open('D:\Soft\Documents\Django projects\Python basics\example.txt','w')
    for i in range(len(some_list)):
        f.write('0')