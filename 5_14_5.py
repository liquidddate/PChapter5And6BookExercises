import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
my_turtle = turtle.Turtle()
my_turtle.shape( "circle" )
my_turtle.color( "green" )


def draw(t:turtle, length):
    angle = 50
    factor = 0.6

    if length > 5:
        t.forward( length )
        t.left( angle )
        draw(t, factor * length )
        t.right( 2 * angle )
        draw(t, factor * length )
        t.left( angle )
        t.back( length )

# my hypothesis is that the turtle will draw in upon itself until the recursion stops.

#it makes a cool fractal pattern, i was way off

draw(my_turtle, 100)

turtle.exitonclick()