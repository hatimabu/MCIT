import my_temperature
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
converted_to_fahrenheit = my_temperature.celsius_to_fahrenheit(celsius_input)
converted_to_celsius = my_temperature.fahrenheit_to_celsius(fahrenheit_input)
print(f"{celsius_input}°C is {converted_to_fahrenheit:.2f}°F")
print(f"{fahrenheit_input}°F is {converted_to_celsius:.2f}°C")