import turtle

t = turtle.Turtle()

def stairs_downwards(x):
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)

stairs_downwards(20)



turtle.getscreen()._root.mainloop()