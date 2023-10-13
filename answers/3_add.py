# Task 3 - Add
# Write a program that asks for two numbers, and then adds them together
# It should be able to cope with invalid numbers and ask again

def get_number():
    while True:
        number_str = input("Write a number: ")

        try:
            return int(number_str)
        except ValueError:
            print("That's not a number!")


first_number = get_number()
second_number = get_number()
print(first_number + second_number)
