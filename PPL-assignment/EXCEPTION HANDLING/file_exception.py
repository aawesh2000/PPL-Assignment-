while(1):
    file = input("filename: ")
    try:                          #search for the file if file is not found then it will raise a exception
        file = open(file, 'r')  
        content = file.read()
    except IOError:					   							
        print("\nFile does not exist.Please enter again.\n")
    else:								
        print(content)
        break
