# mini project
# goal: create a reusable function, when given a name--using the letters position in the american alphabet,
# calulate the value of the name
# potentially include a functionality to keep track and rank the names
import numpy as np

# dictionary for associating letters with number values
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

# to allow for looping through multiple name entries
count = 0

# initialize counter
name_total = 0

# name rank system
name_hist = {}
question = input('Would you like to enter a name? ').lower()
while count == 0:
    if question == 'yes':
            name = input('Please type a name: ').lower()
            name_hist[name] = 0
            # loop through letters in name
            for i in name:
                if i in alphabet.keys():
                    name_total += alphabet[i]
                elif i == ' ':
                    continue
                else:
                    print("please use only letters")
            print(f'The total for your name is: {name_total}')
            name2 = input('Would you like to enter another name? ').lower()
            name_hist[name] = name_total
            if name2 == 'yes':
                name_total = 0
                continue
            else:
                question = ' '
                exit
    else:
        print('Have a nice day')
        count = 1
rankings = np.sort(list(name_hist.values()))[::-1]
print(rankings)
