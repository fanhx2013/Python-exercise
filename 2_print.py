# -*- coding: utf-8 -*-
age = int(input('Please input the age:'))
if age >= 18:
	print('adult')
else:
	print('teenager')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'

print(b'ABC'.decode('ascii'))

s1 = 72
s2 = 85
r = (s2 - s1)/s1*100
print('提升的成绩为：''%.1f''%%'%r)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
# L的长度：
print(len(L))
# L的末尾追加'a'
print(L.append('a'))
print(L)
# 把'b'插到元素1的位置
print(L.insert(1,'b'))
print(L)
# 删除L末尾的元素
print(L.pop())
print(L)
# 删除元素1
print(L.pop(1))
print(L)
# 把元素2替换为'c'
L[2] = 'c'
print(L)
