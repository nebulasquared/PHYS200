from TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = .00001


def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

def polygon(t, length, n):
	for i in range(int(n)):
		fd(t, length)
		angle = 360.0/n
		lt(t, angle)

def circle(t, r):
	circum = 2*math.pi*r
	n = int(circum/2)
	length = circum/n
	polygon(t, length, n)

def arc(t,r,angle):
	circum = 2*math.pi*r
	arclength = circum*angle/360
	n = circum/2

	forward = arclength/n
	approach = float(angle)/n
	

	for i in range(int(n)):
		fd(t, forward)
		lt(t, approach)

arc(bob, 100, 30)

#the following check of polygon.py on whether a script
#is running is largely derived from the solution

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

wait_for_user()
