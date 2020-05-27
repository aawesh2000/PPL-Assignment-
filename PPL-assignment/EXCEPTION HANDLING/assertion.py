try: 
    x = 1
    y = 0
    assert y != 0,"invalid operation"#second argument here is the error message provided by the user to get printed if faced any error
    print(x / y)  #runs if condition is true
  
except AssertionError as msg:    
    print(msg)
