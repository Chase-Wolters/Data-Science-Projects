# new python project - guess the number game

start = input('''Welcome to the Guessing Game!
Which game mode would you like to play?
GAME 1: You choose a number and the computer will guess
or
GAME 2: The computer chooses a number and you will guess
                 
RULES:
1. You or the computer will only have 3 guesses
2. Each number must be between 1 & 100
3. You must answer if the guessed number is too high or too low

Please make a game mode selection: ''').lower()

attempts = {'1': 'First', '2': 'Second', '3': 'Third'}
tries = list(attempts)
secret_num = 100

if start == 'game 1':
    for i in attempts:
        guess = int(input(f"Please enter your {attempts[i]} guess: "))
        if guess == secret_num:
            print(f'Congratulations!!! You found the secret number: {secret_num}')
            exit
        if guess != secret_num and i != tries[-1]:
            print('Sorry not the secret number')
        else:
            print('Sorry, you did not find the secret number')
