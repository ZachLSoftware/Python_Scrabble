###Functions###
import random
import numpy as np

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
    except AssertionError:
        return False

    return True   #If all letters were in the alphabet, the loop ends and returns True


#Begin Letter Score Function
#Letter must exist in the alphabet
#Only accepts one character per function call
#Returns score of valid letter or 0 if invalid
def getLetterScore(letter):
    
    Scores=readFile('scores.txt') #Read file to get scores list
    try:
        assert len(letter) < 2, "Exception: More then one character submitted!"  #Raises Exception if too many characters given
        assert onlyEnglishLetters(letter)==True, "Exception: Non-Alphabetic Character!"  #Raises an Exception if English test fails

        #Match the submitted letter with score table
        for i in Scores:
            if letter.upper() == i.split()[0]:
                return int(i.split()[1])

    #Exception Block
    except AssertionError as msg:
        print(msg)
        return 0
    except TypeError:
        print('Exception: Non-Alphabetic Character!')
        return 0

#Begin getWordScore Function
#Word must only contain english letters
#Returns score of word if valid, 0 if not valid
def getWordScore(word):
    
    word_score = 0  #set initial value
    try:
        for char in word:
            assert getLetterScore(char)  #Asserts that each letter is valid and returns a valid score.
            word_score += int(getLetterScore(char))

    except AssertionError:
        word_score=0
        
    except TypeError:
        print('Exception: Non-Aphlabetic Character!')
    finally:
        return word_score


#Generate random tile list
#Pulls from Global Variable tiles and returns a list
def randTiles(myTiles):
    Tiles=readFile('tiles.txt')
    newTiles = myTiles.copy()
    while len(newTiles) < 7:
        newTiles.append(Tiles[random.randrange(0,len(Tiles))])  #Uses the global Variable read in from Task1 Tiles to pull 7 random tiles.
    return newTiles
                                
#Begin Tile Validation
#Word must contain only english letters
#Word characters must exist in tile set
#Returns True if above is satisfied, False if not
def checkTiles(word, myTiles):
    
    remainingTiles=myTiles.copy()  #Create a copy of tiles so we don't affect the original.
    wild=myTiles.count('')
    #Begin Try Except block
    try:
        #For loop to test characters against tiles
        for char in word:
            if char.upper() not in remainingTiles and wild>0:
                wild-=1
                continue
            assert onlyEnglishLetters(word), "Exception! The Word contains Non-Alphabetic Characters!"  #Create Assert Statement for non english letter
            assert char.upper() in remainingTiles, "Exception! The word contains a character not found in your Tiles." #If not found in tiles, throw assertion error

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


#Creates Game Board and Column Dictionary for Coordinates
def createBoard():
    board = np.zeros((17,17),'U2') #Initialize array
    board.fill('_')  #Fill with underscores
    COLUMNS={}  #Initialize Columns Dictionary
    alpha='A'
    count=1
    
    #Loop to create Board Borders
    for i in range(1,16):
        board[0,i]=board[16,i]=alpha #Assigns Letters to top and bottom rows.
        board[8,8]='X' #Create Centre Square

        #Expand number columns to 2 spaces for asthetics
        if len(str(i)) < 2:
            board.T[0,i]=board.T[16,i]=' ' + str(i) #Transpose array and set top and bottom rows.
        else:
            board.T[0,i]=board.T[16,i]=str(i)
        
        COLUMNS[alpha]=count #Add to dictionary
        alpha = chr(ord(alpha)+1) #Iterate to next Letter
        count+=1
    board[0,0] = board[0,16]=board[16,0]=board[16,16]='  ' #Set corner squars.

    return (board, COLUMNS) #Return Game Board and Dictionary


#Accepts myTiles and a word, removes used tiles
def removeTiles(word, myTiles):
    remTiles=myTiles.copy() #Copy list
    for char in word:
        remTiles.remove(char.upper()) #Remove character from list
    return remTiles.copy() #Return new list


#Accepts a number and list
#returns new tiles after removing selected tiles
def changeTiles(num, myTiles):
    print('Enter one tile at a time.')
    remTiles=myTiles.copy() #Create copy list
    try:
        for x in range(0,num):
            run=True #Set run for validation loop
            while run:
                y=input('Which tile would you like to replace? ')

                #Checks if entered tile is in list
                if y.upper() in remTiles:
                    remTiles=removeTiles(y,remTiles) #send tile to removeTiles function
                    
                    run=False #break loop
                else:
                    print('\nThat is not in your tiles.\n')
                    run=True
                    
        #print(word)
        newTiles=randTiles(remTiles) #Fills in the tile list
        return newTiles #returns new list.
    
    except ValueError:
        print('Value Error')
        return myTiles
        
        

#Validates if word placement is valid
def checkBoard(d,x,y,word,board):
    #Begin Try Except
    try:
        
        xl=x+len(word) #gets the max row
        yl=y+len(word) #gets the max column

        #Begin Horizontal Test
        if d.upper() == 'H':

            #Asserts word is in bounds
            assert yl<=16, "Word is too long for board location!"

            #Asserts that the word attaches to another word
            assert (board[x,y:yl]!='_').any(), "Exception: This section contains no words!"

            #Begin Checks
            for char in word:
                if board[x,y]==char.upper() or board[x,y]=='_':

                    #Uses a copy of original board to test
                    board[x,y]=char.upper()

                    #Sends to checkPerpWordH function to check if there
                    #are any characters perpindicular to current character
                    assert checkPerpWordH(x,y,word,board), "A perpindicular word cannot be formed here!"
                    y+=1 #Iterate to next column
                    valid = True #Keeps Valid True
                else:
                    valid = False
                    break

            #Tests if the word ends next to another word or at end of board
            if valid:
                if yl-1<=14 and board[x,yl]=='_':
                    valid=True
                elif yl-1==15:
                    valid=True
                else:
                    valid=False  #Returns false if word ends at another word.
            
        #Begin Vertical Check
        elif d.upper() == 'V':

            #Asserts that the word is within bounds
            assert xl<=16, "Word is too long for board location!"

            #Asserts word attaches to another word
            assert (board[x:xl,y]!='_').any(), "Exception: This section contains no words!"

            
            for char in word:
                if board[x,y]==char.upper() or board[x,y]=='_':
                    board[x,y]=char.upper()

                    #Sends to checkPerpWordH function to check if there
                    #are any characters perpindicular to current character
                    assert checkPerpWordV(x,y,word,board), "A perpindicular word cannot be formed here!"
                    
                    x+=1 #Iterate Row
                    valid = True
                else:
                    valid = False
                    break

            #Tests if the word ends next to another word or at end of board
            if valid:
                if xl-1<=14 and board[xl,y]=='_':
                    valid=True
                elif xl-1==15:
                    valid=True
                else:
                    valid=False
                
    except AssertionError as msg:
        print(msg)
        valid = False
    except:
        print('Unknown Error')
        valid=False
    finally:
        return valid


###Function to lay tiles on the board
###Accepts a direction, coordinates, previous word
###New word, board, and tile set
def layTiles(d,x,y,word,oword,board,myTiles):
    #Counts wilds
    wild=myTiles.count('')

    #Sets counter
    count = 0
    
    remTiles=myTiles.copy() # Creates a copy of myTiles

    y=COLUMNS[y.upper()] #Looks up integer for coordinate Y

    xl=x+len(word) #Sets the end of the word range
    yl=y+len(word)
    
    x=int(x) #Makes sure x is in int type
    
    total_words=[word] #Creates a list of words found during laying of tiles
    score=0 #Set score for turn to 0

    #Begin Try Statement
    try:
        #Checks if D has an extra value indicating first turn
        if len(d)>1 and d[0].upper()=='H':
            assert 'X' in board[x,y:yl], 'First turn must play at center'
            d='H'
            print(d)
        elif len(d)>1 and d[0]=='V':
            assert 'X' in board[x:xl,y], 'First turn must play at center'
            d='V'
            print(d)

        #If d is not bigger then 1, play as normal
        else:
            assert checkBoard(d,x,y,word,np.copy(board)), "Invalid word placement!"  #Asserts that the word can be played at location
            
        assert checkBoardTiles(d,x,y,word,board,myTiles), "Tile Error!" #Asserts you have the tiles in your set

        #Begin Laying tiles
        #Check Direction first
        if d.upper() == 'H':
            for char in word:

                #checks for Perpindicular words and adds them to a set if valid.
                temp,perp_word=checkPerpWordH(x,y,word,board)
                total_words.append(perp_word)

                #If the character is already layed, iterate column
                if board[x,y]==char.upper():
                    y+=1

                #If the board is blank here, lay down the tile
                else:
                    board[x,y]=char.upper()  #Tile is placed
                    if char.upper() not in remTiles and wild>0: #Checks for use of wild.
                        remTiles.remove('') #Remove Wild
                        remTiles.append(char.upper()) #Change wild for character requested
                        wild-=1 #Remove wild from count
                    remTiles = removeTiles(char, remTiles) #Clear used tiles
                    y+=1 #Iterate Column
                    
        #Begin Vertical loop
        elif d.upper() == 'V':
            for char in word:
                
                #checks for Perpindicular words and adds them to a set if valid.
                temp,perp_word=checkPerpWordV(x,y,word,board)
                total_words.append(perp_word)

                #If tile exists, iterate row
                if board[x,y]==char.upper():
                    x+=1

                #If the board is blank here, lay down the tile
                else:
                    board[x,y]=char.upper() #Place tile
                    if char.upper() not in remTiles and wild>0: #Confirm use of wild
                        remTiles.remove('')
                        remTiles.append(char.upper())
                        wild-=1
                    remTiles = removeTiles(char, remTiles) #remove used tiles
                    
                    x+=1 #iterate row

        #Get the score for all words created
        total_words.remove(oword) #Remove previous word
        for w in total_words:
            score=score+getWordScore(w)
            
        success=True  #If all the above ran, return True

    #Catch Assertion errors and print feedback
    except AssertionError as msg:
        print(msg)
        success=False

    #Catch Index errors in case of word length
    except IndexError:
        print('The word is too long for the board!')
        success=False
    #Catch all
    except:
        print('Unknown Error')
        success=False

    #Finally return the board, bool, newtile set, and the score
    finally:
        return (board, success, remTiles.copy(),score)


###Function that checks the tiles laid on the board + user tiles
###Confirms if a word can be formed.
def checkBoardTiles(d,x,y,word,board,myTiles):
    char_list=[] #create list to hold extra tiles

    #Begin Test loop
    if d.upper()=='H':
        for char in word:
            if board[x,y]==char.upper(): #if the tile is already laid
                char_list.append(char)   #append to char_list
                y+=1
            else:
                y+=1
    elif d.upper()=='V':
        for char in word:
            if board[x,y]==char.upper():#if the tile is already laid
                char_list.append(char)  #append to char_list
                x+=1
            else:
                x+=1
                
    #remove any characters found in char list and the word.
    for char in char_list:
        word=word.replace(char,'')

    if checkTiles(word, myTiles.copy()):
        return True
    else:
        return False
                
###Checks if there is a perpindicular word
def checkPerpWordH(x,y,word,board):
    test_word='' #Create a placeholder string
    
    if board[x+1,y] != '_' or board[x-1,y] != '_': #If either above or below word is not blank, run through
        lowx=x #Sets initial value for lower range
        highx=x #sets initial value for higher range

        #Get the lowest range row
        if board[lowx,y]!='_':
            
            #Continues to drop x lower until we hit a blank
            while board[lowx,y] != '_':
                lowx-=1
            
            lowx+=1 #Compinsate for the while until lowx is blank

        #Now iterate until highx is found
        while board[highx,y]!='_':
            highx+=1

        #Now pull out the word from the board    
        for r in range(lowx,highx):
            test_word=test_word+board[r,y]
            
        #Test if the perp word is in the dictionary.
        if isValid(test_word,[],dictionary):
            return (True,test_word)
        else:
            return (False,test_word)

    #if no perp words, return true and blank string
    else:
        return (True,test_word)


##Works exactly like checkPerpWordH but for vertical words.
def checkPerpWordV(x,y,word,board):
    test_word=''
    if board[x,y+1] != '_' or board[x,y-1] != '_':
        lowy=y
        highy=y
        if board[x,lowy]!='_':
            while board[x,lowy] != '_':
                lowy-=1
            lowy+=1
        while board[x,highy]!='_':
            highy+=1

        for r in range(lowy,highy):
            test_word=test_word+board[x,r]

        if isValid(test_word,[],dictionary):
            return (True,test_word)
        else:
            return (False,test_word)
    else:
        return (True,test_word)
        

###Constants###
BOARD,COLUMNS=createBoard()
dictionary=readFile('dictionary.txt')
