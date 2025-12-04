celsius_temperature = float(input("What is the temperature? °C: "))

fahrenheit_temperature = (celsius_temperature * 1.8) + 32
kelvin_temperature = celsius_temperature + 273.15

print(f"Fahrenheit Temperature is: {fahrenheit_temperature} °F")
print(f"Kelvin Temperature is: {kelvin_temperature} K")
