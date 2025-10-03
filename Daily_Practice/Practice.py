# a script to practice building functions and using loops
# build an script that will take in user information and add them to a directory
# then ask a user who they want to search for 

# insert directory info
directory = []

# empty string to hold insert directory options
dir_info = ''

insert_info = 0
while insert_info == 0:
    choice = input('''Hello! Pick an action:
see full directory
Search Person
Insert new info
If done with directory, please enter 0: ''')
    if choice == 'Search Person':
         dir_info = input('Hello! please enter info:')
         directory =+ dir_info
    if choice == '0':
        insert_info = 1
    
