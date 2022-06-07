from responses import fighter, mage, barbarian
import string
print('Welcome to my game, I hope you will enjoy it ^^! ')
fighter()
#beginning of the game
def choosegender():
    gender =  input('Are you male, female or other? ')
    if gender == ("male"):
        return chooseklasses()
    elif gender == ("female"):
        return chooseklasses()
    elif gender == ("other"):
        return chooseklasses()
    else:
        return 'you can\'t play the game'
#to choose your classes
def chooseklasses():
    question = input('Hello, adventerure do you wish to battle? \n Type "yes" if you want to battle!  ')
    if question == ("yes"):
        classes =  input('choose your class, fighter, mage or barbarian:  ')
        if classes == "fighter":
            return story('Fighter')
        elif classes == "mage":
            return story('Mage')
        elif classes == "barbarian":
            return story('Barbarian')
        else:
            return 'You have not chosen barberian, mage, or fighter so you will not contineu. '
    else:
        return 'You scared little bitch, you no want batlle no want honer!! go back to baby corner!! '

#storyline 
def story(battlestyle):
    #fighter class
    if battlestyle == "Fighter":
        fighter()
    #mage class
    elif battlestyle == "Mage":
        mage()
    #barbarien class
    elif battlestyle == "Barbarian":
        barbarian()
    else:
        return ('something went horrably wrong and we will figure out next time what it is.')

print(choosegender())