# Zachary Larsen
# CW1102 CW2
# Task 6
##Program tests if a word is found in the dictionary and tile set

import random

#Function to read in file that exists locally
#Returns a list from the contents of the file
def readFile(name):

    #only works for relative paths

    try:
        f = open(name)
        new_list = f.read().split('\n')
        return new_list

    #Except Block
    except IOError:
        print("There was an error reading the file %s.txt." % name)
    except:
        print("An unexpected error occured")
    finally:
        f.close()

#Begin Letter Validation Function
#Accepts a word and returns True if
#all characters are in the alphabet
#and False if not
def onlyEnglishLetters(word):
    
    #create a list of English Letters
    alphabet =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    #Check if each letter in the word is contained in Alphabet
    try:
        for letter in word:
            assert letter.upper() in alphabet, "Exception: Non-Alphabetic Character!"
    except AssertionError as msg:
        return False

    return True   #If all letters were in the alphabet, the loop ends and returns True


#Generate random tile list
#Pulls from Global Variable tiles and returns a list
def randTiles():

    Tiles=readFile('tiles.txt') #Get tile list from tiles.txt
    newTiles=[]
    for i in range(0,7):
        newTiles.append(Tiles[random.randrange(0,len(Tiles))]) #Uses the global constant read in from Task1 Tiles to pull 7 random tiles.
    return newTiles


#Begin Tile Validation
#Word must contain only english letters
#Word characters must exist in tile set
#Returns True if above is satisfied, False if not
def checkTiles(word, myTiles):
    
    remainingTiles=myTiles.copy()  #Create a copy of tiles so we don't affect the original.

    #Begin Try Except block
    try:
        #For loop to test characters against tiles
        for char in word:
            assert onlyEnglishLetters(word), "Exception! The Word contains Non-Alphabetic Characters!"  #Create Assert Statement for non english letter
            assert char.upper() in myTiles, "Exception! The word contains a character not found in your Tiles." #If not found in tiles, throw assertion error

            #For loop to pop the tile matched, allows for checking for multiple of the same character.
            for tile in range(len(remainingTiles)):

                #If char is no longer in remaining tiles, throw exception
                assert char.upper() in remainingTiles, "Exception: The word contains a character you have used too many times."
                
                if char.upper() == remainingTiles[tile]:
                    remainingTiles.pop(tile)
                    break
                else:
                    continue
                        
    except TypeError:
        print("Exception: The Word Contains Non-Alphabetic Character!")
        return False

    except AssertionError as msg:
        print(msg)
        return False
    
    return True  #Return True if all characters found in myTiles


    
#Begin Word Validation Function
#Word must only contain English Letters
#Word characters must exist in tile set
#Word must exist in dictionary
#Returns True if above is satisfied, False if not
def isValid(word, myTiles, dictionary):
    try:
        assert checkTiles(word, myTiles)  #Asserts word is in current Tile Set
        assert word.upper() in dictionary, "Exception: Word not found in dictonary!"  #Asserts word is in dictionary
        return True
    except AssertionError as msg:
        if str(msg):
            print(msg)
        return False
    
    
#Starting Tile set for Test Data
myTiles = ['T','Y','S','E','U','W','I']
Dictionary=readFile('dictionary.txt') #Read in the dictionary into a list

#Program Introduction
print('This Program will check if you can create a given word with the tiles you have')
print('You currently have these tiles: ' + str(myTiles) + "\n")

##Send some test data
test_data=['Yes','west','Set','Suit','Sweet','Swet','Reza','342','Last One']
print('This program returns if a word is valid and the tiles remaining\nHere is some Test Data!\n')

print("For the below words, we get the following results: \n")

for word in test_data:
    if isValid(word, myTiles, Dictionary):
        print(word + " is a valid word \n")
    else:
        print(word + " is an invalid word.\n")

##End Test Data
        
main_loop = 'Y'

#Begin Main User loop
while main_loop.upper() == 'Y':
    
    main_loop=input('Would you like to get the score of another word?: (Y|N)')
    
    if main_loop.upper() == 'Y':

        #Displays current tile set and gives user option to generate new set.
        print('\nThe Tiles you have are: ' + str(myTiles) + '\n')
        changeTile='Y'
        while changeTile.upper()=='Y':
            changeTile=input('Would you like to draw new tiles? Y or N: ')
            if changeTile.upper()=='Y':
                myTiles = randTiles()
                print('\n' + str(myTiles) + '\n')
            elif changeTile.upper()=='N':
                break
            else:
                print('\nPlease enter a Y or N\n')
                changeTile='Y'
                continue

        #Display Current Tile set again before getting user input
        print('\nThe Tiles you have are: ' + str(myTiles) + '\n')

        #Get User data and test
        user_word=input('Please enter your own word to test against the tiles: ')
        print('\n')

        #Tests user input and confirms if word is valid or not.
        if isValid(user_word, myTiles, Dictionary):
            print("YES! \'" + user_word.upper() + "\' is a valid word!\n")
        else:
            print("No! \'" + user_word.upper() + "\' is not a valid word.\n")
            
    elif main_loop.upper() == 'N':
        print('Goodbye!')
        break
    else:
        print("\nPlease enter Y or N\n")
        main_loop='Y'
        continue


