###Main Loop Functions###
from functions import *

def tileChangeLoop(tiles):
    myTiles=tiles.copy()
    #Displays current tile set and gives user option to generate new set.
    print('\nThe Tiles you have are: ' + str(myTiles) + '\n')
    changeTile='Y'
    skip=False
    while changeTile.upper()=='Y':
        try:
            if not skip:
                changeTile=input('Would you like to change any tiles? Y or N: ')
            if changeTile.upper()=='Y':
                #myTiles = randTiles([])
                num=input('How many tiles do you want to replace? ')
                assert num.isdigit(), "Enter a number of tiles to replace."
                num=int(num)
                assert num >=0 and num<=7, "Enter a number between 1-7."
                if num==7:
                    myTiles=randTiles([])
                elif num==0:
                    changeTile='N'
                    continue
                else:
                    myTiles=changeTiles(num,myTiles)
                print('\n' + str(myTiles) + '\n')
                skip=False
            elif changeTile.upper()=='N':
                break
            else:
                print('\nPlease enter a Y or N\n')
                changeTile='Y'
                continue
        except AssertionError as msg:
            print(msg)
            changeTile='Y'
            skip=True

    return myTiles.copy()

def getUserWord(myTiles,dictionary):
    run=True
    
        #Get User data and test
    while run:
        try:
            #Display Current Tile set again before getting user input
            print('\nThe Tiles you have are: ' + str(myTiles) + '\n')
            user_word=input('Please enter a word: ')
            print('\n')
            assert isValid(user_word,myTiles,dictionary)
            print("YES! \'" + user_word.upper() + "\' is a valid word!\n")
            run=False
        except AssertionError:
            run=True
            print("No! \'" + user_word.upper() + "\' is not a valid word.\n")
            myTiles=tileChangeLoop(myTiles)
    return user_word


def getCoord():
    run=True
    while run:
        try:
            d=input('Enter direction (H|V): ')
            coord=input('Enter starting column Starting Row (A-0)(1-15):')
            assert len(coord)>=2 and len(coord)<=3, "Please enter a valid coordinate.\n"
            if len(coord)==2:
                x=coord[1]
            else:
                x=coord[1:3]
            y=coord[0]
            assert x.isdigit(), "Please enter a valid Row Number."
            assert y.isalpha(), "Please Enter a valid Column Letter."
            x=int(x)
            assert d.upper() == 'H' or d.upper() == 'V', "Enter H or V.\n"
            assert y.upper() in COLUMNS, "Column out of Range.\n"
            assert x>=1 and x<=15, "Row out of Range.\n"
            run=False
        except AssertionError as msg:
            print(msg)
            run==True
    return (d,x,y)




    
