for i in range(5):  #this loop indicates no of rows 
    for j in range(5-i): # j loop indicates no of spaces in each row
        print(" ",end=" ")
    for k in range(i+1): # k loop indicates no of stars in each row
        print("*",end=" ")
    for l in range(i):# l loop indicates no of stars in each row
        print("*",end=" ")
    print()