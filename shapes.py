import turtle
t = turtle.Turtle()
t.speed(0)
turtle.screensize(1000, 1000)

def draw_square():
  t.begin_fill()
  for i in range (4):
    t.fd(50)
    t.left(90)
  t.end_fill()


def draw_rows(x, y):
  for i in range(4): 
    for i in range(4):
      t.penup()
      t.goto(x,y)
      t.pendown()
      draw_square()
      x+=100
    x-=400
    y+=100


def draw_box():
  t.penup()
  t.goto(-100, -100)
  t.pendown()
  for i in range (4):
    t.fd(400)
    t.left(90)
draw_box()

turtle.getscreen()._root.mainloop()