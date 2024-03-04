import socket
import pygame
from _thread import *
import ssl

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"./keys/server_cert.pem", keyfile=r"./keys/server_key.pem")

server_socket.listen(2)
    
pygame.init()
SCREEN_SIZE=(0,0)#For Fullscreen
screen=pygame.display.set_mode(SCREEN_SIZE)
WindowRunning=True
GameNotOver=True
data_received=None
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


def drop(columnNumber):
    current_row=change_row(columnNumber)
    if player()=='r':    
        tileMap[current_row][columnNumber]='r'
    else:
        tileMap[current_row][columnNumber]='g'

def change_row(column):
    tileMapTranspose=transpose(tileMap)
    for i in tileMapTranspose[column]:
        if i =='r' or i=='g':
            current_row=tileMapTranspose[column].index(i)-1
            return current_row    
    return 5

def threaded_client1():
    global data_received
    while True:
        
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        ssl_client_socket = ssl_context.wrap_socket(client_socket, server_side=True)
        while True:
            data_received = ssl_client_socket.recv(1024).decode("utf8")
                
def threaded_client2():
    global data_received
    while True:
        
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        ssl_client_socket = ssl_context.wrap_socket(client_socket, server_side=True)
        while True:
            data_received = ssl_client_socket.recv(1024).decode("utf8")
            
start_new_thread(threaded_client1,())
start_new_thread(threaded_client2,())

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
    
    if GameNotOver:
        if data_received:
            print(data_received, "Player",player())
            drop(int(data_received))
            wincheck(player())    
            data_received=None
            turn+=1
                              
    if not GameNotOver:
        if player()=='r':    
            screen.blit(Endtitle2,(455,350)) 
        else:
            screen.blit(Endtitle1,(455,350))     
    pygame.display.flip()
    
pygame.quit()