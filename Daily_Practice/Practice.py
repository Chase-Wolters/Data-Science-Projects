# a script to practice building functions and using loops
# build an script that will take in user information and add them to a directory
# then ask a user who they want to search for 

# insert directory info
directory = {"chase wolters": "123-432-2444", 
             "evelyn wilson": "321-325-8740",
             "shawn wolters": "298-294-8597"}

insert_info = 0
while insert_info == 0:
    choice = input('''Hello! Pick an action:
see full directory
Search Person
Insert new info
If done with directory, please enter 0: ''').lower()
    if choice == 'see full directory':
        print(directory.keys())
    elif choice == 'search person':
        person_info = input("Please type the name of the person who's info you want to know: ").lower()
        if person_info in directory.keys():
            print(directory[person_info])
    elif choice == 'insert new info':
        dir_info = input('Please enter info:')
        directory.append(dir_info)
    elif choice == '0':
        insert_info = 1

    
