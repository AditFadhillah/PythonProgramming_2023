
print("Insert temperature in Kelvin:")
kelvin = input()
if kelvin.isdecimal():
    print("Temperature in Kelvin:", int(kelvin))
    ABSOLUTE_ZERO = -273.15
    celsius_convert = float(kelvin) + ABSOLUTE_ZERO

    print("Temperature in Celsius:", float(celsius_convert))
else:
    print("Please input a digit.")  
