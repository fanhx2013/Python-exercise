# -*- coding: utf-8 -*-
#cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 输入到运行框中

###############################练习题###############################
#7-1 汽车租赁
car = input('What car do you want to rental?')
print('Let me see if I can find you a ' + car)

#7-2 餐馆订位
guest = input('How many people for dinner?')
if int(guest) > 8:
	print('Sorry, there\'s no table tonight.')
else:
	print('OK, we will hold a table for you.')

#7-3 10的整数倍
number = input('Please input a number')
if int(number)%10 == 0:
	print('It canbe divided by 10!')
else:
	print('Sorry, it cannot be divided by 10.')
	
####################################################################

#while语句——让用户选择何时退出
promt = '\n1.Tell me something, and I will repeat it back to you:'
promt += '\nEnter \'quit\' to end the program.'
message = ''
while message != 'quit':      #当用户输入quit的时候，程序才会停止
	message = input(promt)
	print(message)            #但是这个程序会在用户输入quit后又重复了一遍quit

promt = '\n2.Tell me something, and I will repeat it back to you:'
promt += '\nEnter \'quit\' to end the program.'
message = ''
while message != 'quit':
	message = input(promt)
	if message != 'quit':     #这样的话就不会最后又打印一遍quit了
		print(message)
		
#使用标志
promt = '\n3.Tell me something, and I will repeat it back to you:'
promt += '\nEnter \'quit\' to end the program.'
active = True
while active == True:
	message = input(promt)
	if message == 'quit':
		active = False
	else:
		print(message)

#使用break退出循环（在任何Python循环中都可以使用break语句）
promt = '\n4.Tell me something, and I will repeat it back to you:'
promt += '\nEnter \'quit\' to end the program.'
while True:           #这里跟上面的标志意义是一样的，只不过没有再定义个变量而已
	message = input(promt)
	if message == 'quit':
		break         #此处的break就可以直接跳出循环，不再执行余下代码
	else:
		print(message)

#在循环中使用continue
current_number = 0              #先定义个数字
while current_number < 10:      #在0~10内循环
	current_number += 1
	if current_number%2 == 0:   #如果是偶数
		continue                #就跳出去，从头再循环
	print(current_number)       #如果是奇数，就把它打印出来
	
#避免无限循环（Ctrl+C即可停止循环）

###############################练习题###############################
#7-4 比萨配料
topping = ''
while topping != 'quit':
	topping = input('Please say a topping: ')
	if topping != 'quit':
		print('We will add ' + topping + ' to your pizza.')

#7-2 电影票
age = 0
while age < 200:
	age = int(input('Please input your age: '))
	if age < 3:
		print('You\'re free to see the movie')
	elif age >= 3 and age < 12:
		print('Your ticket price is $10')
	elif age >= 12:
		print('Your ticket price is $15')
	elif str(age) == 'quit':
		break
#7-3 三个出口
#略

#7-4 无限循环
topping = input('Please say a topping: ')
while topping != 'quit':
	if topping != 'quit':
		print('We will add ' + topping + ' to your pizza.')
	else:
		break

#7-8 熟食店
sandwich_orders = ['A','B','C','D','E']
finished_sandwiches = []
while sandwich_orders:
		current_sandwich = sandwich_orders.pop()
		print('I made your ' + current_sandwich + ' sandwich')
		finished_sandwiches.append(current_sandwich)
for each in finished_sandwiches:
	print(each)
	
#7-9 五香烟熏牛肉（pastrami）卖完了
sandwich_orders = ['A','pastrami','B','C','pastrami','D','pastrami','E']
print("Sorry, pastrami is sold out.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

#7-10 梦想的度假胜地
vacationland = {}
active = True
while active:
	name = input("\nWhat is your name? ")
	response = input("\nWhat is your vacationland? ")
	vacationland[name] = response
	repeat = input("Would you like to let another person respond? (yes/no)")
	if repeat == "no":
		active = False
print("\n---- Poll Results ----")
for name, response in vacationland.items():
	print(name,response)

####################################################################


#for循环
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
