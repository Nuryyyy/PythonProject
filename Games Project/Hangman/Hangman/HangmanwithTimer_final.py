import os
import random # randomize words to guess
from time import sleep, time
from hangman_drawing import hangman, welcome, game_over, congratulation, endgame, times_up # I compile all drawing or art in one file and just call them here
from hangman_words import animals_list, countries_list, fruits_list, movies_list, sport_list #divided into 5 diff categories with their correspanding lists

def game_loop(): #flow of them whole game/ Purpose for repeating game
  Welcome()
  game_play()

def Welcome():
    print(welcome)
    sleep(2)
    name = str(input("\n What is your name? ").capitalize())
    print(f'''
                 **********************************************************************************************************************************************************
                                                                  Hello, and welcome to the HANGMAN GAME, {name}. 
                                        There are five different categories from which you select and the secret word will be derived from that. 
                    To win, you must correctly guess the hidden word within 30 seconds. Remember, there are six(6) lives you can use to win the game before you are hanged.
                 **********************************************************************************************************************************************************
         
                                                                                      ''')
    os.system("pause")

def game_play():
  #variable
  timer = 30
  game_start = True #to start the game
  lives = len(hangman) - 1 #6
  already_guessed = []
  
  choice = input('''
    Select number of category: 
      1. Animals
      2. Countries
      3. Fruits
      4. Movies
      5. Sports
      >>>  ''')
  while not choice.isdigit() or not 1 <= int(choice) <= 5 :
    print("That does not correspond to any of the choices.")
    choice = (input("Please enter a NUMBER of your choice >>> "))
  if choice == '1':
    word_list = animals_list
  elif choice == '2':
    word_list = countries_list
  elif choice == '3':
    word_list = fruits_list
  elif choice == '4':
    word_list = movies_list
  elif choice == '5':
    word_list = sport_list
  
  word_guess = random.choice(word_list)
  
  guess_display = '_' * len(word_guess) #display the number of word to guess in line
  print(f"\nThis is the Hangman word from category {choice}: {guess_display}")
  
  start_time = time() #we begin counting
  while game_start:
    input_letter = input("""
                         
***********************************************************************
Guess a letter: """).lower()
  
    if input_letter in already_guessed: #print the letter that was already guess
      print("\nYou already guessed that letter! Here is what you've guessed:")
      print(','.join(already_guessed))
      #already_guessed = already_guessed + input_letter
      
    if input_letter not in word_guess and input_letter not in already_guessed: #letter input is incorrect and if letter is already guessed, it will not deduct number or tries. 
        lives -= 1
        if lives < 6 and lives != 0:
            print(hangman[lives])
            sleep(1)
            print(f'\nYou guessed wrong! You have {lives} turn(s) left')
        else:
            print(hangman[lives])
            print(game_over)
            print(f"\nSorry, you didn't guess the secret word.\nThe secret word is '{word_guess}'")
            game_start = False
            exit()
      
    already_guessed += input_letter #displays the letter answered less the line
    counter = 0
    
    #in this area we made the design "_" for unguess letter and for every correct letter in will be replace by the correct one. And also displat the already guessed letter.
    for letter in word_guess:
        if letter in already_guessed:
            print(f"{letter}",end="")

        else:
            print("_",end='')
            counter +=1
            
    if counter == 0:
        print(congratulation)
        sleep(1)
        game_start = False
        exit()
    
    #times up
    end_time = time()
    time_diff = int(end_time - start_time)
    if time_diff > timer:
        print(times_up)
        print(f"You've been hanged!")
        print(hangman[0])
        print(f"The secret word is '{word_guess}'.")
        exit()
        game_start = False
        
def exit():
    again = input("\nWant to play again? Y/N >>> ").upper()
    if again == 'Y':
        game_loop()
          
    else:
      print(endgame)

    
game_loop()

