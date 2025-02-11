# Q1. Create a list of tuples
beatles_container1 = [("Paul McCartney", "bass guitar"),
                      ("John Lennon", "rhythm guitar"),
                      ("George Harrison", "lead guitar"),
                      ("Ringo Starr", "drums")]

# Q2. Put the same content into a dictionary
beatles_container2 = {}
for entry in beatles_container1:
    beatles_container2[entry[0]] = entry[1]

# Q2. Alternative solution:
beatles_container2 = dict(beatles_container1)

# Q3. Putting the code into a function
def beatle_lookup(name):

    # Simplified version of code above
    beatles_container2 = dict([("Paul McCartney", "bass guitar"),
                               ("John Lennon", "rhythm guitar"),
                               ("George Harrison", "lead guitar"),
                               ("Ringo Starr", "drums")])

    # Check whether name exists as key in dictionary
    if name in beatles_container2:
        return beatles_container2[name]
    else:
        return "Name '{}' not found. Available names: {}".format(name, list(beatles_container2.keys()))


# Test beatle_lookup function 
print(beatle_lookup('Paul McCartney'))    
print(beatle_lookup('Mick Jagger'))
