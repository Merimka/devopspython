#Ask user to enter a string and print a rotated
#Left 2 version where the first 2 characters
# of the string moved to the end.
#'Hello' -> 'lloHe'
#'mute' -> 'temu
#"techtorial"->'chtorialte'


# input function allow us to get value when we run code rather than
# giving in the begining of coding.
# Using input function we can get string variables, which will help
# us to work with dymanic values.

user_string =input("Enter a string value: ")
#First two characters from the given string

first_two = user_string[0:2]
rest_of_str = user_string[2:]
end_result = rest_of_str + first_two
print("Rotated left 2 version of variable str is",end_result)










