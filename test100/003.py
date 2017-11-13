num = 1
while num <=3000:
	for i in range(1,num):
		if (num+100) == i*i:
			for j in range(1,(num + 268)):
				if (num +268) == j*j:
					print(num)
	num += 1