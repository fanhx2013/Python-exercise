# -*- coding: utf-8 -*-
#cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 输入到运行框中

#for循环遍历列表
magicians = ['A','b','c','d','e']
for magician in magicians:
	print(magician)
	
#函数range()用于生成一系列数字
for value in range(1,5):
	print(value)      #结果是只会打印出1,2,3,4（因为range表示只显示到第几个数前为止）

#函数list()可以将range()出的数字作成列表
print(list(range(1,5))) #这个输出的是[1,2,3,4]

#函数range()还可以指定步长
print(list(range(2,11,2))) #这个输出1~10之间的偶数

#函数range()几乎可以创建出任何你想要的数字集
squares = []
for num in range(1,11):
	square = num**2
	squares.append(square)
print(squares)

#有一些可以计算列表中最大、最小、求和等等的函数，如下：
num = [1,2,3,4,5,6,7,8,9,10]
print(max(num)) #10
print(min(num)) #1
print(sum(num)) #55

#列表解析（注意这里的for循环不需要加冒号）
sum_squares = [value**2 for value in range(1,11)] #输出[1,4,9,16,25,36,49,64,81,100]
print(sum_squares)

########################练习题########################
#4-3 数到20
for number in range(1,21):
	print(number)
#4-4 打印出一百万
#print(list(range(1,1000001)))

#4-5 计算1~1000000的总和
list_a = list(range(1,1000001))
print(max(list_a))
print(min(list_a))
print(sum(list_a))

#4-6 奇数
list_b = []
for each in range(1,20,2):
	list_b.append(each)
print(list_b)

#4-7 3的倍数
list_c = list(range(3,30,3))
print(list_c)
for every_num in list_c:
	print(every_num)
	
#4-8 立方
list_d = [value**3 for value in range(1,11)]
print(list_d)

######################################################

#切片：用于处理列表的部分元素
players = ['A','B','C','D','E']
print(players[0:3]) #同range()一样，这里输出的就是第0,1,2这三个元素（没有第3个元素），输出'A','B','C'
print(players[1:4]) #这个就是从第二个开始提取，输出'B','C','D'
print(players[:4])  #当没有前面的索引时，默认从头开始提取，输出'A','B','C','D'
print(players[2:])  #当没有后面的索引时，默认提取到最后，输出'C','D','E'
print(players[-3:]) #当索引是负数时，表示从倒数第N个元素开始提取，一直到最后一个元素，输出'C','D','E'

#遍历切片：可以用for循环来遍历切片
for player in players[:3]:  #依次打印出列表的前三名
    print(player)

#复制列表
A_foods = ['pizza','fruits','noodles','rice']
B_foods = A_foods[:]    #注意此处不能写作B_foods = A_foods，因为这样就相当于A和B是同一个列表，之后无论对A或B作出任何操作，都会同时作用于A和B
A_foods.append('ddd')
B_foods.append('eee')
print(A_foods)          #输出['pizza','fruits','noodles','rice','ddd']
print(B_foods)          #输出['pizza','fruits','noodles','rice','eee']

#元组的创建
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = ()     #这表示是一个空元组
tup5 = (50,)  #元组中只包含一个元素时，需要在元素后面添加逗号来消除歧义

#元组中的元素不可被修改
a_tuple = (200,50)
#a_tuple[0] = 250  #这样就会报错，因为元组中的元素不可以被修改

#访问元组(元组与字符串类似，下标索引从0开始，可以进行截取，组合等)
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print(tup1[0])      #输出'physics'
print(tup2[1:5])    #输出(2,3,4,5)

#遍历元组：可以用for循环来遍历元组
for each_tuple in a_tuple:  #依次打印出列表的所有值
	print(each_tuple)

#修改元组(虽然元素不可被修改，但是可以对元组进行连接组合)
tup6 = tup1 + tup2
print(tup6)   #输出('physics', 'chemistry', 1997, 2000,1,2,3,4,5,6,7)

#删除元组(元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组)
del tup6
#print(tup6)  #报错，输出#NameError: name 'tup6' is not defined，表示tup6已被删除，无法打印出来
