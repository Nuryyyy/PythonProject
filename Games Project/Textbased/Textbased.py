import time
#introduction
title = '''
        ███████████████████▀████████████████████████████████████████████
        █▄─▀█▀─▄██▀▄─██─▄▄▄▄█▄─▄█─▄▄▄─██▀▄─██▄─▄█████─▄▄▄─█▄─██─▄█▄─▄▄─█
        ██─█▄█─███─▀─██─██▄─██─██─███▀██─▀─███─██▀███─███▀██─██─███─▄▄▄█
        ▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▀
        '''
print(title)
time.sleep(2)
name = input("\nWelcome to test-based game!\nTo begin, enter your name adventurer: ").capitalize()
time.sleep(3)



def game_loop():
    introduction()
    first_scene()

def introduction():
    #introduction:
        
        print('''
            *****************************************************************************************************************
                        Gloomwood Forest has always been a favorite of Lady Fele's because of the forest's              
                        abundant wildlife and musical rivers. It was a place of joy for her. A mystical cup             
                        hidden beneath the river has kept the forest safe from the horrific beasts who attack           
                        it. However, one day the water had dried up, the plants were wilting, strange new                  
                        species had appeared, and the culprit must be the disappearance of the magical cup.             
            *****************************************************************************************************************
            ''')
        print("")
        time.sleep(5)
        print(f"And now the time has come for you, {name}, brave adventurer, to assist Lady Fele in retrieving the magical cup. ")
        time.sleep(3)
        
def first_scene():
    choice_1 = input("\nYou are in the midst of a now wasted forest and have two options: to your left is a horrendous bear, and to your right is a path that goes deeper into the forest. Which path do you will you take?\n     a: Right\n     b: Left\nChoose: ").lower()
    if choice_1 == 'a':
            right()
    else:
        print("That was your last breath! You were consumed by the ravenous beast.")
        time.sleep(3)
        print('''
                █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
                █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄
                ''') 
        repeat = input("\nWanna play again? y/n: ").lower()
        if repeat == "y":
            game_loop()
        else:
            no_game()
def right():
    choice_2 = input("As you venture farther into the forest, you notice a crumpled piece of paper among the fallen leaves; do you pick it up to read it, or do you simply pass it by?\n    a: Pick it up\n    b: Leave it\nChoose: ").lower()
    if choice_2 == 'a':
        read()
    else:
        print("The letter was left on the ground, and as you walked by, you noticed footprints leading over a dry river. Following the footprints, you came face to face with a menacing serpent, its eyes piercing as it stared straight at you. Your mind is clouded by dread, and you must decide whether to flee or confront the terrifying serpent. It made a hissing sound, ran after you, and swallowed you whole.")
        time.sleep(3)
        print('''
                █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
                █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄
                ''') 
        repeat = input("\nWanna play again? y/n: ").lower()
        if repeat == "y":
            game_loop()
        else:
            no_game()
def read():
    print("You took the letter in your hands and read it. 'Don't go where the footsteps go; they lead to certain death! Instead, go to your left and be careful.'")
    choice_4 = input("As you followed the directions and veered to the left, you came across an abandoned home whose roots wrapped around the structure as though it were an integral part of the massive tree that stood nearby. You decide whether to go towards it or turn back.\n     a: Forward     \n     b: Turn back\nChoose:").lower()
    if choice_4 == 'a':
        house()
    else:
        print("You decided to go back, got lost in the woods, and were devoured by a deathly serpent.")
        time.sleep(3)
        print('''
                █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
                █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄
                                                    ''') 
        repeat = input("\nWanna play again? y/n: ").lower()
        if repeat == "y":
            game_loop()
            
        else:
            no_game()
def house():
    choice_5 = input("You quietly walk towards the house and peek through. Then there it is! You saw the stolen magical cup! In a flash, you're off to the house. You burst inside the house, your blade ready to slay anyone in your path. Then you noticed a young woman clothed in tattered and ragged clothes. Her entire body shook with fear and shock. Behind her was a bed on which a frail old man lay. She begged you to spare her life, saying she simply needs the cup to heal her grandfather, who was dying. You must decide whether to return the cup or let it work its magic on the dying elderly man.\n     a: Help\n     b: Take back\nChoose: ").lower()
    if choice_5 == 'a':
        help()
    else:
        print(f'''
                While the young woman sobbed uncontrollably, you took the cup and abandoned the dying old man. 
                Casting a spell of eternal damnation upon you. Even though Lady Fele was overjoyed and gave you 
                an award, she was saddened by the whole story saddened and went looking for the young woman, only
                to discover that she had vanished from her home and had never been seen again. The Gloomland is 
                restored to its former glory. You, {name}can't shake the image of a dying man and the nightmares 
                of terrifying monsters. Ultimately, he was doomed by his own guilt.
                ''')
        ending()
def help():
    print('''
          Upon hearing the sorrowful tale, one could not help but feel sorrow. In allowing the cup to do its healing work,
          you made the old man and his daughter very happy. The elderly man miraculously became a young man, and he blessed
          you with goodness as payment for your kindness and good heart. The story of the enchanted cup and your return to 
          Lady Fele was joyously reported. It filled her with pride and happiness. In return for your service to her kingdom, 
          she has showered you with gifts and elevated you to a position of prominence. Gloomwood's previous splendor is 
          restored when the cup is returned to its rightful place.''')  
    ending()     
def ending():
    time.sleep(5)
    print('''       
                                ▀█▀ █░█ █▀▀ █▄░█   █▀▀ █▄░█ █▀▄
                                ░█░ █▀█ ██▄ █░▀█   ██▄ █░▀█ █▄▀''')
    repeat = input("\nWanna play again? y/n: ").lower()
    if repeat == "y":
            game_loop()
    else:
        no_game()
def no_game():
    print('''
          ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   ▄▀█ █▀▄ █░█ █▀▀ █▄░█ ▀█▀ █░█ █▀█ █▀▀ █▀█ █
          ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀█ █▄▀ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ██▄ █▀▄ ▄
            ''') 
        
game_loop()    


            

