l = ['a','b','c','d','e']
try:
    print(l[5])   #index error 
except LookupError: #looking for index out of range 
    print("list index out of range")
else:
    pass
