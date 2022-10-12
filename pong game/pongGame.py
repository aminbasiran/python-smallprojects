import random
import turtle
import tkinter
# X_COORDINATES = 0
# Y_COORDINATES = 0

dx = 2
dy = 5
scoreA = 0
scoreB = 0


# master = turtle.Turtle()
master = turtle.Screen()  
# master2 = turtle.TurtleScreen(tkinter.Canvas)
# master = turtle.screensize(canvwidth=400,canvheight=400,bg="blue")  
master.title('my pong game')



master.setup(width=400,height=400)
# master.bgcolor("black")
# master.tracer(0)

# PADDLE A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('green')
paddleA.penup()
paddleA.goto(-170,0)
paddleA.shapesize(stretch_wid=2,stretch_len=1)

# PADDLE B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('purple')
paddleB.penup()
paddleB.goto(170,0)
paddleB.shapesize(stretch_wid=2,stretch_len=1)

# DRUNKBALL
drunk_ball= turtle.Turtle()
drunk_ball.speed(0)
drunk_ball.shape('square')
drunk_ball.color('blue')
drunk_ball.penup()
drunk_ball.goto(0,0)


# drunk_ball.forward(100)
# paddleA.shapesize(stretch_wid=1,stretch_len=1)

# def randomMovingDrunk_ball():
#     randomNumber1 = random.randint(0,100)

#     drunk_ball.forward()
#     drunk_ball.backward()


def goUp():
    
    Y_COORDINATES = paddleA.ycor()
    Y_COORDINATES = Y_COORDINATES + 20
    paddleA.sety(Y_COORDINATES)

    
def goDown():
    
    Y_COORDINATES = paddleA.ycor()
    Y_COORDINATES = Y_COORDINATES - 20
    paddleA.sety(Y_COORDINATES)

def goUpSecond():
    
    Y_COORDINATES = paddleB.ycor()
    Y_COORDINATES = Y_COORDINATES + 20
    paddleB.sety(Y_COORDINATES)

    
def goDownSecond():
    
    Y_COORDINATES = paddleB.ycor()
    Y_COORDINATES = Y_COORDINATES - 20
    paddleB.sety(Y_COORDINATES)

master.listen()
master.onkeypress(goUp,"w")
master.onkeypress(goDown,"s")
master.onkeypress(goUpSecond,"Up")
master.onkeypress(goDownSecond,"Down")


master.update()
while True:
    
    drunk_ball.setx(drunk_ball.xcor() + dx)
    drunk_ball.sety(drunk_ball.ycor() + dy)

# paddle A border 
    if paddleA.ycor() > 150:
        paddleA.sety(150)

    if paddleA.ycor() < -150:
        paddleA.sety(-150)

# paddle B border
    if paddleB.ycor() > 150:
        paddleB.sety(150)

    if paddleB.ycor() < -150:
        paddleB.sety(-150)

# drunk_ball y bounce 
    if drunk_ball.ycor() > 190:
        drunk_ball.sety(190)
        dy = dy *-1

    if drunk_ball.ycor() < -190:
        drunk_ball.sety(-190)
        dy = dy *-1  

# drunk_ball x bounce
    if drunk_ball.xcor() > 200:
        drunk_ball.goto(0,0)
        dx = dx *-1
        scoreA = scoreA +1
        print("Score A: " + str(scoreA))
     

    if drunk_ball.xcor() < -200:
        drunk_ball.goto(0,0)
        dx = dx *-1  
        scoreB = scoreB +1
        print("Score B: " + str(scoreB))  

# drunk_ball paddle A and B bounce
    if drunk_ball.xcor() < -150 and (drunk_ball.ycor() < paddleA.ycor()+20 and drunk_ball.ycor() > paddleA.ycor()-20):
        drunk_ball.setx(-150)
        dx = dx *-1

    if drunk_ball.xcor() > 150 and (drunk_ball.ycor() < paddleB.ycor()+50 and drunk_ball.ycor() > paddleB.ycor()-50):
        drunk_ball.setx(150)
        dx = dx *-1

    if scoreA==2 or scoreB ==2:
        exit()

    

   
        

    # if drunk_ball.ycor() < -190:
    #     drunk_ball.sety(-190)
    #     dy = dy *-1   


    

