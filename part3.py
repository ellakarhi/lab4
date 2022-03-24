import turtle

t = turtle.Turtle()

def stairs_down(x):
  for i in range(4):
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)

stairs_down(20)

turtle.getscreen()._root.mainloop()