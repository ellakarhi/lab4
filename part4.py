import turtle

t = turtle.Turtle()

def stairs_down(x, steps):
  for i in range(steps):
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)

stairs_down(20, 5)

turtle.getscreen()._root.mainloop()