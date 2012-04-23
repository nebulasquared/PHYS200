#Chapter 5 Exercise 5.4
#Create a function snowflake that draws three Koch curves to create a snowflake using TurtleWorld

from TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = .00001

def koch(t, x):
	if x<3:
		fd(t, x)
	else:
		koch(t, x/3.0) #should it be x/3.0 or x/3?
		lt(t, 60.0)
		koch(t, x/3.0)
		rt(t, 120.0)
		koch(t, x/3.0)
		lt(t, 60.0)
		koch(t, x/3.0)

def snowflake(t,x):
	for i in range(2):
		koch(t,x)
		rt(t, 60.0)
		koch(t,x)
		rt(t,60.0)
		koch(t,x)
		rt(t, 60.0)

snowflake(bob,100)
