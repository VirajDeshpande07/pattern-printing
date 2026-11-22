# Print the upper half of the pyramid
for i in range(1, 6):
    # Print spaces and odd numbers of stars
    print("  " * (5 - i) + "* " * (2 * i - 1))

# Print the lower half of the pyramid
for i in range(4, 0, -1):
    # Print spaces and decreasing stars
    print("  " * (5 - i) + "* " * (2 * i - 1))