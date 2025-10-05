# new py file to practice script writing
# this script will use dictionaries to convert letters in a word into there alphanumeric word
# potential use cases: police can scan a license plate and instead of needing to read it out and potentially have an error,
# the computer will translate it. 
# however, upon typing this I realized if a cop can get a picture of the liscence plate, then they dont need the alphanumeric code 

alphanumberic = { 'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
                 'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
                 'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                   'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'xray', 'y': 'yankee', 'z': 'zulu'}

word = input('Please enter word and I will translate to alphanumeric code: ')

# for i in word:
#     if i == alphanumberic.keys()
#     print(alphanumberic[i])

print(alphanumberic.keys())