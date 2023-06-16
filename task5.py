# Zachary Larsen
# CW1102 CW2
# Task 5
##Program tests if a word is valid based on tile set alone

import random  #To generate random tile list

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
#Word must only contain letters found in the alphabet
#Returns True if above is satisfied, False if not
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
    Tiles=readFile('tiles.txt')
    newTiles=[]
    for i in range(0,7):
        newTiles.append(Tiles[random.randrange(0,len(Tiles))])  #Uses the global Variable read in from Task1 Tiles to pull 7 random tiles.
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

                #If the character is the same as the current tile, pop the tile from the list
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



#Declare myTiles
myTiles = ['T','Y','S','E','U','W','I']


#Welcome Statment
print('This Program will check if you can create a given word with the tiles you have')
print('You currently have these tiles: ' + str(myTiles) + "\n")

##Send some test data

test_data=['Swet','Set','Wits','Suit','Sweet','Test','Reza',342,'Last One']
print('This program returns if a word is valid.\nHere is some Test Data!\n')

print("For the below words, we get the following results: \n")

for i in range(0,len(test_data)):
    try:
        assert checkTiles(test_data[i], myTiles)
        print("YES! \'" + str(test_data[i]).upper() + "\' can be created with your tiles!\n")
    except AssertionError:
        print("No! \'" + str(test_data[i]).upper() + "\' cannot be created with your tiles.\n")

#End Test Data

##Begin Main Loop for user interaction
main_loop = 'Y'
while main_loop.upper() == 'Y':
    
    #Confirm User wants to continue
    main_loop=input('Would you like to test another word?: (Y|N)')
    if main_loop.upper() == 'Y':

        #Display Current Tile Set
        print('\nThe Tiles you have are: ' + str(myTiles) + '\n')
        changeTile='Y' #Variable for Changing Tiles Loop
        
        #Loop Block that allows the user to generate a new tile list.
        while changeTile.upper()=='Y':
            changeTile=input('Would you like to draw new tiles? Y or N: ')

            #If users specified Y, generate new tile list, else break while loop.
            if changeTile.upper()=='Y':
                myTiles = randTiles()
                print('\n' + str(myTiles) + '\n')
            elif changeTile.upper()=='N':
                break
            else:
                print('\nPlease enter a Y or N\n')
                changeTile='Y'
                continue

        #Display current tile set again and get user input    
        print('\nThe Tiles you have are: ' + str(myTiles) + '\n')   
        user_word=input('Please enter your own word to test against the tiles: ')
        print("\n")
        
        #Validate Tiles and give user feedback
        if checkTiles(user_word, myTiles):
            print("YES! \'" + user_word.upper() + "\' can be created with your tiles!\n")
        else:
            print("No! \'" + user_word.upper() + "\' cannot be created with your tiles.\n")
            
    #Ends or validates Main Loop input.
    elif main_loop.upper() == 'N':
        print('Goodbye!')
        break
    else:
        print('\nPlease enter a Y or N\n')
        main_loop='Y'
        continue


