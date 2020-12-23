# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'This is totally random, hopefully long enough string, that contains different characters, that I can work with'
char_1 = input('Enter the character that you want to count: ')
result_1 = 0
current_index = 0
while current_index < len(string_1):
    if string_1[current_index] == char_1:
        result_1 += 1
    current_index += 1
else:
    print(f'Current index is at it\'s last position # {current_index}, the loop has stopped.')
print(f'The character {char_1} occurs {result_1} times \U0001F913')


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 12345
result_2 = 1
index = 0

while index < len(str(number_1)):
    result_2 = result_2 * int(str(number_1)[index])
    index += 1
print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 12345
result_3 = ''
index_2 = len(str(number_2)) - 1

while index_2 >= 0:
    result_3 = str(result_3) + str(number_2)[index_2]
    index_2 -= 1
result_3 = int(result_3)
print(result_3)
# print(int(result_3)) or just this instead of previous 2 if you don't need to save the result as int
