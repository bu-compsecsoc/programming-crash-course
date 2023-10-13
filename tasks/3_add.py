# Task 3 - Add
# Write a program that asks for two numbers, and then adds them together
# It should be able to cope with invalid numbers and ask again

try:
    number_str = input("Write a number: ")
    number = int(number_str)
except ValueError:
    print("That's not a number!")
