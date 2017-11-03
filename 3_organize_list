# -*- coding: utf-8 -*-
#cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 输入到运行框

#方法sort()会永久性的修改列表的排列顺序
cars = ['bmw','audi','buick','benz','toyota']
cars.sort()
print(cars)

#也可以将列表元素倒着排序，只需要加个参数“reverse=True”即可，而且同样也是永久性的
cars.sort(reverse=True)
print(cars)

#和方法sort()不同，函数sorted()则可以临时改变列表顺序，而不会对原始数据产生影响（注意，一个是方法，一个是函数）
print(sorted(cars))  #这个是['audi','benz','bmw','buick','toyota']
print(cars)          #这个是['toyota','buick','bmw','benz','audi']，还是原来的顺序，没变

#同样函数sorted()也可以倒着排序，参数也是“reverse=True”，也是临时的
print(sorted(cars,reverse=True))

#倒着打印列表则可以用方法reverse()，它不会按首字母排序，只是单纯的将当前列表倒着排；同样它也是永久性的，如果想回到原始数据，那么再执行一遍reverse()即可
fruit = ['pear','apple','strawberry','banana','cherry']
fruit.reverse()
print(fruit)

#函数len()确定列表长度
print(len(fruit))
