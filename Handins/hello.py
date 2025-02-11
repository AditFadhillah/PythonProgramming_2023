print("Hello, World!") # Python 3

print("")
# square of the average of all prime numbers between 0 and 10 
x = ((2+3+5+7)/4.0)**2
print(x)

print("")
print(7/2)           # python2: integer division. python3: no problem
print(7/2.0)         # normal division
print(7/float(2))

print("")
x = 3
y = 4
print(x < y)
print(x > y)
print(x == y)

x = 4
x += 1   # same as x = x+1
x -= 2   # same as x = x-2
x *= 3   # same as x = x*3
x //= 2  # same as x = x//2
x **= 2  # same as x = x**2
x %= 5   # same as x = x%5

print("")
x = 1
print((x > 0) and (x < 10))
print((x > 0) or (x < 10))
print((x > 0) and (x > 10))

True and True   # -> True
True or True    # -> True'
True and False  # -> False

print("")
print(4+6 / 2) # missing parentese for 4+6

print("")
x = 4
x += 1
x -= 2
x *= 3
x //= 2
x **= 2
x %= 5
print(x) # the program calculate all the previous statements

print(not (not (x > 0) or not (x < 10)))
