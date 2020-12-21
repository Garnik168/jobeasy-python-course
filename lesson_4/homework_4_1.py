# Save to variable result_1 the first character of string_1 variable. In result_2 save the last character
# of string_1. Use indexes.

string_1 = 'Python'
result_1 = string_1[0]
result_2 = string_1[-1]
print(result_1)
print(result_2)


# Save to variable result_3 string value from string_2 variable, written in reverse order, using concatenation.

string_2 = 'Python'
result_3 = string_2[-1] + string_2[-2] + string_2[-3] + string_2[-4] + string_2[-5] + string_2[-6] # I guess this is what required
# result_3 = string_2[5] + string_2[4] + string_2[3] + string_2[2] + string_2[1] + string_2[0] # could also be done like this
# result_3 = string_2[::-1] # Fastest, reverse with slicing
print(result_3)




# Slice string string_3 from 5th to 20th (excluding 20th) character and save the result to variable result_4

string_3 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_4 = string_3[4:19]
print(result_4)


# Slice string string_4 from 10th character to the end of the string. Save only every second character to variable
# result_5

string_4 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_5 = string_4[9::2]
print(result_5)

# Slice string string_5 from the first to the last character, save only every forth character and
# save the result to variable result_6

string_5 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_6 = string_5[::4]
print(result_6)


# Slice string string_6 from the first to 14th (including 14th) character, save only every third character and save
# the result to variable result_7

string_6 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_7 = string_6[0:14:3]
# result_7 = string_6[:14:3]
print(result_7)


# Save to variable result_8 string value from string_7 variable, written in reverse order, using slicing.

string_7 = 'Python'
result_8 = string_7[::-1]
print(result_8)


# Create a range of numbers from 0 to 10 (excluding 10) and save it to result_9 variable

result_9 = range(10)
print(result_9[0])
print(result_9[1])
print(result_9[2])
print(result_9[3])
print(result_9[4])
print(result_9[5])
print(result_9[6])
print(result_9[7])
print(result_9[8])
print(result_9[9])
# Second Solution
# result_9 = list(range(10))
# print(result_9) # casted to the list

# Third Solution
# for numbers in range(10):
#     result_9 = numbers
#     print(result_9) # range trough for loop