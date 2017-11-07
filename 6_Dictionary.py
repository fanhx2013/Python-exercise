# -*- coding: utf-8 -*-
#cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 输入到运行框中

#字典的定义，是一系列的“键-值”对
dict = {'Peter':95,'Bob':78,'Jack':88}
print(dict['Peter'])

#添加“键-值”对（添加顺序是无序的）
dict['Adam'] = 99
print(dict)

#创建空字典
dict_a = {}
print(dict_a)

#修改字典中的值
dict['Adam'] =78
print(dict)

#删除“键-值”对
del dict['Adam'] #这里被删除的“键-值”对是被永久删除的
print(dict)

#多行字典，注意缩进
dict_b = {
	'A':'a',
	'B':'b',
	'C':'c',
	'D':'d',
	'E':'b',
	'F':'c',  #最后一个逗号可写可不写
	}
print(dict_b)

#遍历字典中的“键-值”对，使用方法items()
for key,value in dict_b.items():
	print(key,value)

#遍历字典中的所有“键”，使用方法keys()
for key in dict_b.keys():   #这里省掉“.keys()”也可以，默认就把字典中的所有keys都打印出来
	print(key)

#按顺序遍历字典中的所有“键”，使用函数sorted()
for key in sorted(dict_b):  #这里将“键”按照A-Z的排序输出
	print(key)

#遍历字典中的所有“值”，使用方法values()
for value in dict_b.values():
	print(value)   #这样就可以打印出所有的“值”
print('\n')

for value in set(dict_b.values()):    #但是用函数set()就可以将重复的“值”删掉，仅保留独一无二的“值”，结果同样是无序的
	print(value)

#嵌套——字典列表
alien0 = {'color':'green', 'points':5}
alien1 = {'color':'yellow', 'points':10}
alien2 = {'color':'red', 'points':15}

aliens = [alien0,alien1,alien2]
for alien in aliens:
	print(alien)

aliens = []
for alien_number in range(30):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print('...')

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
		
#嵌套——在字典中存储列表
pizza = {
	'crust':'thick',
	'toppings':['mushroom','extra cheese'],
	}
print(pizza['crust'])
print(pizza['toppings'])

#嵌套——在字典中存储字典
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
		},    #这里的逗号千万不能忘掉
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',		
		},
	}
for username, user_info in users.items():
	print(username)
	full_name = user_info['first'] + ' ' +user_info['last']
	location = user_info['location']
	print(full_name)
	print(location)
	
#其他功能
dict = {'Peter':95,'Bob':78,'Jack':88}
b = 'Black' in dict      #通过in判断key是否存在
print(b)                 #这里返回False

c = dict.get('Black')    #也可以通过get获取key是否存在
print(c)                 #这里返回None，因为不存在；如果存在，则返回对应的value值

e = dict.get('Black',-2) #这里get到Black的值是-2，而实际上Black并未存储到dict中
print(e)                 #返回-2

f = dict.get('Bob')
print(f)                 #这里返回78

g = dict.pop('Bob')      #用方法pop()可以删除一个“键-值”对
print(dict)
'''
一、请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
二、和list比较，dict有以下几个特点：
1.查找和插入的速度极快，不会随着key的增加而变慢；
2.需要占用大量的内存，内存浪费多。
而list相反：
1.查找和插入的时间随着元素的增加而增加；
2.占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
三、dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出
的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等
都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
'''
