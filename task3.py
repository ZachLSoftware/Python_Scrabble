# Zachary Larsen
# CW1102 CW2
# Task 3
##Program takes a letter and provides a scrabble score

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
    
    Scores=readFile('scores.txt') #Read in scores.txt
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
    

main_loop = 'Y'

##Send some test data
print('This program returns the score of a letter.\nHere is some Test Data!\n')

test_data=['R', 'e', 'z', 'a', '3', 82, 'Reza', 'Test Word']
print('If the input is correct, we will receive a score value, otherwise we receive 0')
print("For below inputs we get the following:\n")

for i in range(0,len(test_data)):
    print("For \'" + str(test_data[i]) + "\' we get: " + str(getLetterScore(test_data[i])) + " Points!\n")
##End Test Data

#Begin Main Loop for User interaction
while main_loop.upper() == 'Y':
    main_loop=input('Would you like to see the score of a letter?: (Y|N)')

    #Confirm user choice, confirm y or n, and break if n
    if main_loop.upper() == 'Y':
        
    #Get User Input and Test 
        user_letter=input('Please enter a letter: ')
        print('\n')

        #Test user's letter, if 0 is returned, we get the else statement.
        if getLetterScore(user_letter):
            print('For the letter \'' + user_letter.upper() + '\' you would receive ' + str(getLetterScore(user_letter)) + ' points!\n')
        else:
            print('You did not enter a valid letter.\n')
        continue

    elif main_loop.upper() == 'N':
        break
    else:
        print("\nPlease enter Y or N \n")
        main_loop='Y'
        continue



