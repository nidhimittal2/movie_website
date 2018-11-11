import turtle
def draw_square(brad):
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)
#def draw_triangle(tom):
    #for i in range(0,3):
    #    tom.forward(100)
    #    tom.left(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(80)
    for i in range(0,36):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()
draw_art()
