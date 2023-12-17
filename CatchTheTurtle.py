import turtle
import random
import time


turtle_screen = turtle.Screen()
turtle_screen.title("Catch The Turtle")
turtle_screen.bgcolor("light blue")

turtle_ = turtle.Turtle()
turtle_.shape("turtle")
turtle_.color("green")
turtle_.shapesize(3, 3, 3)
turtle_.penup()


text_turtle = turtle.Turtle()
text_turtle.color("black")
text_turtle.penup()
text_turtle.hideturtle()
top_height = turtle_screen.window_height() / 2
y = top_height - top_height / 10
text_turtle.setposition(0, y)


text_turtle2 = turtle.Turtle()
text_turtle2.color("red")
text_turtle2.penup()
text_turtle2.hideturtle()
top_height = turtle_screen.window_height() / 2
y = top_height - top_height / 6
text_turtle2.setposition(0, y)


def random_turtle():
    score_ = 0
    time_ = 20
    while time_ > 0:
        random_x = random.randrange(-350, 350, 25)
        random_y = random.randrange(-300, 250, 25)
        turtle_.teleport(random_x, random_y)
        x_cor = int(turtle_.xcor())
        y_cor = int(turtle_.ycor())
        turtle_.showturtle()
        text_turtle.write(arg=f"Score: {score_}", move=False, align='center', font=("arial", 25, "normal"))
        text_turtle2.write(arg=f"Time: {time_}", move=False, align='center', font=("arial", 20, "normal"))
        time.sleep(0.4)
        turtle_.hideturtle()
        time.sleep(0.6)
        time_ -= 1
        text_turtle2.clear()
        if time_ == 0:
            text_turtle2.write(arg="GAME OVER", move=False, align='center', font=("arial", 20, "bold"))


random_turtle()
turtle.mainloop()
