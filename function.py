# -*- coding: utf-8 -*-
import math

print(max(1,3,-4))

n1 = 255
n2 = 1000
N1 = hex(n1)
N2 = hex(n2)
print(str(N1))
print(str(N2))

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

#print(my_abs(-5))
def power(x,n):
	sum = 1
	while n > 0:
		sum = sum *x
		n = n - 1
	return sum

print(power(2,3))

a = '   Python   a   '
print(a.rstrip())

def nop():
	pass


def quadratic(a,b,c):
	derta = b**2 - 4*a*c
	x1 = 1
	x2 = 1
	if a == 0:
		return('a cannot be zero, please input another number')
	elif derta < 0:
		return('wrong number, derta cannot lower than 0')
	elif derta == 0:
		x1 = -b/(2*a)
		return x1
	elif derta > 0:
		x1 = (-b + math.sqrt(derta))/(2*a)
		x2 = (-b - math.sqrt(derta))/(2*a)
		return x1, x2
a = int(input('Please input a: '))
b = int(input('Please input b: '))
c = int(input('Please input c: '))
print(quadratic(a,b,c))
