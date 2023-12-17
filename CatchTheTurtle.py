import turtle
import random
import time


turtle_screen = turtle.Screen()
turtle_screen.title("Catch The Turtle")
turtle_screen.bgcolor("light blue")


turtle_ = turtle.Turtle()
turtle_.shape("turtle")
turtle_.color("green")
turtle_.shapesize(4, 4, 4)
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


click_list = [0, 0]


def mouse_click_cor(click_x, click_y):
    print(click_list)
    click_list.insert(0, int(click_x / 50))
    click_list.insert(1, int(click_y / 50))


turtle.onscreenclick(mouse_click_cor)


def random_turtle():
    score_ = 0
    time_ = 25
    while time_ > 0:
        random_x = random.randrange(-300, 300, 10)
        random_y = random.randrange(-300, 250, 10)
        turtle_.teleport(random_x, random_y)

        x_cor = int(turtle_.xcor() / 50)
        y_cor = int(turtle_.ycor() / 50)
        print(f"{x_cor} , {y_cor}")
        xy_click_cor = click_list

        turtle_.showturtle()
        text_turtle.write(arg=f"Score: {score_}", move=False, align='center', font=("arial", 25, "normal"))
        text_turtle2.write(arg=f"Time: {time_}", move=False, align='center', font=("arial", 20, "normal"))
        time.sleep(0.5)
        turtle_.hideturtle()
        time.sleep(0.5)
        time_ -= 1
        text_turtle2.clear()

        if time_ == 0:
            text_turtle2.write(arg="GAME OVER", move=False, align='center', font=("arial", 20, "bold"))

        if xy_click_cor[0] == x_cor and xy_click_cor[1] == y_cor:
            text_turtle.clear()
            score_ += 1


random_turtle()
turtle.mainloop()
