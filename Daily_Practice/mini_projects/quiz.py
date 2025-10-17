# this script will display a 5-question quiz. The users will get to choose from a set of 4 options and it will track their score and display correct answers at the end

questions = ("What is the Oklahoma State University Mascot named? ", 
             "How many teams are in the Big 12 football conference? ", 
             "What is the name of Oklahoma State's football stadium? ",
             "What city is Oklahoma State University located? ",
             "Name of famous country singer that attended Oklahoma State University? ")

answers = ("A. Pistol Pete B. Masked Raider C. Peter D. Boone",
           "A. 12 B. 8 C. 16 D. 14",
           "A. Boone Pickens B. Neyland C. Gaylord D. Marshall",
           "A. Tempe B. Tulsa C. Oklahoma City D. Stillwater",
           "A. Steely Dan B. Garth Brooks C. Raskal Flats D. Kenney Chesney")

correct = ("A", "C", "A", "D", "B")


for i in questions:
    print(f'Question #{questions.index(i)+1}: {i}')
    for a in answers:
        print(f'Your answer choices are: {a}')


    # for  in answers:
    #     answer = input("Type your answer here: ").upper()
