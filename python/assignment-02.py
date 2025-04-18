# Given list
numbers = [1, 5, 6, 5, 1, 2, 3]

# Create a list for duplicates
duplicates = []

# Loop through the list
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Print the result
print("Duplicate elements:", duplicates)
