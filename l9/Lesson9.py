import turtle as tur

def make_window(title, color):
    farm = tur.Screen()
    farm.setup(width=850,height=750)
    farm.bgcolor(color)
    farm.title(title)

    return farm

def make_paddle(spd, shape, color, size=(6,2),pos=(400,0)):
    paddle = tur.Turtle()
    paddle.speed(spd)
    paddle.shape(shape)
    paddle.color(color)
    paddle.shapesize(stretch_wid=size[0], stretch_len=size[1])
    paddle.penup()
    paddle.goto(pos)

    return paddle

def make_ball(spd, shape, color, size=(2,2),velX=5, velY=-5):
    ball=tur.Turtle()
    ball.speed(spd)
    ball.shape(shape)
    ball.color(color)
    ball.penup()
    ball.shapesize(stretch_wid=size[0], stretch_len=size[1])
    ball.dx = velX
    ball.dy = velY

    return ball

def sketcher(color="purple", score=(0,0)):
    sketcher=tur.Turtle()
    sketcher.speed(0)
    sketcher.color(color)
    sketcher.goto(0, 260)
    sketcher.penup()
    sketcher.hideturtle()
    sketcher.clear()
    sketcher.write(f"Left Player: {score[0]}\t\tRight Player: {score[1]}",
    align="center", font=("Courier", 24, "normal"))





def main():
    table = make_window("Ping Pong Table", "purple")
    ball = make_ball(10, "circle", "orange")


    left_player = make_paddle(0, "square", "green", (6,2), (-400, 0))
    right_player = make_paddle(0, "square", "green", (6,2), (400, 0))

    def leftPaddleUp():
        l_up = left_player.ycor()
        l_up += 20
        left_player.sety(l_up)

        
    def leftPaddleDn():
        l_dn = left_player.ycor()
        l_dn -= 20
        left_player.sety(l_dn)
        

    def rightPaddleUp():
        r_up = right_player.ycor()
        r_upy += 20
        right_player.sety(r_up)
        
    def rightPaddleDn():
        r_dn = right_player.ycor()
        r_dn -= 20
        right_player.sety(r_dn)

    table.listen()
    table.onkeypress(rightPaddleUp, "w")
    table.onkeypress(rightPaddleDn, "s")
    table.onkeypress(leftPaddleUp, "Up")
    table.onkeypress(leftPaddleDn, "Down")

    while True:
        table.update()

        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        left_score = 0
        right_score = 0


        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1
       
       
        if ball.ycor() < 280:
            ball.sety(-280)
            ball.dy *= -1

        if ball.xcor() > 500:
            ball.goto(0,0)
            ball.dy *= -1
            right_score += 1
            sketcher("purple",score=(left_score, right_score))
        
        
        if ball.xcor() < -500:
            ball.goto(0,0)
            ball.dy *= -1
            left_score += 1
            sketcher("purple",score=(left_score, right_score))

        if (ball.xcor() > (left_player.pos()[0] - 40) and ball.xcor() < 370) \
            and ball.ycor() < ((left_player.pos()[1] + 40)) \
                and ball.ycor()> ((right_player.pos()[1] - 40)):
            ball.setx(360)
            ball.dx *= -1
        
        if (ball.xcor() < (right_player.pos()[0] - 40) and ball.xcor() > -370) \
            and ball.ycor()<((right_player.pos()[1] + 40)) \
                and ball.ycor()>((right_player.pos()[1] - 40)):
            ball.setx(-360)
            ball.dx *= -1

main()    