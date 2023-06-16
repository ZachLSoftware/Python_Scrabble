from validation_functions import *
from board_functions import *
from tile_functions import *


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
