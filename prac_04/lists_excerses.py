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