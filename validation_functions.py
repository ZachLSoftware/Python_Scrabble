###Functions###
import random
import numpy as np



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
    except AssertionError:
        return False

    return True   #If all letters were in the alphabet, the loop ends and returns True

   

#Begin Word Validation Function
#Word must only contain English Letters
#Word characters must exist in tile set
#Word must exist in dictionary
#Returns True if above is satisfied, False if not
def isValid(word, myTiles, dictionary):
    
    try:
        #assert checkTiles(word, myTiles)  #Asserts word is in current Tile Set
        assert word.upper() in dictionary, "Exception: Word not found in dictonary!"  #Asserts word is in dictionary
        return True
    except AssertionError as msg:
        if str(msg):
            print(msg)
        return False



        
        

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


def checkBoard(d,x,y,word,board):
    try:
        xl=x+len(word)
        yl=y+len(word)
        if d.upper() == 'H':
            
            assert (board[x,y:yl]!='_').any(), "Exception: This section contains no words!"
            for char in word:
                if board[x,y]==char.upper() or board[x,y]=='_':
                    y+=1
                    valid = True
                else:
                    valid = False

        elif d.upper() == 'V':
            assert (board[x:xl,y]!='_').any(), "Exception: This section contains no words!"
            for char in word:
                if board[x,y]==char.upper() or board[x,y]=='_':
                    x+=1
                    valid = True
                else:
                    valid = False
    except AssertionError as msg:
        print(msg)
        valid = False
    except:
        print('Unknown Error')
        valid=False
    finally:
        return valid

def checkBoardTiles(d,x,y,word,board,myTiles):
    char_list=[]
    if d.upper()=='H':
        for char in word:
            if board[x,y]==char.upper():
                char_list.append(char)
                y+=1
            else:
                y+=1
    elif d.upper()=='V':
        for char in word:
            if board[x,y]==char.upper():
                char_list.append(char)
                x+=1
            else:
                x+=1
    print(char_list)
    for char in char_list:
        word=word.replace(char,'')
    print(word)
    if checkTiles(word, myTiles):
        return True
    else:
        return False
                
                
