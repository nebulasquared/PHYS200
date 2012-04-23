def is_triangle(a,b,c):
    if a > (b + c) or b > (a + c) or c > (a + b):
        print 'No, this is not a true triangle. Rinse and repeat.'
    else:
        print 'Yes, apparently we have created a triangle. '

def make_triangle():
	a = int(raw_input('What is the length of triangle side a?\n'))
	b = int(raw_input('What is the length of side b?\n'))
	c = int(raw_input('What is the length of side c?\n'))
	is_triangle(a,b,c)

make_triangle()
