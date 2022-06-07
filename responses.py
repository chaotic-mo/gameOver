def fighter():
    print("You have chosen fighter! ")
    print('Type the following answer in numbers')
    path = int(input('You will have 2 choices, do you want the path of five or the path of four? '))
    if path == (5):
        return 'You have sadly stumbeld in a mase, you will never leave this hell but thanks for playing ^^! '
    elif path == (4):
        print('You aquierd a sword well done, subsequently you also came face to face with a mintour. \n Do you want to fight it? ')
        fight = input('Type "yes" if you want to battle! ')
        if fight == ("yes"):
            print('With a slash, you slaughterd the head of the minatour.')
            proceed = input('You have slayen the beast, you walk further and further until you see a door with de numer 9 on it. \n Would like to proceed to go through it? type "9" if yes. ')
            if proceed == (9):
                print(
                    '''
                    The door has been slammed shut, and befor you realise it, you see a father mintaur and a mother hydra. \n
                    They smell the blood of there new born son, of which they are the parents who made that union. \n
                    To live you need to fight or try to escape.
                    ''')
                again_fight = input('Will you fight the father and mother type "yes". ')
                if again_fight == ("yes"):
                    return('You tried, your hardest to fight them of, but the immortal creatures are far stronger, so you died. ')
                else:
                    return('You tried the other option is assum, x:D did not work out i see. because you are dead now. ')
            else:
                return('You need to go through door 9 to proceed :p. ')
        else:
            return('You have to start over  ')

def mage():
    print('You have chosen mage, your spell list 3 fire balls per round and healing. ')
    door_six = input('as you stummbeld through a forest, you come acorss a old ruin with weird symbols, would like to explore. type "yes" to contineu. ')
    if door_six == ("yes"):
        print('As you explored you suddenly transported too a room. in fornt of you, you see a door that you think you can burn.')
        burn = input('Would you like to burn the door type "yes" for brunning')
        if burn == ("yes"):
            print('You tried burning the wooden door but some how your power does not work in this room.')
            voice = input(
                '''
                You hear a voice telling you, "HAHAHA, YOU WILL NEVER GET OUT OF HERE. \n
                But if you defeat grandfather-ROC and Grandmother-dragon i may consider it."
                Are you going to fight? type "fight"
                ''')
            if voice == ("fight"):
                return('''As you agreed with the 2 giant creaters, a Roc and a Dragon respectivly appeard and you are just slaughtered. \n
                Because of the fact you are the mere level 1 xD. ''')
            else:
                return('Well sucks to be you he let you rot the room :p. ') 
        else:
            return('Without doing anything was a problem so the room was filled with sand and you suffecated. ')
    else:
        return('I guess even mages have cowards :D . ')

def barbarian():
        print('''You have chosen barberian, you crafty basterd. You are more brawn then brain. You also get a hammer ;D. \n
        As you ar taking the hammer, you felt a power auro around you transporting you to unkown location. \n
        As you are transported you see 2 doors with numbers on them, door 8 and door 7 which will you chose?''')
        door = int(input('You, need to type the number of the door. '))
        if door == (8):
            bash = input('You think that you can bash it in with your head or hammer, type "hammer" or "head"')
            if bash == ("head"):
                print('You tried to bash the door, but you did not succeed because you got electrocuded. so you dead :D ')
            elif bash == ("hammer"):
                return'You tried to bash the door with your hammer, but you did not succeed because you got electrocuded :D try  to look for traps.'
            else:
                return '''by doing nothing the story won't progress sorry <,< '''
        elif door == (7):
            print('by going through this door, you survived to no bieng electrocuted, but now you are locked  and the only way to get out is to defeed the orc that you came face to face with.')
            orc = input('wil you fight the orc "yes" or "no"? ')
            if orc == ("yes"):
                weapon = input('Will you fight it with your "head" or "hammer?" ')
                if weapon == ("hammer"):
                    return('You succefully defeated the orc, by bashing his head in you won.')
                elif weapon == ("head"):
                    return('You underestimated the hard skull of the orc, so you bashed youre head in two and you died.')
                else:
                    return('doing nothing will get you killed ;p. ')
            else:
                return('doing noting will get you killed x:D')
        else:
            return('''just don't play then <,<''')

