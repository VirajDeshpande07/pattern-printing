# Print the upper half of the butterfly
for i in range(1, 6):
    # Print stars on both sides with spaces in the middle
    print("* " * i + "  " * (2 * (5 - i)) + "* " * i)

# Print the lower half of the butterfly
for i in range(4, 0, -1):
    # Decrease stars and increase middle spaces
    print("* " * i + "  " * (2 * (5 - i)) + "* " * i)