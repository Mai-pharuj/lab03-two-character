# lab03.py for Shulin Li and Pharuj Rajborirug
# CS20, Spring 2016, Instructor: Phill Conrad
# Draw some initials using turtle graphics
import turtle


def drawS(s,w,h):
# draw a letter S using s-Turtle, with some width and height
    

# set up initial position
    s.penup()
    s.setx(-100)
    s.sety(-100)

# start drawing
    s.pendown()
    s.circle(h,-90)
    s.circle(h,270)
    s.circle(-h,270)
    s.goto(-100+h,-100+3*h+w)
    s.circle(-h-w,-90)
    s.circle(-h-w,-180)
    s.circle(h+w,-270)
    s.goto(-100-h, -100+h)
    s.hideturtle()
   
   

def drawL(l,w,h):
# draw a  letter L using l-Turtle, with some width and height

# set up initial position
    l=turtle.Turtle()
    l.penup()
    l.setx(100)
    l.sety(90)

# start drawing
    l.pendown()
    l.right(90)
    l.forward(2*h)
    l.left(90)
    l.forward(h)
    l.left(90)
    l.forward(w)
    l.left(90)
    l.forward(h-w)
    l.right(90)
    l.forward(2*h-w)
    l.left(90)
    l.forward(w)
    l.hideturtle()
   
#test
def go():
    shulin=turtle.Turtle()
    drawS(shulin,4,50)
    drawL(shulin,4,100)
