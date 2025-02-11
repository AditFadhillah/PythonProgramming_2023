def kelvin_to_celsius(temperature):
    temperature = temperature - 273.15
    print(temperature)

def kelvin_to_fahrenheit(temperature):
    temperature = (temperature - 273.15) * 9/5 + 32
    print(temperature)

if __name__ == "__main__":
    temperature = input("Temperature in Kelvin: ")
    if temperature.isdigit():
        temperature = int(temperature)
        kelvin_to_celsius(temperature)
        kelvin_to_fahrenheit(temperature)
    else:
        print("Please input a digit.")  
