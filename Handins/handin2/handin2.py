beatles_container1 = [("Paul McCartney", "bass guitar"),
                      ("John Lennon", "rhythm guitar"),
                      ("George Harrison", "lead guitar"),
                      ("Ringo Starr", "drums")]

beatles_container2 = {}
for name, instrument in beatles_container1:
    beatles_container2[name] = instrument

print(beatles_container2["Ringo Starr"])

def beatle_lookup(name):
    if name in beatles_container2:
        return beatles_container2[name]
    else:
        available_names = list(beatles_container2.keys())
        error_message = f"ERROR, Name '{name}' not found. Available names: {available_names}"
        return error_message
    
print(beatle_lookup("John Lennon"))
print(beatle_lookup("Mick Jagger"))