''' create a banking app that prompts the user to:
1. check balance
2. deposit money
3. withdraw money
4. exit
'''
'''Part II
Improvements upon the banking app:
make a frontend interface that looks better
maybe using flask
'''
import flask

def checkbalance(balance):
    print('*****************************************')
    print(f'Your balance is: ${balance:.2f}')
    print('*****************************************')
    return balance


def deposit(balance):
    print('*****************************************')
    depo = int(input('Please enter the amount you want to deposit: '))
    balance += depo
    print('*****************************************')
    print(f'Your new balance is ${balance:.2f}')
    print('*****************************************')
    return balance


def withdraw(balance):
    print('*****************************************')
    while True:
        withdraw = int(input('Please enter the amout you want to withdraw: '))
        if withdraw > balance:
            print('You cannot withdraw more than your balance')
            continue
        elif withdraw <= balance:
            balance -= withdraw
            print('*****************************************')
            print(f'You withdrew ${withdraw:.2f}. Your new balance is: ${balance:.2f}')
            print('*****************************************')
            return balance
        else:
            print('Please enter a valid number')


balance = 0
print('Welcome to your personal banking app')
while True:
    start = int(input('please select an action from the list:\n'
'''1. check balance
2. deposit money
3. withdraw money
4. exit \n'''))
    
    if start == 1:
        balance = checkbalance(balance)
    elif start == 2:
        balance = deposit(balance)
    elif start == 3:
        balance = withdraw(balance)
    if start == 4:
        break
    else:
        continue

print('Thank you! Have a great day.')

