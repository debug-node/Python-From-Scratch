# Create three lists representing the three rows of the map
Line1 = [" ", " ", " "]  # Row 1
Line2 = [" ", " ", " "]  # Row 2
Line3 = [" ", " ", " "]  # Row 3

# Combine the three rows into a single list (2D map)
map = [Line1, Line2, Line3]

print("Hiding your treasure! X marks the spot.")

# Ask user for input (example: "a1" or "c3")
position = input()

# Extract the letter (column) and convert to lowercase
letter = position[0].lower()

# Create a list for column reference
abc = ["a", "b", "c"]

# Find the index of the letter (a=0, b=1, c=2)
letter_index = abc.index(letter)

# Convert the number from string to int and adjust for 0-based index
number_index = int(position[1]) - 1

# Place the "X" at the correct position on the map
map[number_index][letter_index] = "X"

# Print the updated map
print(f"{Line1}\n{Line2}\n{Line3}")
