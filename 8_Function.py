# -*- coding: utf-8 -*-
#cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 运行
import math

###################################函数的参数#######################################
#位置参数（参数的调用顺序要正确）
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('dog', 'Harry')
#describe_pet(5,6) 注意这里传int型会报错
#-----------------------------------------------------------------------------------
#关键字参数
describe_pet(animal_type = 'cat', pet_name = 'Mike')
'''这里还是用上面的函数，只是传参时指定了参数名，这样即使顺序不同也能正确传参'''

#举例 - 接收用户信息
def build_profile(first, last, **user_info):   #该函数需用户提供名、姓、以及其他任意数量的“键-值”对，**user_info为空字典
	profile = {}                               #先创建一个profile空字典，用来存储用户简介
	profile['first_name'] = first              #将“名”加入到字典中
	profile['last_name'] = last                #将“姓”加入到字典中
	for key, value in user_info.items():       #遍历user_info所有的“键-值”对
		profile[key] = value                   #并把key,value都加到profile
	return profile                             #然后返回profile

user_profile = build_profile('albert','einstein',location = 'princeton',filed = 'physics',)
print(user_profile)

#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

#请看示例：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Michael', 30)                           #输出name: Michael age: 30 other: {}

#也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing')               #输出name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')  #输出name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#关键字参数有什么用？它可以扩展函数的功能。
#比如，在person函数里，我们保证能接收到name和age这两个参数，
#但是，如果调用者愿意提供更多的参数，我们也能收到。
#试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
#其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])   #输出name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#当然，上面复杂的调用可以用简化的写法：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)     #输出name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
#-----------------------------------------------------------------------------------
#命名关键字参数

#-----------------------------------------------------------------------------------
#默认参数
'''
def describe_pet(animal_type = 'dog', pet_name):  #这样是错的，默认参数应该放在后面，否则报错SyntaxError: non-default argument follows default argument
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet(pet_name = 'Harry')
describe_pet('Harry')
'''
def describe_pet(pet_name, animal_type = 'dog'):  #这样就没有问题了
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#以下三种传参方式都可以
describe_pet(pet_name = 'Harry')
describe_pet('Harry')
describe_pet('Mike', animal_type = 'cat')

#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
#先定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L

#当你正常调用时，结果似乎不错：
add_end([1, 2, 3])        #返回[1, 2, 3, 'END']
add_end(['x', 'y', 'z'])  #返回['x', 'y', 'z', 'END']

#当你使用默认参数调用时，一开始结果也是对的：
add_end()                 #返回['END']

#但是，再次调用add_end()时，结果就不对了：
add_end()                 #返回['END', 'END']
add_end()                 #返回['END', 'END', 'END']

#很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
#原因解释如下：
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#如果改变了L的内容，则下次调用时，默认参数的内容就变了，
#不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：!!!!!默认参数必须指向不变对象!!!!!

#要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#现在，无论调用多少次，都不会有问题：
add_end()   #返回['END']
add_end()   #返回['END']
#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，
#对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
#此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时
#读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，
#那就尽量设计成不变对象。
#-----------------------------------------------------------------------------------
#可变参数
'''如果我们想求任意数的平方和，可以这样写'''
def cal(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n**2
	return sum
print(cal([1,2,3])) #结果是14

'''但是这样的话，调用的时候还得组装出一个list或tuple，比较麻烦，所以可以把函数的参数改为可变参数'''
def cal(*numbers):    #只需要参数前面加个星号，这样参数接收到的就是一个tuple，内部代码不变
	sum = 0
	for n in numbers:
		sum = sum + n**2
	return sum
print(cal(1,2,3)) #传参的时候就可以传任意个数字，空的也行

'''又如果，已经存在一个list或tuple变量，怎么用可变参数传进去呢？'''
num = [1,2,3]
print(cal(num[0],num[1],num[2])) #这样把每个元素都传进去

'''但是这样又太麻烦，所以Python允许在list或tuple前面加个星号，把list或tuple的元素变为可变参数传进去'''
num = [1,2,3]
print(cal(*num))  #这样就可以了
#-----------------------------------------------------------------------------------
#参数组合

#############################################################################

###############################练习题###############################
#8-6 城市名
def city_country(city, country):
	print(city, country)
city_country('China','Beijing')
city_country('Japan','Tokyo')
city_country('Korea','Seoul')

#8-7 专辑
def make_album(singer, album_name, songs_num = ''):
	album = {'singer':singer, 'album_name':album_name}
	if songs_num:
		album['songs_num'] = songs_num
	return album
print(make_album('Jay','Cowboy'))
print(make_album('JJ','No.89757',12))

#8-8 用户的专辑
def make_album(singer, album, songs_num = ''):
	album_info = {'singer':singer, 'album':album}
	if songs_num:
		album_info['songs_num'] = songs_num
	return album_info

while True:
	print("\nPlease tell me the singer name: ")
	print("(Enter 'q' at any time to quit)")
	singer_name = input("Singer name: ")
	if singer_name == 'q':
		break
	album_name = input("Album name: ")
	if album_name == 'q':
		break
	album = make_album(singer_name, album_name)
	print(album)
	
#8-9 魔术师（使用函数修改列表）
magicians = ['Adam','Bob','Cindy','Diana','Ella']
def show_magicians(magicians):
	for each in magicians:
		print(each)
show_magicians(magicians)

#8-10 了不起的魔术师
def make_great(magicians):
	for each in magicians:
		print("the Great " + each)
make_great(magicians)

#8-11 不变的魔术师
make_great(magicians[:])   #这里表示make_great函数调用的是magicians的副本，而不是原件

#8-12 三明治
def sandwich(*food):
	for each in food:
		print(each)		
sandwich('A','B','C')

#8-13 用户简介
#略

#8-14 汽车
def make_car(manufacturer, model, **kw):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key, value in kw.items():
		car[key] = value
	return car

car_info = make_car('buick', 'regal', color = 'yellow', part = True)	
print(car_info)


####################################################################





'''
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
'''

'''
#一元二次方程求解
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
'''

'''test'''
