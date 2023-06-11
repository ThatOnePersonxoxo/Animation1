import turtle

turtle.bgcolor('#303030')

animation = turtle.Turtle()
animation.speed(20)
animation.pencolor('#ADD8E6')
for i in range (400):
    animation.forward(i)
    animation.left(91)

a2 = turtle.Turtle()
a2.speed(15)
a2.pencolor('#006400')
for i in range (350):
    a2.forward(i)
    a2.right(91)

a3 = turtle.Turtle()
a3.speed(20)
a3.pencolor('#FFD700')
for i in range (400):
    a3.forward(i)
    a3.right(91)

a4 = turtle.Turtle()
a4.speed(15)
a4.pencolor('#CAFF70')
for i in range (400):
    a4.forward(i)
    a4.left(300)
