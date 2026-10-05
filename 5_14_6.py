import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
my_turtle = turtle.Turtle()
my_turtle.shape( "circle" )
my_turtle.color( "green" )
my_turtle.penup()
my_turtle.goto(-150, 0)
my_turtle.pendown()

def koch(t:turtle, x):
    if x < 5:
        t.forward(x)
    else:
        koch(t, x/3)
        t.left(60)
        koch(t, x/3)
        t.right(120)
        koch(t, x/3)
        t.left(60)
        koch(t, x/3)
        koch(t, x-1)

koch(my_turtle, 120)

#i honestly completely forgot how the turtle works and how to draw with it, but i think my function is correct
#nvm i figured out i had to have the exitonclick on the bottom lol
turtle.exitonclick()