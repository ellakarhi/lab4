import turtle

t = turtle.getturtle()
t.fd(30)
t.rt(90)
t.fd(40)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(40)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(40)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(40)



def right():
  t.fd(30)
  t.rt(90)
def left():
  t.fd(40)
  t.lt(90)

right()
left()
right()
left()
right()
left()
right()
left()

turtle.getscreen()._root.mainloop()