
# Let's say we want to include another value of the variable in a string
# This variable could be different data type such as int,float etc,


number_of_student = 34
description = "Total number of student is {}"
print(description)

#Curly braces didn't have any function in this case.
#just printed as it is in the string.

#let's use format method

print(description.format(number_of_student))
#Total number of students is 34

number_of_teachers = 3
ratio_description = "Total number of students is {} and number of teachers is {}"
print(ratio_description.format(number_of_student,number_of_teachers))
#Total number of students is 34 and number of teachers is 3


#NOTE: The braces in the formatted string can be indexed and they will get the parameters
#in order of their index numbers

ratio_description = "Total number of students is {1} and number of teachers is {0}"
print(ratio_description.format(number_of_teachers,number_of_student))
# Total number of students is 34 and number of teachers is 3


# We can format the string using f-string
student_name = "Jonh"
print(f"The name of student is {student_name}")

number_of_fruits = 10
str = f'The number of fruits we have is {number_of_fruits}'
print(str)





