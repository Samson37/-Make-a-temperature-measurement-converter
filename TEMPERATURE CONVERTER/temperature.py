def celsius_to_fahrenheit(celsius):
return (Celsius * 9/5) + 32 
def fahrenheit_to_celsius(fahrenheit):
 return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
 return celsius + 273.15
def kelvin_to_celsius(kelvin):
return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
 celsius = fahrenheit_to_celsius(fahrenheit)
return celsius_to_kelvin(celsius)
def kelvin_to_fahrenheit(kelvin):
celsius = kelvin_to_celsius(kelvin)
 return celsius_to_fahrenheit(celsius)

# Example usage
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C, F, K): ")
if unit.upper() == "C":
 fahrenheit = celsius_to_fahrenheit(temperature)
 kelvin = celsius_to_kelvin(temperature)
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)
elif unit.upper() == "F":
 celsius = fahrenheit_to_celsius(temperature)
 kelvin = fahrenheit_to_kelvin(temperature)
 print("Temperature in Celsius:", celsius)
 print("Temperature in Kelvin:", kelvin)
elif unit.upper() == "K":
 celsius = kelvin_to_celsius(temperature)
fahrenheit = kelvin_to_fahrenheit(temperature)
print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
else:
 print("Invalid unit. Please enter C, F, or K.")