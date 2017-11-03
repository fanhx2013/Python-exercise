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
