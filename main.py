import turtle
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
  t.fd(27)
  t.rt(90)

def l_setup():
  t.lt(180)
  t.penup()
  t.fd(80)
  t.pendown()
  t.rt(90)

t.lt(90)
bigline(100, 20)
t.lt(180)
t.fd(20)
shortbox(40, 15)
shortbox_set()
shortbox(40, 15)
shortbox_set()
shortbox(40, 15)

l_setup()

bigline(100, 20)


turtle.getscreen()._root.mainloop()