sum = 1
for i in range(0,100):
	for j in range(0,100):
		sum += i + j
		sum *= sum
		print ("Sum = ", end="")
		print(sum)