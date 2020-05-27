import random as r
while(1):
	print("enter 1 to play\nenter 0 to exit")
	i = int(input())
	if( i == 0 ):
		break
	else :
		print("enter the beginning and end range for guessing ")
		b = int(input())
		e = int(input())
		if(b > e):
			print("wrong range")
			break
		g = r.randint(b,e)
		k = 0
		print("you will get three chances to guess")
		while(k < 3):
			n = int(input())
			if( n < b or n > e):
				print("check your range plz")
			elif( n == g):
				print("you got it")
				break
			elif( n < g):
				print("think higher")
				k = k + 1
			elif( n > g):
				print("your guessing too high")
				k = k + 1
		if( n != g ):
			 print("answer is ",g)
