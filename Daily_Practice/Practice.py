# a script to practice building functions and using loops
# build an script that will take in user information and add them to a directory
# then ask a user who they want to search for 
    
# defaul insert directory info
directory = {"chase wolters": "123-432-2444", 
             "evelyn wilson": "321-325-8740",
             "shawn wolters": "298-294-8597"}

insert_info = 0

choice = input('''Hello! Welcome to the directory, please pick an action:
Menu
See full directory
Search Person
Insert new info
If done with directory, please enter 0: ''')
while insert_info == 0:
    if choice == 'menu':
        print('''
Menu
See full directory
Search Person
Insert new info
If done with directory, please enter 0: ''')
    if choice == 'see full directory':
        print(directory.keys())
    if choice == 'search person':
        person_info = input("Please type the name of the person who's info you want to know: ").lower()
        if person_info in directory.keys():
            print(directory[person_info])
        else:
            print('Person not in directory')
    # using .split method to add additional entries to the directory
    if choice == 'insert new info':
        dir_info = input('''Please enter info in specified format
firstname lastname: phonenumber: ''')
        name = dir_info.split(':')
        directory[name[0]] = name[1]
    if choice == '0':
        insert_info = 1
    else:
        choice = input('please pick an action: ').lower()
