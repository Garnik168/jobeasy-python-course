# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

# type your code here
temperature_fahrenheit = float(input("Enter your Temperature in Fahrenheit: "))
result_temperature = (temperature_fahrenheit - 32) * 5 / 9
print(result_temperature)
# or easier
result_temperature_f_string = (float(input("Enter your Temperature in Fahrenheit: ")) - 32) * 5 / 9
print(f'Your temperature in Celsius is {result_temperature_f_string}\U000000B0')
