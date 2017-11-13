l = int(input("Please input the lirun: "))
price = 0
if l <= 10:
	price = l*0.1
elif l > 10 and l <= 20:
	price = 1+(l-10)*0.075
print(price)