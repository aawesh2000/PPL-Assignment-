p = int(input("Enter dividend: "))
while(1):

    try:
        q = int(input("Enter the divisor: "))
        ans = p / q							 #here we try do division if any time divisor is zero then exception is raised

    except ZeroDivisionError:
        print("Divisor can't be zero\nEnter the divisor again")

    else:
        print(ans)
        break
