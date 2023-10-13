# Task 2 - Process Files
# Write a program that reads the file lines.txt and prints the lines with a > in front of them
# Input: > Ben
# Output: Hello, Ben!

with open("lines.txt") as f:
    text = f.read()

lines = text.splitlines()

output = ""
for line in lines:
    output += f"> {line}\n"


with open("output.txt", "w") as f:
    f.write(output)
