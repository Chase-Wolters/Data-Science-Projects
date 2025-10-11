# new python project - guess the number game
import random as rand

start = input('''Welcome to the Guessing Game!
Which game mode would you like to play?
GAME 1: The computer chooses a number and you will guess
or
GAME 2: You choose a number and the computer will guess
                 
RULES:
1. You or the computer will only have 3 guesses
2. Each number must be between 1 & 100
3. You must answer if the guessed number is too high or too low

Please make a game mode selection: ''').lower()

attempts = {'1': 'First', '2': 'Second', '3': 'Third'}
tries = list(attempts)
secret_num = rand.randint(1,100)

if start == 'game 1':
    for i in attempts:
        # inserting the values from attempts for each iteration
        guess = int(input(f"Please enter your {attempts[i]} guess: "))
        if guess == secret_num:
            print(f'Congratulations!!! You found the secret number: {secret_num}')
            break
        if guess != secret_num and i != tries[-1]:
            print('Sorry not the secret number')
            if guess > secret_num:
                print('Your guess was too high')
            else:
                print('Your guess was too low')
        else:
            print(f'Sorry, you did not find the secret number: {secret_num}')
else:
    print('''Get your secret number ready and remember the rules:
RULES:
1. You or the computer will only have 3 guesses
2. Each number must be between 1 & 100
3. You must answer if the guessed number is too high or too low''')
    print(input('Press enter when ready to star: '))

    comp_guess = rand.randint(1,100)
    for i in attempts:
        print(f'My {attempts[i]} guess is: {comp_guess}')
        response = input('Is my guess too high (h), too low (l), or correct(c)? ').lower()
        if response == 'h' and i != tries[-1]:
            print('My guess was too high')
            comp_guess = rand.randint(1,comp_guess - 1)
        elif response == 'l' and i != tries[-1]:
            print('My guess was too low')
            comp_guess = rand.randint(comp_guess + 1, 100)
        elif response == 'c':
            print('Yay I guessed the secret number!')
            break
        else: 
            print('Oh no, I did not find the secret number')
