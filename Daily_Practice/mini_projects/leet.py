s = 'MCMVLII'
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,  'C': 100, 'D': 500, 'M': 1000}
numeral = 0
for i, current_value in enumerate(s):
    if i < len(s) - 1:
        next_value = s[i+1]
        if roman[current_value] < roman[next_value]: 
            numeral -= roman[current_value]
        else:
            numeral += roman[current_value]
    else:
            numeral += roman[current_value]


# for i in current:
#     if roman[i] < roman[current[i] + 1]:
#         numeral-=roman[i]
#     else:
#         numeral += roman[i]



        # number = 0
        # for i in numeral:
        #     number += numeral[i]
        # return number