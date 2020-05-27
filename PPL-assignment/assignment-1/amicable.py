def divisorsum(i):
	sum = 1
	for j in range(2,int((i**0.5) + 1)):
		if(i%j == 0):
			if(i/j != j):
				sum = sum + j + (i/j)
			else:
				sum = sum + j
	return int(sum)
n = 0
i = 1
while(n < 10):
	i = i + 1
	j = divisorsum(i)
	if(i != j):
		if(i < j):
			if(i == divisorsum(j)):
				print(i, j)
				n = n + 1



