import time
from tkinter.messagebox import QUESTION


#Welcome message
welcome = '''
            ████████████████████████████████████████████████████████████████████████████████████████████▀█████████████████████
            █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─███─▄▄▄─█▄─██─▄█▄─▄█░▄▄░▄███─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█
            ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─███─██▀─██─██─███─███▀▄█▀███─██▄─██─▀─███─█▄█─███─▄█▀█
            ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀───▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀'''
print(welcome)
time.sleep(2.5)
#variables
score = 0
quiz = True
#beginning
name = input("\nTo begin, enter your name: ").capitalize()
time.sleep(1)
print(f"Hi {name}! Read the instruction below before taking the quiz.")

while quiz:
    def instruction():
        time.sleep(2)
        print('''
        ===============================================================================================================================================================
        You are given ten(10) number of items from which you must select the letter that corresponds to your answer. For each accurate response, you receive one point.
        Remember, to pass the quiz you must get at least 8 points.")
        ===============================================================================================================================================================
        ''')
        time.sleep(3)
        begin = input("To begin type 'y' or to exit the quiz type any letter: ").lower()
        if begin == 'y':
            question()
        else:
            quiz = False
            
    def question():
        global score
        #Questions1
        print("1. Which built-in function can get information from the user:\na. input\nb. write\nc. get ")
        answer_1 = input("Answer: ").lower()
        if answer_1 == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions2
        print("###############################################################################################################################")
        print("2. This function prints the specified message to the screen, or other standard output device.\na. print()\nb. type()\nc. sort()")
        answer_2 = input("Answer: ").lower()
        if answer_2 == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions3
        print("###############################################################################################################################")
        print("3. Type of variable acts as a container that holds information that cannot be changed later.\na. list\nb. constants\nc. dictionary")
        answer_3 = input("Answer: ").lower()
        if answer_3 == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions4
        print("###############################################################################################################################")
        print("4. A symbolic name that is a reference or pointer to an object.\na. dictionary\nb. variable\nc. function")
        answer_4 = input("Answer: ").lower()
        if answer_4 == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions5
        print("###############################################################################################################################")
        print("5. It is a reserved word in Python that is used to define the Python language's syntax and structure.\na. keyword\nb. interpreter\nc. list")
        answer_5 = input("Answer: ").lower()
        if answer_5 == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions6
        print("###############################################################################################################################")
        print("6. Is a collection of script modules accessible to a program to simplify the programming process and removing the need to rewrite commonly used commands.\na. dictionary\nb. list\nc. library")
        answer_6 = input("Answer: ").lower()
        if answer_6 == 'c':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions7
        print("###############################################################################################################################")
        print("7. When you have two or more strings that you want to combine into one.\na. join()\nb. concatenation\nc. string")
        answer_7 = input("Answer: ").lower()
        if answer_7 == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions8
        print("###############################################################################################################################")
        print("8. A function that returns the length of a given string, array, list, tuple, dictionary, or other data structure.\na. len()\nb. compile()\nc. dir()")
        answer_8 = input("Answer: ").lower()
        if answer_8 == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions9
        print("###############################################################################################################################")
        print("9. A _______ operator compares two values and returns a boolean value, either True or False.\na. AND\nb. OR\nc. comparison")
        answer_9 = input("Answer: ").lower()
        if answer_9 == 'c':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        #Questions10
        print("###############################################################################################################################")
        print("10. The ________ statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.\na. break\nb. pass\nc. continue")
        answer_10 = input("Answer: ").lower()
        if answer_10 == 'c':
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        
        if score <= 5:
            print(f"\nFinal Score: {score}\nBetter luck next time!")
        if score == 10:
            print(f"\nFinal Score: {score}\nPerfect!")
        if 10 > score > 5: #6-9
            print(f"\nFinal Score: {score}\nWell done!")
    instruction()       
    #game_quiz()
    print("")
    final_question = input("Wanna try again? y/n\n").lower()
    if final_question == 'y':
        score = 0
        instruction()
    else:
        print("\nThank you for playing Nury's Quiz Game!")
        break
        
    #passing score
    #summary
