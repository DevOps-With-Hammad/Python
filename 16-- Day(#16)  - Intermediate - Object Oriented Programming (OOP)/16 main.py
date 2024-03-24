# Object and Class Creation
import turtle
import another_module

print("Here is your answer " + str(another_module.car + another_module.merc)
      + "\n followed by getting data from another module\n  "
      + str(another_module.bm))

# Let's Play a little with Turtle
from turtle import Turtle, Screen
Hammad = Turtle()
print(Hammad)
Hammad.shape("turtle")
Hammad.color("yellow")
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()