# This program simulates a phone-book

from ast import Num
from unicodedata import name


contact_no = {'Omy': 84203983,'Suhi': 7573802,'Tom': 8734802}
x = 0

while x<5:
    print("Enter the name to find contact(press ENTER to exit): ")
    name = input()

    if name == "":
        break
    if name in contact_no:
        print('The contact number of '+name +" is "+str(contact_no[name]))
    else:
        print("There is no such name in the phone-book. Do you want to add it?")
        desc = input()

        if desc == 'yes':
            print("Enter the number: ")
            num = input()
            contact_no[name] = num
            print("Number added")
        elif desc == 'no':
            print('Do you want to quit?')
            desc = input()
            if desc == 'yes':
                break
            else:
                print('Keep searching')
        x = x+1
        