# Ask user to give two string values and 
# print True if the second string starts with 
# last two charachters 
# of the first string OR print True 
# if the first string starts with
# first two charachters of the second string.

value_1 =input("Enter a first string: ")
value_2 =input("Enter a second string: ")
last_two_value_1=value_1[-2:]
# Last two char of the value2
condition = value_2.startswith(last_two_value_1)
#first two charachters of the second string.
first_two_value_2 = value_2 [:2]
condition2 = value_1.startswith(first_two_value_2)

end_result = condition or condition2
print(end_result)





