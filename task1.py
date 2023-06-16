# Zachary Larsen
# CW1102 CW2
# Task 1


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
        print("There was an error reading the file %s." % name)
    except:
        print("An unexpected error occured")
    finally:
        f.close()

##Read each file into a variable and show output
print('Reading dictionary.txt...\n')
Dictionary=readFile('dictionary.txt')
if Dictionary:
    print('Dictionary.txt contains ' + str(len(Dictionary)) + ' Words.\n')
else:
    print('Error Reading File...\n')
    
print('Reading scores.txt...\n')
Scores=readFile('scores.txt')
if Scores:
    print('Scores.txt contains \n' +str(Scores) + '\n')
else:
    print('Error Reading File...\n')
    
print('Reading tiles.txt...\n')
Tiles=readFile('tiles.txt')
if Tiles:
    print('tiles.txt contains \n' + str(Tiles) + '\n')
else:
    print('Error Reading File')

input('Press enter to end...')
