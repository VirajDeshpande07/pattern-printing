# Print spaces before the stars
for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")
    # Print increasing stars
    for k in range(i+1):
        print("*",end=" ")
    print()  # Move to the next line