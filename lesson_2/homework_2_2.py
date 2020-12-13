# Change result_string_1 that 'very simple language' will be displayed on a new line

result_string_1 = 'Python is the \nvery simple language'
print(result_string_1)


# Change result_string_2 to print out the phrase: 'What does the word 'integer' mean'

result_string_2 = "What does the word 'integer' mean"
print(result_string_2)


# Assign number variable to value "5" (as a string). Then rise the number to the power 3.
# Save the expression to result_value variable

number = "5"
result_value = int(number) ** 3
print(result_value)
# or
number_2 = "5"
result_value_2 = pow(int(number_2), 3)
print(result_value_2)


# Enter a random number, then save the value to n variable.
# Finally, you should repeat the variable "word" n times and save the value to result_string_3

n = 11
word = 'super'
result_string_3 = word * n
print(result_string_3)
# or better looking version
result_string_3 = (word + ' ') * n
print(result_string_3)
# or
n_2 = int(input('Enter how many time you want to see "I love You": '))
word_2 = 'I love You'
result_string_4 = (word_2 + ' ') * n_2 + '\U0001F913'
print(result_string_4)
