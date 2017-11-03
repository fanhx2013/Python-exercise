# -*- coding: utf-8 -*-
#cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 运行

#位置参数
'''
def square(x):   #求x的平方
	s = x * x 
	return s

def power(x,n):  #求x的n次方
	s = 1
	while n>0:
		s = s * x
		n = n - 1
	return s
x = int(input())
n = int(input())
print(power(x,n))
'''
#默认参数
'''
由于power()需要传入2个参数，所以显然不能再填入1个参数，否则会报错；
所以就需要定义一个“默认参数”
power(x,n=2)这样用的时候，power(5)就默认计算平方
>>> power(5)
25
>>> power(5, 2)
25
'''
'''
def power(x,n=2):  #求x的2次方
	s = 1
	while n>0:
		s = s * x
		n = n - 1
	return s
x = int(input())
print(power(x))
'''
'''
所以默认参数降低了函数调用的难度
需要注意的是：必选参数在前，默认参数在后，否则会报错；
变化大的参数放在前面，变化小的参数放在后面。变化小的参数可作为默认参数
'''
'''
def enroll(name, gender):
	print('name: ',name)
	print('gender: ',gender)
	return name,gender
name = input()
gender = input()
print(enroll(name,gender))
'''
#可变参数
'''
参数可以是个list或tuple，这样参数就可以无限制
'''
def sum(numbers):
	summit = 0
	for n in numbers:
		summit = summit + n
	return summit
numbers = (1,3,5,7)	
print(sum(numbers))

'''
但是也可以在参数前面加个*号
'''
