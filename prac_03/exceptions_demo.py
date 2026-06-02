"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
if the value of the numerator is not integer
2. When will a ZeroDivisionError occur?
if the denominator is equal to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes i have done it in a code
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Not possible")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")