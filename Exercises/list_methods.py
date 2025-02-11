# Define the initial list
capitals = ["Amsterdam", "Tokyo", "London", "Cape Town"]

# Print the full list
print(capitals)

# Print the first item of the list
print(capitals[0])

# Add "Paris" to the end of the list and print the updated list
capitals.append("Paris")
print(capitals)

# Print a range of indexes 1 to 3 of the list
print(capitals[1:3])

# Reverse the items of the list and subsequently print the updated list
capitals.reverse()
print(capitals)

# Add "Cape Town" to the end of the list and print the updated list
capitals.append("Cape Town")
print(capitals)

# Count the number of times "Cape Town" is in the list and print the result
count_cape_town = capitals.count("Cape Town")
print(count_cape_town)

# Remove the first occurrence of "Cape Town" from the list
capitals.remove("Cape Town")

# Print the length (number of items) of the list
print(len(capitals))

# Add the number 100 to the front of the list (index 0) and print the list
capitals.insert(0, 100)
print(capitals)

# Update the value of the first item (current value 100) to "Washington" and print the list
capitals[0] = "Washington"
print(capitals)

count = capitals.count("Cape Town")
print(count)

capitals.extend(["Jakarta", "Beijing"])
print(capitals)

index = capitals.index("Tokyo")
print(index)

capitals.pop(3)
print(capitals)

capitals.sort()
print(capitals)

capitals.clear()
print(capitals)

""" 
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

"""