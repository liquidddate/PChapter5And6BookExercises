import turtle


def draw_sierpinski(t, length, depth):
    if depth == 0:
        # base case: draw one triangle and end up where we started
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        half = length / 2
        # bottom-left sub-triangle
        draw_sierpinski(t, half, depth - 1)
        # bottom-right sub-triangle
        t.forward(half)
        draw_sierpinski(t, half, depth - 1)
        t.backward(half)
        # top sub-triangle
        t.left(60)
        t.forward(half)
        t.right(60)
        draw_sierpinski(t, half, depth - 1)
        t.left(60)
        t.backward(half)
        t.right(60)


t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, -100)
t.pendown()

draw_sierpinski(t, 300, 3)

turtle.done()