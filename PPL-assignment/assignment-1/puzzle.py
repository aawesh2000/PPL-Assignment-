import sys
def puzzle():
	
	#print ("What is your first move?")
	obj=eval(input("What is your first move?"))
	if obj=="G":
		print("Good move!,Next ?")
		obj2=eval(input())
		if obj2=="A":
			print("Good move!,Next ?")
			obj3=eval(input())
			if obj3=="GR" or obj3=="W":
				print("Good move!,Next ?")
				obj4=eval(input())
				if obj4=="FG":
					print("Correct,Next?")
					obj5=eval(input())
					if obj5=="W" or obj5=="GR":
						print("Correct, Next ?")
						obj6=eval(input())
						if obj6=="A":
							print("Correct, Next ?")
					
							
							obj7=eval(input())
							if obj7=="G":
								print("you have solved it")
							else:
								print("Game over")
								sys.exit()
			
						else:
							print("Game over")
							sys.exit()
			
					else:
						print("Game over")
						sys.exit()
			
				else:
					print("Game over")
					sys.exit()
			
			else:
				print("Game over")
				sys.exit()
			
				
		else:
				print("Game over")
				sys.exit()
			
	else:
		print("Game over")
		sys.exit()
    						
	
if __name__ == "__main__": 					
	print ("TO SELECT GOAT,ENTER-G,TO SELECT TIGER ENTER-T,TO SELECT GRASS ENTER-GR")
	print ("TO MOVE THE FARMER ALONE TO ORIGINAL SIDE,ENTER A")
	print ("TO RETURN TO ORIGINAL SIDE,USE FARMER WITH GOAT/WOLF/GRASS-FG/FW/FGR")
	puzzle() 
