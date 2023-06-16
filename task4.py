# Zachary Larsen
# CW1102 CW2
# Task 4
##Program takes a word and provides a scrabble score

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




main_loop = 'Y'

##Send some test data
print('This program returns the score of a word.\nHere is some Test Data!\n')
test_data = ['Programming', 'Python', 'Reza', 'Leicester', '3numbers', 82, 'Rez@', 'Test Word']

print("For the below words, we get the following Scores:\n")
for i in range(0,len(test_data)):
    if getWordScore(test_data[i]):
        print("For \'" + str(test_data[i]) + "\' we get: " + str(getWordScore(test_data[i])) + " Points!\n")
    else:
        print("\'" + str(test_data[i]) + "\' is not a valid word!\n")

##End Test Data

##Begin main user loop
while main_loop.upper() == 'Y':
    main_loop=input('Would you like to get the score of another word?: (Y|N)')


    if main_loop.upper() == 'Y':

        #Get User input and test    
        user_word=input('Please enter a word: ')
        print('\n')

        #Tests user input and prints score if word is valid.
        if getWordScore(user_word):
            print("For the word \'" + user_word.upper() + "\' you get a score of \'" + str(getWordScore(user_word)) + "\'!\n")
        else:
            print("\'" + user_word.upper() + "\' is not a valid word.\n")

    elif main_loop.upper() == 'N':
        print('Goodbye')
        break
    else:
        print('\nPlease enter a Y or N\n')
        main_loop='Y'
        continue

