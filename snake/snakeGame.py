import random
from tkinter import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCORE = 0
BODY_SIZE = 10
SNAKE_COLOUR ="blue"
SNAKE_FOOD = "purple"

def food():
    x = random.randint(0,30-1)*BODY_SIZE
    y = random.randint(0,30-1)*BODY_SIZE
    canvas.create_rectangle (x,y,x+BODY_SIZE,y+BODY_SIZE,fill="GOLD")
    
def update():
    food()
    SNAKE_VELOCITY_X = 0
    SNAKE_VELOCITY_Y = 0
    snakeX = 0
    snakeY = 0
    snakeX = snakeX + SNAKE_VELOCITY_X
    snakeY = snakeY + SNAKE_VELOCITY_Y
    snakeHandle = canvas.create_rectangle (snakeX,snakeY,snakeX+BODY_SIZE,snakeY+BODY_SIZE,fill="blue")


    
    
master =Tk()
master.geometry("%sx%s"%(SCREEN_WIDTH,SCREEN_HEIGHT))
labelName= Label(master, text="A python game!", font= ('Courier 10 underline'))
labelScore = Label(master, text="%s"%(SCORE), font=('Courier 10')) 
labelName.pack()
labelScore.pack()
canvas = Canvas(master, bg="black",width=300,height=300)
canvas.pack()


def right_direction(event):
    SNAKE_VELOCITY_X = 1
    SNAKE_VELOCITY_Y = 0
    # canvas.move(snakeHandle)
def left_direction(event):
    SNAKE_VELOCITY_X = -1
    SNAKE_VELOCITY_Y = 0
    print(SNAKE_VELOCITY_X)
def up_direction(event):
    SNAKE_VELOCITY_X = 0
    SNAKE_VELOCITY_Y = 1
    print(SNAKE_VELOCITY_Y)
def down_direction(event):
    SNAKE_VELOCITY_X = 0
    SNAKE_VELOCITY_Y = -1
    print(SNAKE_VELOCITY_Y)

master.bind("<Right>", right_direction)
master.bind("<Left>", left_direction)
master.bind("<Up>", up_direction)
master.bind("<Down>", down_direction)

update()    

master.mainloop()
