GameNotOver=True
current_row=5
turn=0
winner=1
board=[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]

def print_board():
    
    for i in board:
        for j in i:
            print(j,end=" ")
        print()

def bottom_is_fillled(column):
    if board[current_row][column-1]==1 or board[current_row][column-1]==2:
        return True
    
def transpose(l1): 
    l2=[]
    for i in range(len(l1[0])):
        row=[]
        for j in range(len(l1)):
            row.append(l1[j][i])
        l2.append(row)
    return l2

def wincheck(symbol):
    global GameNotOver
    global winner
    j=0
    for i in range(0,len(board)):
        for j in range(0, len(board[0])-3):
            if((board[i][j] == symbol) and (board[i][j+1] == symbol) and (board[i][j+2] == symbol) and (board[i][j+3] == symbol)):
                winner=symbol
                GameNotOver=False
    for i in range(0,len(board)-3):
        for j in range(0, len(board[0])):
            if((board[i][j] == symbol) and (board[i+1][j] == symbol) and (board[i+2][j] == symbol) and (board[i+3][j] == symbol)):
                winner=symbol
                GameNotOver=False
    for i in range(0,len(board)-3):
        for j in range(0, len(board[0])-3):
            if((board[i][j] == symbol) and (board[i+1][j+1] == symbol) and (board[i+2][j+2] == symbol) and  (board[i+3][j+3] == symbol)):
                winner=symbol
                GameNotOver=False
            if((board[i+3][j] == symbol) and (board[i+2][j+1] == symbol) and (board[i+1][j+2] == symbol) and (board[i][j+3] == symbol)):
                winner=symbol
                GameNotOver=False  

def change_bottom(column):
    boardTranspose=transpose(board)
    for i in boardTranspose[column-1]:
        if i ==1 or i==2:
            current_row=boardTranspose[column-1].index(i)-1
            return current_row

while GameNotOver:
    
    if turn%2==0:
        c=int(input("Player 1 , enter column number(1-7): "))
        if bottom_is_fillled(c):
            board[change_bottom(c)][c-1]=1
            print_board()
        else:
            board[5][c-1]=1
            print_board()
            
        wincheck(1)
    else:
        c=int(input("Player 2 , enter column number(1-7): "))
        if bottom_is_fillled(c):
            board[change_bottom(c)][c-1]=2
            print_board()
        else:
            board[5][c-1]=2
            print_board()
            
        wincheck(2)
            
    turn+=1

print("The Winner is Player",winner)