message = "Hello, world!"       # Create string variable
print(len(message))             # Len returns the length of a string

f = open("message.txt", 'w')    # Opening file. There is a cleaner way of doing this, which we will see later in the course.
f.write(message)                # Using the .write method on the File object to write a string to the open file
f.close()                       # Closing file.
