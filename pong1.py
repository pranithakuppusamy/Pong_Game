import winsound
import turtle

wn=turtle.Screen()
wn.title("pong by @Pranitha")
wn.bgcolor("#000080")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball=turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy =-0.2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0    Player B:0",align="center",font=("Courier",20,"normal"))

#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboar binding
wn.listen()
wn.onkeypress(paddle_a_up,"1")
wn.onkeypress(paddle_a_down,"2")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
#main 
while True:
    wn.update()


    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1 
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",20,"normal"))
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",20,"normal"))
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)

    
    #paddle and ball collision
    if (ball.xcor()>340 and ball.xcor() < 350) and (ball.ycor()<paddle_b.ycor()+45and ball.ycor()>paddle_b.ycor()-45):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor() > -350) and (ball.ycor()<paddle_a.ycor()+45and ball.ycor()>paddle_a.ycor()-45):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
    
    if(score_a>9 and score_b<score_a):
        pen.clear()
        pen.write("Player A Wins ",align="center",font=("Courier",25,"bold"))
        score_b=-1
    if(score_b>9 and score_a<score_b):
        pen.clear()
        pen.write("Player B Wins",align="center",font=("Courier",25,"bold"))
        score_a=-1
    if(score_a==11 or score_b==11):
        break
        
   

