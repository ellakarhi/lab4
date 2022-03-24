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


t.lt(90)
bigline(100, 20)
t.backward(20)
shortbox(40, 15)


turtle.getscreen()._root.mainloop()