###Scrabble Game###
##Zachary Larsen###
##24-11-2020##


###Import all functions, numpy, and main_loop functions
from functions import *
import numpy as np
from main_loop import *


Dictionary=readFile('dictionary.txt') #Read in the dictionary into a list

#Program Introduction
print('Welcome to ScrabblePy!')

#Set initial tiles and variables
myTiles=randTiles([''])
main_loop = 'Y'
count=0
totalscore=0

#Begin Main User loop
while main_loop.upper() == 'Y':

    main_loop=input('Would you like to play a word?: (Y|N)')
    
    if main_loop.upper() == 'Y':

        #Test if the user would like to change any tiles
        myTiles=tileChangeLoop(myTiles)

        #Will print board after tile loop
        print(BOARD)

        #Get the Users word
        user_word=getUserWord(myTiles,Dictionary)

        #Get coordinates from the user
        d,x,y=getCoord()

        #test if this is the first turn                            
        if count < 1:

            d=d.upper()+'1'#Adds 1 to d to signal first turn
            BOARD,success,myTiles,score = layTiles(d,x,y,user_word,'',BOARD,myTiles) #Go to main layTile function

            #If word laid successfully, move to next turn
            if success:
                count+=1
                run=False

            #User must start over but it will not move to second turn
            else:
                print("Make sure your first play goes through the centre.")
                run=False
                continue
            
        #Play any other turn
        else:
            BOARD,success,myTiles,score = layTiles(d,x,y,user_word,old_word,BOARD,myTiles)
            run=False

        #Print board again after turn regardless of success
        #print(BOARD)

        #If successful do the below
        if success:
            myTiles=randTiles(myTiles) #Refill Tiles
            totalscore=totalscore+score #Add score to total
            old_word=user_word.upper() #get old word set for next turn
            print(BOARD)
            print("\'" + user_word + "\' gives you " + str(getWordScore(user_word)) + " Points!")
            print("Your total score is " + str(totalscore))

    #If user chooses to quit, display final score and exit       
    elif main_loop.upper() == 'N':
        print('Your final score was ' + str(totalscore) + '!')
        print('Thank you for Playing!')
        input('Press enter to exit...')
        #print('Goodbye!')
        break

    #Test if Y or N weren't used.
    else:
        print("\nPlease enter Y or N\n")
        main_loop='Y'
        continue

