import turtle
turtle.screensize(1000)
t = turtle.Turtle()

def bigline(x, y):
  t.fd(x)
  t.rt(90)
  t.fd(y)
  t.rt(90)
  t.fd(x)
  t.rt(90)
  t.fd(y)
def shortbox(x, y):
  t.fd(x)
  t.lt(90)
  t.fd(y)
  t.lt(90)
  t.fd(x)
def shortbox_set():
  t.rt(90)
  t.fd(27.5)
  t.rt(90)

def l_setup(x):
  t.lt(180)
  t.penup()
  t.fd(x)
  t.pendown()
  t.rt(90)

#To make the E
t.lt(90)
bigline(100, 20)
t.lt(180)
t.fd(20)
shortbox(40, 15)
shortbox_set()
shortbox(40, 15)
shortbox_set()
shortbox(40, 15)

#To make the Ls
l_setup(80)
bigline(100, 20)
t.lt(180)
l_setup(40)
bigline(100,20)

#to make the A
t.penup()
t.fd(20)
t.rt(90)
t.fd(70)
t.pendown()
t.circle(30)
t.penup()
t.fd(20)
t.lt(90)
t.fd(30)
t.pendown()
t.circle(20)
t.penup()
t.fd(50)
t.lt(110)
t.pendown()
shortbox(65,10)
t.lt(90)
t.fd(15)

turtle.getscreen()._root.mainloop()