##Tile Functions##
from board_functions import *
from validation_functions import *
from main_functions import *


#Generate random tile list
#Pulls from Global Variable tiles and returns a list
def randTiles(myTiles):
    Tiles=readFile('tiles.txt')
    newTiles = myTiles.copy()
    while len(newTiles) < 7:
        newTiles.append(Tiles[random.randrange(0,len(Tiles))])  #Uses the global Variable read in from Task1 Tiles to pull 7 random tiles.
    return newTiles
                                

                                        
    except TypeError:
        print("Exception: The Word Contains Non-Alphabetic Character!")
        return False

    except AssertionError as msg:
        print(msg)
        return False
    
    return True  #Return True if all characters found in myTiles
def removeTiles(word, myTiles):
    remTiles=myTiles.copy()
    for char in word:
        remTiles.remove(char.upper())
    return remTiles

def changeTiles(num, myTiles):
    word=''
    try:
        for x in range(0,num):
            run=True
            while run:
                y=input('Which tile would you like to replace? ')
                if y.upper() in myTiles:
                    word=word+y
                    run=False
                else:
                    print('\nThat is not in your tiles.\n')
                    run=True
        print(word)
        newTiles=removeTiles(word,myTiles)
        newTiles=randTiles(newTiles)
        return newTiles
    except ValueError:
        print('Value Error')
