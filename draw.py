import turtle
pen = turtle.Pen()
pen.speed(1)

pen.color('blue') # Setting colour 'blue' and width
pen.width(3)      # set pen width 

pen.left(30)
pen.forward(100)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(75)

pen.color('red') # set color 'Red'
pen.right(60)
pen.forward(75)
pen.right(90)
pen.backward(150)
pen.right(90)
pen.forward(100)

turtle.done()
