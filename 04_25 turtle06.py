import turtle


def drawM(mTurtle, w, h):
    """
    mTurtle will draw the letter M with width and height
    w and h
    """
#0
    X0 = mTurtle.xcor()
    Y0 = mTurtle.ycor()

#1    
    mTurtle.goto(X0,Y0+h)
#2
    mTurtle.goto(X0+w/4.0,Y0+h)
#3
    mTurtle.goto(X0+w*2.0/4.0,Y0+h*3.0/4.0)
#4
    mTurtle.goto(X0+w*3.0/4.0,Y0+h*4.0/4.0)
#5
    mTurtle.goto(X0+w,Y0+h)
#6
    mTurtle.goto(X0+w,Y0) 
#7
    mTurtle.goto(X0+w*3.0/4.0,Y0)
#8
    mTurtle.goto(X0+w*3.0/4.0,Y0+h*3.0/4.0)
#9
    mTurtle.goto(X0+w*2.0/4.0,Y0+h*2.0/4.0)
#10
    mTurtle.goto(X0+w*1.0/4.0,Y0+h*3.0/4.0)
#11
    mTurtle.goto(X0+w*1.0/4.0,Y0)
#12
    mTurtle.goto(X0,Y0)
#13
    mTurtle.up()
    mTurtle.goto(X0+w,Y0)
    mTurtle.down()
# - - -  - - - - - - -  - - - - - - - - - - - -

def drawR(mTurtle, w, h):
    """
    mTurtle will draw the letter R with width and height
    w and h
    """
#0
    X0 = mTurtle.xcor()
    Y0 = mTurtle.ycor()
#1    
    mTurtle.goto(X0,Y0+h) 
#2
    mTurtle.goto(X0+w*3.0/4.0,Y0+h) 
#3
    mTurtle.goto(X0+w,Y0+h*3.0/4.0) 
#4
    mTurtle.goto(X0+w*3.0/4.0,Y0+h*2.0/4.0) 
#5
    mTurtle.goto(X0+w,Y0) 
#6
    mTurtle.goto(X0+w*3.0/4.0,Y0) 
#7
    mTurtle.goto(X0+w*2.0/4.0,Y0+h*2.0/4.0) 
#8
    mTurtle.goto(X0+w*1.0/4.0,Y0+h*2.0/4.0) 
#9
    mTurtle.goto(X0+w*1.0/4.0,Y0) 
#10
    mTurtle.goto(X0,Y0)
#11
    mTurtle.up()
    mTurtle.goto(X0+w*1.0/4.0,Y0+h*5.5/8.0) 
    mTurtle.down()
#12
    mTurtle.goto(X0+w*1.0/4.0,Y0+h*6.5/8.0)
#13
    mTurtle.goto(X0+w*5.0/8.0,Y0+h*6.5/8.0)
#14
    mTurtle.goto(X0+w*5.5/8.0,Y0+h*6.0/8.0)
#15
    mTurtle.goto(X0+w*5.0/8.0,Y0+h*5.5/8.0)
#16
    mTurtle.goto(X0+w*1.0/4.0,Y0+h*5.5/8.0)
#17
    mTurtle.up()
    mTurtle.goto(X0+w,Y0) 
    mTurtle.down()
# - - -  - - - - - - -  - - - - - - - - - - - -

def drawInitialsMR(mTurtle,w,h,s):
    """
    mTurtle will draw the letter P&R with width, height, and space
    w, h, and s
    """
    drawM(mai,w,h)
    mai.up()
    mai.forward(s)
    mai.down()
    drawR(mai,w,h)

# - - -  - - - - - - -  - - - - - - - - - - - -    
mai = turtle.Turtle()

 
