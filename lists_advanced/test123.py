# Generate a pyramid pattern with asterisks
height = 7  # Adjust the height of the pyramid as needed

for i in range(height):  # Outer loop for each row
    # Print leading spaces
    for _ in range(height - i - 1):
        print(" ", end="")

    # Print asterisks for this row
    for _ in range(2 * i + 1):
        print("*", end="")

    # Move to the next line after completing the row
    print()
