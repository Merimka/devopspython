"""
Write the program to get the string value from the specified
position. First, ask the user to enter one String value. Then
ask the user to the enter starting number and ending number.
After that, print the value between the given starting and ending
numbers. (Note: since the user does not know the python, the user
starts counting from 1, and the ending number will be included)
Example:
Please enter the String value:
Definition of Science
Please enter the starting number:
2
Please enter the ending number:
5
The output is:
efin
"""
users_string_value = input("Enter a string: ")
users_starting_number=int(input("Enter a starting number: "))
users_ending_number = int(input("Enter a ending number: "))
users_starting_number -= 1
users_ending_number -= 1
result = users_string_value[users_starting_number:users_ending_number+1]
# Print the result
print(f"The output is: {result}")









