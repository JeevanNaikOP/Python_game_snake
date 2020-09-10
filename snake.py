import turtle
import time
import random

delay = 0.2
score=0
highscore=0

# screen
wn = turtle.Screen()
wn.title("snake game by jeevan")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) 

# snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup() #animation draw =none
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() #animation draw =none
food.goto(0, 100)

segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0 High-score:0",align="center",font=("courier",24,"normal"))


# function
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
       head.direction = "left"


def go_right():
    if head.direction != "left":
       head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bind
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# main
while True:
    wn.update()

    #check collision
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        # hide segment
        for segment in segments:
            segment.goto(1000,1000)

        # clear the segment
        segments.clear()

        # reset the score
        score=0
        pen.clear()
        pen.write("Score:{} High-score:{}".format(score, highscore), align="center", font=("courier", 24, "normal"))

    # when head touches food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # to make difficult
        delay -= 0.01

        # increase the score
        score+=10
        if score>highscore:
            highscore=score

        pen.clear()
        pen.write("Score:{} High-score:{}".format(score,highscore),align="center", font = ("courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

        # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            # hide segment
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment
            segments.clear()

    time.sleep(delay)


