import turtle
import shapes_new as s

# Here's a way of doing it that I don't really love but it works.
# The problem with the old way was that by creating the turtle object
# within the Shapes file, it was executing the entire file upon import
# and the turtle was being deleted before it was ever being used - 
# if that makes sense.

# In other words, when you wrote "import shapes", it was 
# creating the Turtle on lines 2, 3, and 4 of shapes.py, and then terminating at 
# line 35 right away and essentially deleting the turtle from memory. 

# By creating the Turtle right here in the part10 file and passing it to the 
# functions that utilize it, it'll remain 'alive' until the end of THIS 
# file rather than the end of the shapes.py file.

# So, in lines 3, 10, and 21 within the shapes_new file I made, you can see
# how I changed the functions to take in a turtle object from somewhere else
# and in the function calls below you can see that I'm passing the turtle as
# an argument to those functions.

t = turtle.Turtle()
t.speed(0)
turtle.screensize(1000, 1000)

s.draw_rows(t, -100, -100)
s.draw_rows(t, -50, -50)
s.draw_box(t)