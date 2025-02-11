# create variable
message = "Hello, world!"

# print the length of the string
print(len(message))

# open an output file and print the string to the file
with open("message.txt", "w") as file:
    file.write(message)

