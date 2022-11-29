
#Import the required modules
import turtle

#Create the game screen
windw = turtle.Screen()
windw.title("Ping Pong Game Turtle vs Panda")
windw.bgcolor("green")
windw.setup(width=1000, height=800)
windw.tracer(0)

#Create the score to count scores
score_right = 0
score_left = 0

#Create the left paddle of the game
player_turtle = turtle.Turtle()
player_turtle.speed(1)
player_turtle.shape("square")
player_turtle.shapesize(stretch_wid=5, stretch_len=1)
player_turtle.color("black")
player_turtle.penup()
player_turtle.goto(-(windw.window_width()/2 + 50), 0)

#Create the right paddle of the game
player_panda = turtle.Turtle()
player_panda.speed(1)
player_panda.shape("square")
player_panda.shapesize(stretch_wid=5, stretch_len=1)
player_panda.color("black")
player_panda.penup()
player_panda.goto((windw.window_width()/2 - 50), 0)

#Creating the white ball
ball = turtle.Turtle()
ball.speed(8)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

#Creating the pen to record players' scores
records_pos = 260

pen = turtle.Turtle()
pen.speed(1)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, records_pos)
pen.write("Player Panda: 0 Player Turtle: 0", align="center", font=("Courier", 28, "normal"))

#Creating function to play the game

def player_turtle_up():
    y = player_turtle.ycor()
    y += 20
    player_turtle.sety(y)

def player_turtle_down():
    y = player_turtle.ycor()
    y -= 20
    player_turtle.sety(y)

def player_panda_up():
    y = player_panda.ycor()
    y += 20
    player_panda.sety(y)

def player_panda_down():
    y = player_panda.ycor()
    y -= 20
    player_panda.sety(y)


#Creating the keyboard bindings to use when playing the game
windw.listen()
windw.onkeypress(player_turtle_up, "w")
windw.onkeypress(player_turtle_down, "s")
windw.onkeypress(player_panda_up, "Up")
windw.onkeypress(player_panda_down, "Down")


#Create the main game looping function
while True:
    windw.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Checking the border on top, bottom, rigt, and left
    if ball.ycor() > (records_pos - 20):
        ball.sety((records_pos - 20))
        ball.dy *= -1

    elif ball.ycor() < -(windw.window_height()/2 + 20):
        ball.sety(-(windw.window_height()/2 + 20))
        ball.dy *= -1

    if ball.xcor() > player_panda.pos()[0] + 100:
        score_left += 1
        pen.clear()
        pen.write("Player Turtle: {} Player Panda: {}".format(score_left, score_right), align="center", font=("Courier", 28, "normal"))
        ball.goto(0, 0)
        windw.delay(2000)
        ball.dx *= -1

    elif ball.xcor() < player_turtle.pos()[0] - 100:
        score_right += 1
        pen.clear()
        pen.write("Player Turtle: {} Player Panda: {}".format(score_left, score_right), align="center", font=("Courier", 28, "normal"))
        ball.goto(0, 0)
        windw.delay(2000)
        ball.dx *= -1

    #Paddle and the ball collisions solution
    if ball.xcor() < player_turtle.pos()[0] + 20 and ball.pos()[1] < player_turtle.pos()[1] + 50 and ball.pos()[1] > player_turtle.pos()[1] - 50:
        ball.setx(player_turtle.pos()[0] + 20)
        ball.dx *= -1

    elif ball.xcor() > player_panda.pos()[0] - 20 and ball.pos()[1] < player_panda.pos()[1] + 50 and ball.pos()[1] > player_panda.pos()[1] - 50:
        ball.setx(player_panda.pos()[0] - 20)
        ball.dx *= -1