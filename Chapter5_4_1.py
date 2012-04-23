#Chapter 5 Exercise 5.4
#Create a Koch curve fractal, use TurtleWorld to create the pattern

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

koch(bob, 150)
		
