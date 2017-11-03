from random import randint

ainame = 10
print("Guess what I think?")
answer = int(input())
result = (answer - ainame)
bingo = False
while bingo == False:
	answer = int(input())
#	if answer < ainame:
	if result < 0:
		print("Your answer is too small, and input another number.")
#	if answer > ainame:
	if result > 0:
		print("Your answer is too large, and input another number.")
#	if answer == ainame:
	if result == 0:
		print("Bingo!")
		bingo = True

num = randint(1,100)
print("Guess what I think?")
bingo = False

while bingo == False:
	answer = int(input())
	
	if answer < num:
		print("Your answer is too small, and input another number.")
	if answer > num:
		print("Your answer is too large, and input another number.")
	if answer == num:
		print("Bingo!")
		bingo = True

a = 1            #先a设为1
while a != 0:  #a不等于0就一直做
	print ("please input")
	a = int(input())
	print ("over")
