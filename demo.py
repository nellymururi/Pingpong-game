#Pong game
import turtle
import random


#Setup the screen
wn = turtle.Screen()
wn.title("MyfirstPong game")
wn.bgcolor("black") #background color
wn.setup(width = 800, height =600)   #(x_size,y_size)
wn.tracer(0)#no animation

#Score
score_a=0
score_b=0

#Paddle 1
paddle_one=turtle.Turtle()    #create a new Turtle object called paddle one and assign it to variable paddle_one
paddle_one.speed(50)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.shapesize(stretch_wid=5,stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350,0)

#Paddle 2
paddle_two=turtle.Turtle()    #create a new Turtle object called paddle one and assign it to variable paddle_one
paddle_two.speed(50)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5,stretch_len=1)
paddle_two.penup()
paddle_two.goto(350,0)

"""
#Paddle 3
paddle_three=turtle.Turtle()    #create a new Turtle object called paddle one and assign it to variable paddle_one
paddle_three.speed(50)
paddle_three.shape("square")
paddle_three.color("white")
paddle_three.shapesize(stretch_wid=5,stretch_len=1)
paddle_three.penup()
paddle_three.goto(0,300)
"""

#Ball
ball=turtle.Turtle()   
ball.speed(2)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
#ball.dx=0.1
#ball.dy=-0.1
#Code suggestion from Chat gpt
# Initialize ball's movement with a random direction
initial_dx = random.choice([-0.1, 0.1])
initial_dy = random.choice([-0.1, 0.1])
ball.dx = initial_dx
ball.dy = initial_dy

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)



#Function for movement for paddle one
#Going up
def paddle_one_up():
    y=paddle_one.ycor()
    y +=20
    paddle_one.sety(y)

#Going down
def paddle_one_down():
    y=paddle_one.ycor()
    y -=20
    paddle_one.sety(y)


#Keyboard binding
wn.listen()#listens to keyboard input
wn.onkeypress(paddle_one_up,"7")#Should be able to go up when + is pressed,and calls the function paddle_one_up
wn.onkeypress(paddle_one_down,"1")#Should be able to go down when - is pressed and calls the function paddle_one_down

#Function for movement for paddle two
#Going up
def paddle_two_up():
    y=paddle_two.ycor()
    y +=20
    paddle_two.sety(y)

#Going down
def paddle_two_down():
    y=paddle_two.ycor()
    y -=20
    paddle_two.sety(y)

  #Keyboard binding
wn.listen()#listens to keyboard input
wn.onkeypress(paddle_two_up,"9")#Should be able to go up when + is pressed,and calls the function paddle_one_up
wn.onkeypress(paddle_two_down,"3")#Should be able to go down when - is pressed and calls the function paddle_one_down  

#Main game loop
while True:
    wn.update()
    

    #Move the ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor()+ball.dy)

   
    #Border checking
    if (ball.ycor()>290):
        ball.sety(290)#Bounce off of top border
        ball.dy*=-1

    if  (ball.ycor()<-290):
        ball.sety(-290)#Bounce off of bottom border
        ball.dy*=-1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a +=1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a,score_b),align="center",font=("Arial",20,"normal"))
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b +=1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a,score_b),align="center",font=("Arial",20,"normal"))

#Paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_two.ycor() +40 and ball.ycor() >paddle_two.ycor() -40 ):
     ball.setx(340)
     ball.dx *=-1
    
    if (ball.xcor() <-340 and ball.xcor() >-350) and (ball.ycor() <paddle_one.ycor() +40 and ball.ycor() >paddle_one.ycor()-40 ):
      ball.setx(-340)
      ball.dx *=-1


        
         




