''' create a banking app that prompts the user to:
1. check balance
2. deposit money
3. withdraw money
4. exit
'''

def checkbalance(balance):
    print('*****************************************')
    print(f'Your balance is: ${balance:.2f}')
    print('*****************************************')

def deposit(balance):
    print('*****************************************')
    depo = int(input('Please enter the amount you want to deposit: '))
    balance += depo
    print('*****************************************')
    print(f'Your new balance is ${balance:.2f}')
    print('*****************************************')

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
            break
        else:
            print('Please enter a valid number')

deposit(balance)
withdraw(balance)