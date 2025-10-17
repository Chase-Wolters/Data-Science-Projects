# in this project I will create a hangman game where the objective is to guess the word before running out of attempts
import random
from words import words

letters = {''}
secret_word = random.choice(words)
attempt = [1,2,3,4,5,6,7]


Hangman = {1:'''  
  ---------
  |       |  
  |       
  |
  |
  |
-----------''',
2:'''  
  ---------
  |       |  
  |     (*_*)
  |
  |
  |
-----------''',
3:'''  
  ---------
  |       |  
  |     (*_*)
  |       |
  |       
  |
-----------''',
4:'''  
  ---------
  |       |  
  |     (*_*)
  |      \|
  |       |
  |
-----------''',
5:'''  
  ---------
  |       |  
  |     (*_*)
  |      \|/
  |       |
  |
-----------''',
6:'''  
  ---------
  |       |  
  |     (*_*)
  |      \|/
  |       |
  |      /
-----------''',
7:'''  
  ---------
  |       |  
  |     (*_*)
  |      \|/
  |       |
  |      / \\
-----------'''
}

print(input('''
Welcome to the hangman game!
Press ENTER to start '''))

for i in range(Hangman):
    for letter in secret_word:
      print(Hangman[i])
      if letters in secret_word:
        print(letters, end='')
      else: 
        print('-',end='')
      continue
    letters = input(f'Please enter your guess: ')


