# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)

name_1 = 'Garnik'
result_1 = ''

# TODO: Here is your code
for my_name in range(3):
    result_1 += name_1 + ' '
print(result_1)
# times = 3
# for my_name in range(times):
#     result_1 = (name_1 + ' ') * 3
#     print(result_1)
# print(result_1)

# for my_name in name_1:
#     result_1 = (my_name + ' ') * 3
#     print(result_1)
#
# for result_1 in name_1:
#     print(result_1 * 3)
#
# result_1 = name_1
# while result_1 < (name_1 + ' ') * 3:
#     print(result_1)
#     result_1 = result_1 + ' ' + name_1
#
# repeated_times = 123
# for my_name in str(repeated_times):
#     result_1 = name_1
#     print(result_1)



# Ex. 2
# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
# (use loops)
name_2 = input('Enter your Name: ')
number_1 = input('Enter how many times you want your name to repeat: ')
result_2 = ''

# TODO: Here is your code
for repeated_name in range(int(number_1)):
    result_2 += name_2 + ' '
print(result_2)

# Ex. 3
# Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
# into result_3 variable

string_number_1 = input('Enter combination of random numbers that comes up to you mind: ')
result_3 = 0

# TODO: Here is your code
for digits in string_number_1:
    result_3 += int(digits)
print(result_3)

# Ex. 4
# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable

result_4 = 0

# TODO: Here is your code
for num in range(2, 100):
    if num % 2 == 0:
        result_4 += int(num)
print(result_4)

