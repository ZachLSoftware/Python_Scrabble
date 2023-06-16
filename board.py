###Board Functions###

def createBoard():
    board = np.zeros((17,17),'U2')
    board.fill('_')
    alpha='A'
    #upper_board = []
    for i in range(1,16):
        board[0][i]=alpha
        board[16][i]=alpha
        board[8][8]='X'
        if len(str(i)) < 2:
            board.T[0][i]=' ' + str(i)
            board.T[16][i]=' ' + str(i)
        else:
            board.T[0][i]=str(i)
            board.T[16][i]=str(i)
        alpha = chr(ord(alpha)+1)
    board[0][0] = board[0][16]=board[16][0]=board[16][16]='  '
    return board


def layTilesFirstTurn(d,x,y,word,board,myTiles):
    alpha ='A'
    count = 0
    remTiles=myTiles.copy()
    while y.upper() != alpha:
        alpha = chr(ord(alpha)+1)
        count += 1
    y=count+1
    x=int(x)
    xl=x+len(word)
    yl=y+len(word)
    try:
        #assert checkBoard(d,x,y,word,board), 'Invalid word placement!'
        if d.upper() == 'H':
            assert 'X' in board[x,y:yl], 'First turn must play at center'
            for char in word:
                board[x,y]=char.upper()
                remTiles = removeTiles(char, remTiles)
                y+=1
        elif d.upper() == 'V':
            assert 'X' in board[x:xl,y], 'First turn must play at center'
            for char in word:
                board[x,y]=char.upper()
                remTiles = removeTiles(char, remTiles)
                x+=1
        success=True
    except AssertionError as msg:
        print(msg)
        success=False
    except:
        print('Unknown Error')
        success=False
    finally:
        return (board, success, remTiles)

def layTiles(d,x,y,word,board,myTiles):
    alpha ='A'
    count = 0
    remTiles=myTiles.copy()
    while y.upper() != alpha:
        alpha = chr(ord(alpha)+1)
        count += 1
    y=count+1
    x=int(x)
    try:
        assert checkBoard(d,x,y,word,board), "Invalid word placement!"
        assert checkBoardTiles(d,x,y,word,board,myTiles), "Tile Error!"
        if d.upper() == 'H':
            for char in word:
                if board[x,y]==char.upper():
                    y+=1
                else:
                    board[x,y]=char.upper()
                    remTiles = removeTiles(char, remTiles)
                    y+=1
        elif d.upper() == 'V':
            for char in word:
                if board[x,y]==char.upper():
                    x+=1
                else:
                    board[x,y]=char.upper()
                    remTiles = removeTiles(char, remTiles)
                    x+=1
        success=True
    except AssertionError as msg:
        print(msg)
        success=False
    except:
        print('Unknown Error')
        success=False
    finally:
        return (board, success, remTiles)



