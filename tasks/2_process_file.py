# Task 2 - Process Files
# Write a program that reads the file lines.txt
# It then adds "> " to each line
# Then saves it to output.txt

FILEPATH = "./tasks/lines.txt"
with open(FILEPATH) as f:
    text = f.read()

# Reads the lines.txt into the program
