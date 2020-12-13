# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'This is the first string using single quotes'
result_string_2 = "This is the second string using double quotes"
result_string_3 = '"This is the third string using combo of single and double quotes"'
result_string_4 = f'You can also use (f\') formatting to create a string with inserts like this \"\U0001F913\" nerd face'
print(result_string_1)
print(result_string_2)
print(result_string_3)
print(result_string_4)


# Enter your first and  last name. Join them together with a space in
# between. Save a result in a variable result_full_name and
# save the length of the whole name in result_full_name_length variable.

first_name = input('Please enter Your First Name: ')
last_name = input('Please enter Your Last Name: ')
result_full_name = first_name + ' ' + last_name
result_full_name_length = len(result_full_name)
print(f'Thank you {result_full_name} for entering your Full Name')
print(f'The full_name variable length that Python sees is {result_full_name_length}, but Your Full Name character count is actually {result_full_name_length - 1} \U0001F913')


# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

result_ca_capital = f'sacramento'.title()
print(result_ca_capital)
# or
ca_capital = 'sacramento'
result_ca_capital_old_option_long = ca_capital.title()
print(result_ca_capital_old_option_long)
# or
result_ca_capital_old_option_faster = 'sacramento'.title()
print(result_ca_capital_old_option_faster)
# or you can simply ask user to enter any city lower case and convert it to a Title
result_any_city_coolest = f'{input("Type any city name in a lower case please: ")}'.title()
print(result_any_city_coolest + ' ' + '\U0001F913')

# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable

result_planet = 'Earth'.upper()
print(result_planet)
# or
result_planet_f_str = f'Earth'.upper()
print(result_planet_f_str)
# or
our_planet = 'Earth'
result_planet_var_long = our_planet.upper()
print(result_planet_var_long)
# or with any other planets (for some reason I really like the idea of getting user inputs)
result_any_planet_user_input = f'{input("Please enter any planet: ")}'.upper()
print(result_any_planet_user_input + ' ' + '\U0001F913')
