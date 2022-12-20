from time import sleep
from random import shuffle
import os


#Welcome message
welcome = '''
            ████████████████████████████████████████████████████████████████████████████████████████████▀█████████████████████
            █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─███─▄▄▄─█▄─██─▄█▄─▄█░▄▄░▄███─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█
            ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─███─██▀─██─██─███─███▀▄█▀███─██▄─██─▀─███─█▄█─███─▄█▀█
            ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀───▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀'''
print(welcome)
sleep(2.5)

name = input("\nTo begin, enter your name: ").capitalize()
sleep(1)
print(f"\nHi {name}! Read the instruction below before taking the quiz.")
sleep(1.5)

class MC(): #Multiple Choice
    
    def __init__(self, question, right_answer, other_choices):
        self.question = question
        self.right_answer = right_answer
        self.other_choices = other_choices
        
        
list_of_questions = [
    MC("Which question no longer concerns the modern software engineer?:","Why does computer hardware cost so much?", ["Why does software take a long time to finish?","Why can’t software errors be removed from products prior to delivery?"]),
    MC("Which of the items listed below is not one of the software engineering layers?:","Manufacturing",["Process","Methods"]),
    MC("Which of these are the 5 generic software engineering framework activities?:","communication, planning, modeling, construction, deployment.",["communication, risk management, measurement, production, reviewing.","analysis, planning, designing, programming, testing."]),
    MC("The waterfall model of software development is:","A reasonable approach when requirements are well defined",["A good approach when a working program is required quickly","An old fashioned model that is rarely used any more"]),
    MC("The incremental model of software development is:","A good approach when a working core product is required quickly.",["A reasonable approach when requirements are well defined","A revolutionary model that is not used for commercial products"]),
    MC("The prototyping model of software development is:","A useful approach when a customer cannot define requirements clearly",["A reasonable approach when requirements are well defined","A risky model that rarely produces a meaningful product"]),
    MC("Which of the following is not one of the principles of good coding?","Refractor the code after you complete the first coding pass",["Write self-documenting code, not program documentation","Create unit tests before you begin coding"]),
    MC("Which of these is not one of the phase names defined by the Unified Process model for software development?","Validation phase",["Inception phase","Construction phase"]),
    MC("Which of the following is not necessary to apply agility to a software process?","Eliminate the use of project planning and testing",["Only essential work products are produced","Uses incremental product delivery strategy"]),
    MC("Which of the following is not an important trait of an effective software engineer?","Follows process rule dogmatically",["Attentive to detail","Brutally honest"])
]

         
class TF: #True or False questions
    def __init__(self,questions,correct,other):
        self.questions = questions
        self.correct = correct
        self.other = other
        
True_False = [
    TF("Teams with diversity in the individual team member skill sets tend to be more effective than teams without this diversity.","TRUE","FALSE"),
    TF("Software engineering umbrella activities are only applied during the initial phases of software development projects","FALSE","TRUE"),
    TF("The essence of software engineering practice might be described as understanding the problem, planning a solution, carrying out the plan, and examining the result for accuracy.","TRUE","FALSE"),
    TF("Human aspects of software engineering are not relevant in today’s agile process models.","FALSE","TRUE"),
    TF("Planning ahead for software reuse reduces the cost and increases the value of the systems into which they are incorporated.","TRUE","FALSE")
]
def flow():
    intro()
    quiz_1()
    start_quiz_2()
    blabla()

def intro():
    print('''   
            ========================================================================================================================================================
            This quiz is divided into two parts. The first part contains five(5) questions with TRUE or FALSE options, while the second part contains ten(10) 
            questions with multiple answer options. There are a total of 15 items from which you must choose the NUMBER that correlates most closely to your answer. 
            One point is awarded for each correct answer. Remember that you must earn at least 10 points to pass the quiz.
            ========================================================================================================================================================
            ''')
    
    os.system("pause")
    
def quiz_1():
    score = 0
    shuffle(True_False)
    question_num = 1 #item number
    total_score = 0
    #quiz_2 = True

    for item in True_False:
        print(f"\nQuestion #{question_num}: {item.questions}")
        choices = [item.other] + [item.correct] #square brackets turn  answer into list
        shuffle(choices)
        count = 0 #count of choices and in "while" statement choices will continue itirate until it's exhausted
        while count < len(choices):
            print(f"{str(count+1)}: {choices[count]}")
            count +=1
        ans = input("\nEnter the the number of your answer >>> ")
        while not  ans.isdigit() or not(len(choices)>= int(ans) > 0):
            print("That does not correspand to any of the choices.")
            ans = (input("Please enter a NUMBER of your choice >>> "))
        if choices[int(ans)-1] == item.correct:
            print("Correct answer!")
            question_num += 1
            score += 1
        else:
            print("Incorrect!")
            print(f"Correct answer was >>> {item.correct}")
            question_num += 1
    total_score += score
    print("")
    print(f"Part 1 score: {total_score}/5")
    
    print("\nAre you ready to begin the part 2 of the quiz?")
    os.system("pause")
    return total_score
def start_quiz_2():
    total_score = 0
    score = 0 # per item
    question_num = 6
    shuffle(list_of_questions)
    for  item in list_of_questions:
        print(f"\nQuestion #{question_num}: {item.question}")
        print("Choices:")
        choices = [item.right_answer] + item.other_choices
        shuffle(choices)
        count = 0
        while count < len(choices):
            print(f"{str(count+1)}: {choices[count]}")
            count += 1
        user_ans = input("Enter the the number of your answer >>> ")
        while not user_ans.isdigit() or not(len(choices)>= int(user_ans) > 0):
            print("That does not correspond to any of the choices.")
            user_ans = input("Please enter a NUMBER of your choice >>> ")
        if choices[int(user_ans)-1] == item.right_answer:
            print("Correct answer!")
            question_num += 1
            score += 1
        else: #if answer is wrong it will print wrong
                question_num += 1
                print("Incorrect!")
                print(f"Correct answer was >>> {item.right_answer}")
                
                
    total_score += score
    print(f"Part 2 score: {total_score}/10") 
  
    totalsss = quiz_1() + total_score
    if totalsss <= 9:
        print(f"\nFinal Score: {totalsss}/15 \nFAILED! To do well on the quiz, you should study more.")
        final()
    if totalsss == 15:
            print(f"\nFinal Score: {totalsss}/15 \nPERFECT! Such a brilliant mind.")
    if 10 > totalsss >= 14: #10-14
            print(f"\nFinal Score: {totalsss}/15 \nWELL DONE! You passed the quiz!") 

def final():
  final_question = input("\nWant to try again? Y/N >>> ").upper()
  if final_question == 'Y':
      questions_num = 1
      score = 0
      flow()
      False
  else:
      print("\nThank you for playing Nury's Quiz Game!")
      False

intro()
# final_question = input("\nWant to try again? Y/N >>> ").upper()
# if final_question == 'Y':
#     questions_num = 1
#     score = 0
#     flow()
#     False
# else:
#     print("\nThank you for playing Nury's Quiz Game!")
#     False
        
        