game_not_over=True
current_row=5
turn=0
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


def bottom_is_filled(column):

    if board[current_row][column-1]==1 or board[current_row][column-1]==2:
        return True


def wincheck(column, player):
    j=0
    for i in range(0,len(board)):
        for j in range(0, len(board[0])-3):
            if(board[i][j]==player and board[i][j+1]==player and board[i][j+2]==player and board[i][j+3]==player):
                return True
    for i in range(0,len(board)-3):
        for j in range(0, len(board[0])):
            if(board[i][j]==player and board[i+1][j]==player and board[i+2][j]==player and board[i+3][j]==player):
                return True
    for i in range(0,len(board)-3):
        for j in range(0, len(board[0])-3):
            if(board[i][j]==player and board[i+1][j+1]==player and board[i+2][j+2]==player and board[i+3][j+3]==player):
                return True
            if(board[i+3][j]==player and board[i+2][j+1]==player and board[i+1][j+2]==player and board[i][j+3]==player):
                return True
    return False        


def transpose(l1): 
    l2=[]
    for i in range(len(l1[0])):
        row=[]
        for j in range(len(l1)):
            row.append(l1[j][i])
        l2.append(row)
    return l2


def change_bottom(column):
    boardTranspose=transpose(board)
    for i in boardTranspose[column-1]:
        if i ==1 or i==2:
            current_row=boardTranspose[column-1].index(i)-1
            return current_row

while game_not_over:
    
    if turn%2==0:
        c=int(input("Player 1 , enter column number: "))
        if bottom_is_filled(c):
            board[change_bottom(c)][c-1]=1
            print_board()
        else:
            board[5][c-1]=1
            print_board()

        if wincheck(c, 1):
            game_not_over = False
            print("Player 1 wins") 

    else:
        c=int(input("Player 2 , enter column number: "))
        if bottom_is_filled(c):
            board[change_bottom(c)][c-1]=2
            print_board()
        else:
            board[5][c-1]=2
            print_board()
        
        if wincheck(c, 2):
            game_not_over = False
            print("Player 2 wins")
   
    turn+=1

    
