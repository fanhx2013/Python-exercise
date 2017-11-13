
number = [1,2,3,4]
for i in number:
	for j in number:
		for k in number:
			if i != j and i != k and j != k:
				print(i*100+j*10+k)