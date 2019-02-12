from __future__ import division
import math

def f_prnt_tst_msg():
    print ">>> printing test message..."

def f_0(r,s,n):
	# r = radius, n = x_n position, s = slices
	# A_n = (r^2 * sqrt(1 - (n/s)^2))/s
	return ((r**2 * ((1-(n/s)**2)**(1/2))))/s

def f_integral(r,s,a):
	# when a new slice size is defined,
	# move through all n-1 positions and sum areas together ...

	# area of quarter circle
        print (math.pi * r**2)/4

	# run s-1 x's
	for x in range(0, s):
		a += f_0(r,s,x)
        print a
	# arbitrary precision hard-coded
	if (a/((math.pi * r**2)/4)) > 1.0017 and (a/((math.pi * r**2)/4)) < 1.0018:
	        #a = f_0(r,s,n,)
		return a
	else:
		print "here we are ..."
		s += 1
		a = 0
		return f_integral(r,s,a)

print "...showing integral..."
print f_integral(235,1,0)
print "...test message..."
f_prnt_tst_msg()
