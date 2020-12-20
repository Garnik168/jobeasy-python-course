# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

first_number = float(input('Enter Your First number for comparison: '))
second_number = float(input('Enter Your Second number for comparison: '))
result_1 = None
if first_number > second_number:
    result_1 = first_number
    print(result_1)
else:
    result_1 = second_number
    print(result_1)

# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.

number_1 = float(input('Enter a random number please: '))
result_2 = None
if number_1 >= 20:
    result_2 = 'Too High'
    print(result_2)
else:
    result_2 = 'Tank you'
    print(result_2)


# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = input('Please enter Your First Name: ')
last_name = input('Please enter Your Last Name: ')
result_3 = None
if len(first_name) < 5:
    result_3 = first_name + last_name
    result_3 = result_3.upper()
    # print(result_3.upper())
    print(result_3) # remove if the print is out of the IF statement
else:
    result_3 = first_name + ' ' + last_name
    result_3 = result_3.lower()
    # print(result_3.lower())
    print(result_3) # remove if the print is out of the IF statement
# print(result_3) # or just like that

# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = float(input('Please enter a number between 10 and 20 (inclusive): '))
result_4 = None
if 10 <= number_2 <= 20:
    result_4 = 'Thank you'
    # print(result_4)
else:
    result_4 = 'Incorrect answer'
    # print(result_4)
print(result_4) # or here or repeat after each statement to see printed results


# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = int(input('Enter your age: '))
result_5 = None
if age >= 18:
    result_5 = 'You can vote'
    print(result_5) # for every condition separate or one but outside of the conditions
elif age == 17:
    result_5 = 'You can learn to drive'
    print(result_5) # for every condition separate or one but outside of the conditions
elif age == 16:
    result_5 = 'You can buy a lottery ticket'
    print(result_5) # for every condition separate or one but outside of the conditions
elif age < 16:
    result_5 = 'You can go Trick-or-Treating'
    print(result_5) # for every condition separate or one but outside of the conditions
# or hash the last elif statement and do else instead
# else:
#     result_5 = 'You can go Trick-or-Treating'
#     print(result_5) # for every condition separate or one but outside of the conditions
# print(result_5) # or this at the end outside of the conditions or every condition separate


# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = int(input('Enter a number between 1 and 12: '))
result_month = None
if month == 1:
    result_month = 'January'
    result_month = result_month.lower()
    print(f'{month}\'st month is {result_month}')
elif month == 2:
    result_month = 'February'
    result_month = result_month.lower()
    print(f'{month}\'nd month is {result_month}')
elif month == 3:
    result_month = 'March'
    result_month = result_month.lower()
    print(f'{month}\'rd moth is {result_month}')
elif month == 4:
    result_month = 'April'
    result_month = result_month.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 5:
    result_month = 'May'.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 6:
    result_month = 'June'.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 7:
    result_month = 'July'.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 8:
    result_month = 'August'.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 9:
    result_month = 'September'.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 10:
    result_month = 'October'.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 11:
    result_month = 'November'.lower()
    print(f'{month}\'th month is {result_month}')
elif month == 12:
    result_month = 'December'.lower()
    print(f'{month}\'th month is {result_month}')
else:
    print('Incorrect input, try again. Hint: you should enter any whole number from 1 to 12 (included)')
