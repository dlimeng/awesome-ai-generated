import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("pink")
pen.begin_fill()

pen.left(140)
pen.forward(180)
pen.circle(90, 200)
pen.setheading(60)
pen.circle(90, 200)
pen.forward(180)

pen.end_fill()
turtle.done()