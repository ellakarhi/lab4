import turtle

t = turtle.Turtle()

def stairs_down(horizontal, steps, vertical):
  for i in range(steps):
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.left(90)

stairs_down(2, 6, 30)

turtle.getscreen()._root.mainloop()