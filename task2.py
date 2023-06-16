# Zachary Larsen
# CW1102 CW2
# Task 2
##Program validates a word only uses letters from the alphabet.

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
        print(msg)
        return False

    return True   #If all letters were in the alphabet, the loop ends and returns True


#Program Introduction
print("""##This programm tests a single word and makes sure it
only contains English Characters.\nFor Example:##  \n""")


##Send Test Data##
print('For the word HELLO we get ' + str(onlyEnglishLetters('HELLO'))+'\n')
print('For the word HE LLO we get ' + str(onlyEnglishLetters('HE LLO'))+'\n')
print('For the word HE3LLO we get ' + str(onlyEnglishLetters('HE3LLO')) + '\n')
##End Test Data##

##Begin Main User Loop
main_loop = 'Y'
while main_loop.upper() == 'Y':
        
        #Test for user input loop   
        main_loop=input('Would you like to test another word?: (Y|N)')
        if main_loop.upper()=='Y':

            #Get User Input and Test
            user_word=input('Please enter a word: ')
            print('\n')

            #Check if word only uses english letters
            if onlyEnglishLetters(user_word):
                print('\"' + user_word.upper() + '\" only uses English Letters!\n')
            else:
                print('\"' + user_word.upper() + '\" has invalid characters!\n')

        #Break block and data validation    
        elif main_loop.upper() == 'N':
            print('Goodbye!')
            break
        else:
            print("\nPlease enter Y or N \n")
            main_loop='Y'
            continue
