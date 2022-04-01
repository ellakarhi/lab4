import turtle

def draw_square(t: turtle):
  t.begin_fill()
  for i in range (4):
    t.fd(50)
    t.left(90)
  t.end_fill()

def draw_rows(t: turtle, x, y):
  for i in range(4): 
    for i in range(4):
      t.penup()
      t.goto(x,y)
      t.pendown()
      draw_square(t)
      x+=100
    x-=400
    y+=100

def draw_box(t: turtle):
  t.penup()
  t.goto(-100, -100)
  t.pendown()
  for i in range (4):
    t.fd(400)
    t.left(90)