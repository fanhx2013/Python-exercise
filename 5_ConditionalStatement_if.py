# -*- coding: utf-8 -*-
#cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 输入到运行框中

#条件测试
# ==          判断是否相等
# !=          判断是否不相等
# >,>=,<,<=   比较数字
# and         检查多个条件都为True，必须全部都是True才为True；有一个为False，则结果为False
# or          检查多个条件都为False，必须全部都是False才为False；有一个为True，则结果为True
# in          检查特定的值是否已包含在列表中
# not in      检查特定的值是否未包含在列表中
# 布尔表达式  其结果要么是True，要么是False

#if语句
age = 19
if age >= 18:
	print('Yes')
	
#if-else语句
age = 17
if age >= 18:
	print('Yes')
else:
	print('No')
	
#if-elif-else结构
age = 12
if age < 4:
	print('Free to play')
elif age < 18:
	print('You should pay $5')
else:
	print('You should pay $10')
	
#################################练习题##################################
#5-3 外星人颜色#1
alien_color = 'Green'
if alien_color == 'Green':
	print('You got 5 points!')
	
#5-4 外星人颜色#2
alien_color = 'Yellow'
if alien_color == 'Green':
	print('You got 5 points!')
else:
	print('You got 10 points!')

#5-5 外星人颜色#3
alien_color = 'Red'
if alien_color == 'Green':
	print('You got 5 points!')
elif alien_color == 'Yellow':
	print('You got 10 points!')
else:
	print('You got 15 points!')

#########################################################################

#使用if语句处理列表
requests = ['A','B','C','D']
for request in requests:
	if request == 'B':
		print('Sorry, there\'s no B')
	else:
		print('Adding ' + request)
print('Finished!')

#用if处理列表为空的情况
requested = []
if requested:     #这里的if语句后面只加了一个列表名，表示判断当前列表是否为空；如果不空则为True，执行for循环，否则执行else
	for request in requested:
		print("Adding " + request)
	print('Finished!')
else:
	print('Nothing in requested')

#用if处理多个列表间的关系
list_a = ['A','B','C','D','E','F','G']
list_b = ['C','G','H']
for b in list_b:
	if b in list_a:
		print('Adding ' + b)
	else:
		print('Sorry, we don\'t have ' + b)
print('Finished!')

#################################练习题##################################
#5-8 以特殊方式跟管理员打招呼
users = ['admin','A','B','C','D']
for user in users:
	if user == 'admin':
		print('Hello ' + user + ', would you like to see a status report?')
	else:
		print('Hello ' + user + ', thank you for logging in again' )


#########################################################################
