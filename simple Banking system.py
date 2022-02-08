# A simple banking system
# Create a dictionary of users with their balence
#Create options to modify the database:
#1.view the balance
#2.view all the info
#3.Update balance
#if the user doesn't exist , keep an option to add the user to the system or exit 

bank_users = {'Omy' : 5000, 'Saidu' : 7000, 'Suhi' : 10000}

print('*****Welcome to the banking system******')
while True:
    print('What do you like to do?')
    print(' '+'1. View balance')
    print(' '+'2. View all the bank info')
    print(' '+'3. Update balance')
    print(' '+'4. Exit')

    desc = input()
    if desc == '1':
        print('Enter your name,please: ')
        k = input()
        if k in bank_users.keys():
            print('Your balance is '+str(bank_users[k]))
        else:
          print('The user can not be found.Would you like to add the user to the account?')
          print('click yes or no')
          desc = input()
          if desc == 'yes':
              k = input('Enter your name please: ')
              v = input('Enter your balance please: ')
              bank_users.update({k: v})
          else:
              print('Would you like to exit?')
              print('click yes or no')
              desc = input()
              if desc == 'yes':
                  break
            
    elif desc == '2':

        for k,v in bank_users.items():
            print('Username: '+str(k)+' Bank Balance: '+str(v))

    elif desc == '3':
        print('Please enter your name: ')
        k = input()
        if k in bank_users.keys():
            print('Do you want to "add" or "subtract" from your savings?')
            desc = input()
            if desc == 'add':
                temp_balance = bank_users[k]
                extra = input('Enter the amount you want to add: ')
                bank_users[k] = temp_balance + int(extra)
                print('Your balance updated. It is: ')
                print(bank_users[k])
            elif desc == 'subtract':
                 temp_balance = bank_users[k]
                 extra = input('Enter the amount you want to subtract: ')
                 bank_users[k] = temp_balance - int(extra)
                 print('Your balance updated. It is: ')
                 print(bank_users[k])

 
        else:
            print('There is no such account in the bank database. ')

    elif desc == '4':
         break


