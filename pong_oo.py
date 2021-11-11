import turtle
#import winsound

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

class Paddle():
    def __init__(self,initial_position):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape('square')
        self.t.color('white')
        self.t.penup()
        self.t.goto(initial_position, 0)
        self.t.shapesize(5, 1)

    def ycor(self):
        return self.t.ycor()

    def sety(self,y):
        return self.t.sety(y)

paddle_a = Paddle(-350)

paddle_b = Paddle(350)

# Ball
ball = turtle.Turtle()
ball.speed(1000)
ball.shape('square')
ball.color('white')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

# Score
score_a = 0
score_b = 0

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        #winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.dy *= -1

    if ball.xcor() > 390:
        #winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    if ball.xcor() < -390:
        #winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)

        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        #winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        #winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
