# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1: float, num_2: float):
    return num_1 - num_2
print(difference(25, 18))

# Division
# Write a function, which will divide these two numbers

def division(num_1: float, num_2: float):
    if num_2 == 0:
        return f'Can\'t divide by zero'
    else:
        return num_1 / num_2
print(division(10, 0))


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number: int):
    if number > 10:
        return 100 - number
    else:
        return number * 10
print(function_1(5))
print(function_1(25))

# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temerature_convertor(fahrenheit_degree: int):
    return f' {round((fahrenheit_degree - 32) * 5/9)}°C \U0001F913'
print(temerature_convertor(32))
print(temerature_convertor(75))
print(temerature_convertor(20))



# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    distance_meters = distance * 1000
    price_per_meter_count = distance_meters / 140
    price_per_meter = price_per_meter_count * 0.25
    return f'\U00000024 {price_per_meter.__round__(2) + 4.00} \U0001F913'
print(taxi_fare(10))
print(taxi_fare(250))
print(taxi_fare(5))

def taxi_fare_two(distance: float):
    return round(4.0 + ((distance * 1000) / 140) * 0.25, 2)
print(taxi_fare_two(10))

# examples of usage:
# taxi_fare(10) #21.86