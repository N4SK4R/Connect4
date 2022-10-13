game_not_over=True
current_row=5
turn=0
board=[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],]

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


def change_bottom(column):
    boardTranspose=transpose(board)
    for i in boardTranspose[column-1]:
        if i ==1 or i==2:
            current_row=boardTranspose[column-1].index(i)-1
            return current_row

while game_not_over:
    
    if turn%2==0:
        c=int(input("Player 1 , enter column number: "))
        if bottom_is_fillled(c):
            board[change_bottom(c)][c-1]=1
            print_board()
        else:
            board[5][c-1]=1
            print_board()
    else:
        c=int(input("Player 1 , enter column number: "))
        if bottom_is_fillled(c):
            board[change_bottom(c)][c-1]=2
            print_board()
        else:
            board[5][c-1]=2
            print_board()
    turn+=1