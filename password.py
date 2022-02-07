# This program simulates a password protected app access

from re import T
from unicodedata import name


password_bank = {'Omy':12345,'Saidu':23456,'Suhi':34567}
matched = False
x = 0

print("Enter your name: ")

while x<3:
    name = input()
    if name in password_bank:
        for i in range(1,3):
            print("Enter your password: ")
            password = int(input())
            if password in password_bank.values():
                matched = True
                print("Access Granted!")
                break
            else:
                print("Wrong password! Enter Again:"+"You have "+str(3-i)+" chances left")
    else:
        print("There is no such name in the password_bank. Try again.")
    
    x = x+1
    if matched:
        break