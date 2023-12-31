import turtle as t 

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

#feet
t.goto(-100, -150)
rectangle(50,20,'Black')
t.goto(-30,-150)
rectangle(50,20,'Black')


#legs
t.goto(-25, -50)
rectangle(15,100,'Maroon')
t.goto(-55,-50)
rectangle(-15,100,'Maroon')

#body
t.goto(-90,100)
rectangle(100,150,'Hot pink')

#arms
t.goto(-150, 70)
rectangle(60,15,'Goldenrod')
t.goto(-150,110)
rectangle(15,40,'Goldenrod')

t.goto(10, 70)
rectangle(60,15,'Goldenrod')
t.goto(55,110)
rectangle(15,40,'Goldenrod')

#neck
t.goto(-50,120)
rectangle(15,20,'Maroon')

#head
t.goto(-85,170)
rectangle(80,50,'light blue')

#eyes
t.goto(-60,160)
rectangle(30,10,'white')
t.goto(-57,157)
rectangle(5,5,'black')
t.goto(-42,157)
rectangle(5,5,'black')

#mouth
t.goto(-65,135)
t.right(5)
rectangle(40,5,'red')

t.hideturtle()
