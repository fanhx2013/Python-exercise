#随机生成一个数（比如范围是在1~100），允许猜5次，猜大了就提示猜大了，
#猜小了就提示猜小了，猜中了就提示猜中了并输出你猜的这个数。超过5次就提示没机会了不能再猜

# -*- coding: utf-8 -*-
import random

random_num = random.randint(1, 10)
guess = int(input("请输入您猜的数字："))
for i in range(1, 6):
    if i > 4:
        print("抱歉，您没有机会了！")
        break
    if guess > random_num:
        guess = int(input("您猜大了，请再猜："))
    elif guess < random_num:
        guess = int(input("您猜小了，请再猜："))
    elif guess == random_num:
        print("您猜中了！是" + str(guess))
        break
