"""
CP1404/CP5632 Practical
Basic list operations and security check
"""
# ----- Part 1: Basic List Operations -----

numbers = []  # Empty list to store numbers
# Prompt user for 5 numbers
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
    
# Display required information
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")