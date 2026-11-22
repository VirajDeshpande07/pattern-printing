# Print spaces at the beginning of each row
for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    # Print decreasing stars
    for k in range(5-i):
        print("*",end=" ")
    # Print extra stars to complete the pattern
    for l in range(4-i):
        print("*",end=" ")
    print()  # Move to the next line