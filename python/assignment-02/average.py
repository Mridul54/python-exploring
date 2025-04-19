# Write a function that takes two numbers as input and returns their average. Call the function with different values.
def average(a, b):
    return (a + b) / 2

# two input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# functions call and print the result
result = average(num1, num2)
print("The average is:", result)

