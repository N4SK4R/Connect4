import pygame
from pygame import mixer
pygame.init()

SCREEN_SIZE=(0,0)#For Fullscreen
screen=pygame.display.set_mode(SCREEN_SIZE)
mixer.music.load("Audio/bgm.mp3")
mixer.music.play(-1)
WindowRunning=True
GameNotOver=True
turn=0
#Starting postion of Coin
x=690
y=0

tileMap=[[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

#Loading Images
bg=pygame.image.load("Images/SpaceBackground.png")
EmptyCell=pygame.image.load("./Images/SpaceEmptyCell.png")
EmptyCell.set_alpha()
redcoin=pygame.image.load("./Images/SpaceRedCell.png")

greencoin=pygame.image.load("./Images/SpaceGreenCell.png")
Endtitle1=pygame.image.load("./Images/GameOver1.png")
Endtitle2=pygame.image.load("./Images/GameOver2.png")


Display = pygame.Surface([1240,800 ], pygame.SRCALPHA, 32)
Display = Display.convert_alpha()

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
    j=0
    for i in range(0,len(tileMap)):
        for j in range(0, len(tileMap[0])-3):
            if((tileMap[i][j] == symbol) and (tileMap[i][j+1] == symbol) and (tileMap[i][j+2] == symbol) and (tileMap[i][j+3] == symbol)):
                GameNotOver=False
    for i in range(0,len(tileMap)-3):
        for j in range(0, len(tileMap[0])):
            if((tileMap[i][j] == symbol) and (tileMap[i+1][j] == symbol) and (tileMap[i+2][j] == symbol) and (tileMap[i+3][j] == symbol)):
                GameNotOver=False
    for i in range(0,len(tileMap)-3):
        for j in range(0, len(tileMap[0])-3):
            if((tileMap[i][j] == symbol) and (tileMap[i+1][j+1] == symbol) and (tileMap[i+2][j+2] == symbol) and  (tileMap[i+3][j+3] == symbol)):
                GameNotOver=False
            if((tileMap[i+3][j] == symbol) and (tileMap[i+2][j+1] == symbol) and (tileMap[i+1][j+2] == symbol) and (tileMap[i][j+3] == symbol)):
                GameNotOver=False  
    
def player():
    if turn%2==0:
        
        return 'r'
    else:
        return 'g'
            
def columnNo(x):
    x=x/200
    x=int(x)
    return x

def drop(columnNumber):
    #animate(columnNumber,player())
    current_row=change_row(columnNumber)
    if player()=='r':    
        tileMap[current_row][columnNumber]='r'
    else:
        tileMap[current_row][columnNumber]='g'
        
def animate(num,player):
    for i in range(change_row(columnNo(x))):
       tileMap[i][num]=player
    #    pygame.time.delay(250)
       tileMap[i][num]=0
       

def change_row(column):
    tileMapTranspose=transpose(tileMap)
    for i in tileMapTranspose[column]:
        if i =='r' or i=='g':
            current_row=tileMapTranspose[column].index(i)-1
            return current_row    
    return 5
    
while WindowRunning:
    
    screen.blit(bg,(0,0))
    screen.blit(Display,(150,120))
    if player()=='r':
        screen.blit(redcoin,(x,y))
    else:
        screen.blit(greencoin,(x,y))
    
    Y=0
    for row in tileMap:
        X=0
        for cell in row:
            if cell==0:
                Display.blit(EmptyCell,(X*180,Y*130))
            elif cell=='r':
                Display.blit(redcoin,(X*180,Y*130))            
            else:
                Display.blit(greencoin,(X*180,Y*130))
            X+=1
        Y+=1
    
    for event in pygame.event.get():
        key=pygame.key.get_pressed()
        if GameNotOver:
            if event.type==pygame.KEYDOWN:
                if key[pygame.K_d] or key[pygame.K_RIGHT]:
                    x+=180
                
                if key[pygame.K_a] or key[pygame.K_LEFT]:
                    x-=180
                
                if key[pygame.K_SPACE] or key[pygame.K_DOWN]:
                    pop=mixer.Sound("Audio/pop.wav")
                    pop.play()
                    drop(columnNo(x))
                    wincheck(player())    
                    turn+=1
                
            
        if key[pygame.K_ESCAPE]:
            WindowRunning=False    
            
    if not GameNotOver:
        if player()=='r':    
            screen.blit(Endtitle2,(455,350)) 
        else:
            screen.blit(Endtitle1,(455,350))     
    pygame.display.flip()
    
pygame.quit()