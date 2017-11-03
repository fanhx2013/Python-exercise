# -*- coding: utf-8 -*-

name = ['a','b','c']
for x in name:
	print(x)

sum = 0
number = [1,2,3,4,5,6,7,8,9,10]
for x in number:
	sum = sum + x
print(sum)

number = list(range(101))
sum = 0
for x in number:
	sum = sum + x
print(sum)


sum = 0
n = 100
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print('Hello, ',x)


n = 0
while n < 10:
	n = n + 1
	if n%2 == 0:
		continue
	print(n)
