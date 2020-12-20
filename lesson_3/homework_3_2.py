# Enter a number between 1 and 20, save this value to number variable.
# If number is greater than 0 and less than or equal to 7, save the number * 10 to result_1.
# If number is  greater than 7 and less than or equal to 15, save the result of floor division of the number divided by
# 3 to result_1 variable
# If number is  greater than 15 and less than or equal to 20, save the number raised to the power 3 to result_1
# Else save the text "Wrong value" to result_1

number = int(input('Enter a number between 1 and 20: '))
result_1 = None
if 0 < number <= 7:
    result_1 = number * 10
elif 7 < number <= 15:
    result_1 = number // 3
elif 15 < number <= 20:
    result_1 = number ** 3
else:
    result_1 = 'Wrong value, hint: enter a number between 1 and 20 (included) next time'
print(result_1)


# Enter two numbers between 1 and 10, save this values to number_1 variable and number_2 variables.
# If number_1 and number_2 are greater than 0 and less than or equal to 5 save in the product of their multiplication
# to result_2
# If one of the variables (number_1 or number_2) is greater than 5 and less than or equal to 10, but the other isn't,
# then save the sum of the two numbers to result_2
# If both numbers are greater than 5 and less than or equal to 10, multiply their sum by 3 and save it to result_2
# Else save the text "Wrong values, try again" to result_2

number_1 = int(input('Enter the first number between 1 and 10: '))
number_2 = int(input('Enter the second number between 1 and 10: '))
result_2 = None

# SOLUTION 1

# if 0 < number_1 <= 5 and 0 < number_2 <= 5:
#     result_2 = number_1 * number_2
# elif 5 < number_1 <= 10 and 5 < number_2 <= 10:
#     result_2 = (number_1 + number_2) * 3
# elif 5 < number_1 <= 10 or 5 < number_2 <= 10:
#     result_2 = number_1 + number_2
# else:
#     result_2 = "Wrong values, try again. (Hint: Enter any random number in the range from 1 to 10 (included)"
# print(result_2)

# SOLUTION 2

# if 5 < number_1 <= 10 and 5 < number_2 <= 10:
#     result_2 = (number_1 + number_2) * 3
# elif 5 < number_1 <= 10 or 5 < number_2 <= 10:
#     result_2 = number_1 + number_2
# elif 0 < number_1 <= 5 and 0 < number_2 <= 5:
#     result_2 = number_1 * number_2
# else:
#     result_2 = "Wrong values, try again. (Hint: Enter any random number in the range from 1 to 10 (included)"
# print(result_2)

# SOLUTION 3
# if 0 < number_1 <= 5 and 0 < number_2 <= 5:
#     result_2 = number_1 * number_2
# elif 0 < number_1 <= 5 and 5 < number_2 <= 10 or 5 < number_1 <= 10 and 0 < number_2 <= 5:
#     result_2 = number_1 + number_2
# elif 5 < number_1 <= 10 and 5 < number_2 <= 10:
#     result_2 = (number_1 + number_2) * 3
# else:
#     result_2 = "Wrong values, try again. (Hint: Enter any random number in the range from 1 to 10 (included)"
# print(result_2)

# SOLUTION 4

if 0 < number_1 <= 5 and 0 < number_2 <= 5:
    result_2 = number_1 * number_2
elif 5 < number_1 <= 10 and not 5 < number_2 <= 10 or 5 < number_2 <= 10 and not 5 < number_1 <= 10:
    result_2 = number_1 + number_2
elif 5 < number_1 <= 10 and 5 < number_2 <= 10:
    result_2 = (number_1 + number_2) * 3
else:
    result_2 = "Wrong values, try again. (Hint: Enter any random number in the range from 1 to 10 (included)"
print(result_2)

# Enter your first name and save it to first_name variable,
# then Enter last name and save it to last_name
# If first_name or last_name are shorter than 6 characters, save a full name (with a space between) to result_3
# Else save first_name to result_3 as many times as length of last_name value

first_name = input('Please enter your First Name: ')
last_name = input('Please enter your Last Name: ')
result_3 = None
if len(first_name) < 6 or len(last_name) < 6:
    result_3 = f'{first_name} {last_name}'
    # result_3 = first_name + ' ' + last_name #ANOTHER OPTION
else:
    result_3 = first_name * len(last_name)
print(result_3)


# Enter a random number. Save this value to random_number variable
# If this number is less 10 or greater than 99, save the text "Please, put in a number between 10 and 99" to result_4
# If a number doesn't meet the first condition, find the remainder of random_value divided by 2.
# If it is 0, save the text "Even number" to result_4 , else save the message "Odd number"

random_number = float(input('Enter a random number please: '))
result_4 = None
# if 10 > random_number or 99 < random_number:
#     result_4 = 'Please, put in a number between 10 and 99'
if random_number < 10 or random_number > 99: # Option 2
    result_4 = 'Please, put in a number between 10 and 99'
# elif not 10 > random_number and not 99 < random_number:
#     result_4 = random_number % 2
# elif not random_number < 10 and not random_number > 99: # Option 2
#     result_4 = random_number % 2
else: # Option 3
    # if result_4 == 0:               # this one stays with option 1 and option 2 as a root if statement
    #     result_4 = 'Even number'    # option 1 and 2
    # else:                           # option 1 and 2
    #     result_4 = 'Odd number'     # option 1 nad 2
    if random_number % 2 == 0:
        result_4 = 'Even number'
    else:
        result_4 = 'Odd number'
print(result_4)
