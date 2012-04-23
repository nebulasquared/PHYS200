#Chapter 5 Exercise 5.3
# What is this code's function?

from TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = .00001

def draw(t, length, n): #Takes parameters of t (turtle), length, and n (iterations)
	if n == 0: #if n is 0, exit function
		return
	angle = 50 #define angle
	fd(t, length*n) #move t forward a distance of n*length
	lt(t, angle) #move t left and a 50 degree angle
	draw(t, length, n-1) #calling the function we are in, while reducing the size of n, without doing so this becomes an infinite recursion
	rt(t, 2*angle) #move t right at 100 degree angle
	draw(t, length, n-1) #calling the function we are in again, also reducing the size of n
	lt(t, angle) #turn left at 50 degrees
	bk(t, length*n) #move backwards
#Expect repetitive recursion. Each value of n will have to go through two full calls to draw before we reduce the initial n value

draw(bob, 3, 7)

#Running the function yields an interesting (with ever reducing size) pattern. Using a small value for length and a small recursion we can fit the whole pattern on the screen. It can be said to look like rough octogons overlapping forming a heart shape. The pattern seems fractal like in nature

