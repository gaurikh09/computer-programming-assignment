# Write a function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
