import os #for the option press any key to proceed
from pickle import FALSE
from time import sleep
from drawings import title, game_over, the_end, thank_you

print(title)
sleep(1.5)
name = input("\nWelcome to text-based game!\nTo begin, enter your name adventurer: ").capitalize()
print(f"""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                   Hello adventurer, {name}. In this text-based interactive game, you will need to decide what action to do next, 
                    and the results of that decision will determine whether or not you make it to the finish of the adventure.     
                -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
      
      """)
os.system("pause")

class Scenarios:
    def __init__(self, decision, next_scene, no_next_scene,alive): #alive means you can continue the adventure alive
        self.decision = decision
        self.next_scene = next_scene
        self.no_next_scene = no_next_scene
        self.alive = alive

playscene = {
    "scene_1" : Scenarios(
        decision = "You are in the midst of a now wasted forest and have two options: to your left is a horrendous bear, and to your right is a path that goes deeper into the forest. Which path do you will you take?\n    A: Right\n    B: Left",
        next_scene= "scene_2",
        no_next_scene= "That was your last breath! You were consumed by the ravenous beast.",
        alive = 'A'),
    "scene_2" : Scenarios(
        decision="As you venture farther into the forest, you notice a crumpled piece of paper among the fallen leaves; do you pick it up to read it, or do you simply pass it by?\n    A: Pick it up\n    B: Leave it\n",
        next_scene="scene_3",
        no_next_scene="The letter was left on the ground, and as you walked by, you noticed footprints leading over a dry river. Following the footprints, you came face to face with a menacing serpent, its eyes piercing as it stared straight at you. Your mind is clouded by dread, and you must decide whether to flee or confront the terrifying serpent. It made a hissing sound, ran after you, and swallowed you whole.",
        alive = "A"),
    "scene_3" : Scenarios(
        decision = "You took the letter in your hands and read it. 'Don't go where the footsteps go; they lead to certain death! Instead, go to your left and be careful. As you followed the directions and veered to the left, you came across an abandoned home whose roots wrapped around the structure as though it were an integral part of the massive tree that stood nearby. You decide whether to go towards it or turn back.     \n     A: Turn back     \n     B: Forward",
        next_scene = "scene_4",
        no_next_scene="You decided to go back, got lost in the woods, and were devoured by a deathly serpent.",
        alive="B"),
    "scene_4" : Scenarios(
        decision="You quietly walk towards the house and peek through. Then there it is! You saw the stolen magical cup! In a flash, you're off to the house. You burst inside the house, your blade ready to slay anyone in your path. Then you noticed a young woman clothed in tattered and ragged clothes. Her entire body shook with fear and shock. Behind her was a bed on which a frail old man lay. She begged you to spare her life, saying she simply needs the cup to heal her grandfather, who was dying. You must decide whether to return the cup or let it work its magic on the dying elderly man.\n     A: Help\n     B: Take back",
        next_scene= """
                        Upon hearing the sorrowful tale, one could not help but feel sorrow. In allowing the cup to do its healing work, you made the old man and his daughter very happy.
                        The elderly man miraculously became a young man, and he blessed you with goodness as payment for your kindness and good heart.  The story of the enchanted cup 
                        and your return to Lady Fele was joyously reported. It filled her with pride and happiness.  In return for your service to her kingdom, she has showered you with
                        gifts and elevated you to a position of prominence. Gloomwood's previous splendor is restored when the cup is returned to its rightful place.
                                        
                    """,
        no_next_scene= """ 
                        While the young woman sobbed uncontrollably, you took the cup and abandoned the dying old man. Casting a spell of eternal damnation upon you. 
                        Even though Lady Fele was overjoyed and gave you an award, she was saddened by the whole story to discover that she had vanished from her home
                        and had never been seen again. The Gloomwood is restored to its former glory. You, {name}can't shake the image of a dying man and the nightmares
                        of terrifying monsters. Ultimately, he was doomed by his own guilt.
        
        """,
        alive="A")
        }
def flow():
    synopsis
    play_scene(playscene["scene_1"])
    play_again()
def synopsis():
    print('''
                -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                            Gloomwood Forest has always been a favorite of Lady Fele's because of the forest's              
                            abundant wildlife and musical rivers. It was a place of joy for her. A mystical cup             
                            hidden beneath the river has kept the forest safe from the horrific beasts who attack           
                            it. However, one day the water had dried up, the plants were wilting, strange new                  
                            species had appeared, and the culprit must be the disappearance of the magical cup.             
                -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            ''')
    print("")
    os.system("pause")
    print("")
    print(f"And now the time has come for you, {name}, brave adventurer, to assist Lady Fele in retrieving the magical cup. ")
    print("")
    sleep(1.5)
def play_scene(scene):
    print(scene.decision)
    user_input = input("Chose your next move >>>> ").upper()
    print("")
    while not scene.decision == playscene["scene_4"].decision:
        if user_input == scene.alive:
            play_scene(playscene[scene.next_scene])
        elif user_input != scene.alive:
            print(scene.no_next_scene)
            print(game_over)
            play_again()
            break
        break
    if scene.decision == playscene["scene_4"].decision:
        if playscene["scene_4"].alive == 'A':
            print(playscene["scene_4"].next_scene)
            play_again()
        else:
            print(playscene["scene_4"].no_next_scene)
            play_again()
def play_again():
    print(the_end)
    yes = input("Want to play again? Y/N >>> ").upper()
    if yes == 'Y':
        flow()
        FALSE
    else:
        print(thank_you)
        FALSE
        

synopsis()            
play_scene(playscene["scene_1"])
#play_again()