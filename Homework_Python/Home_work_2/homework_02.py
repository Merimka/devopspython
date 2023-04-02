"""
Ask user to enter any string value using input function.
Then, remove ALL THE SPACES (" ") from the given string.
After removing the spaces from the string,
If the string's length is odd print True, otherwise print False.
Example:
Input : I love coding
Output: True
Input : one two
Output: False
"""
users_string = input("Enter a string:")
after_remove_spaces = users_string.replace(" ","")

if len(after_remove_spaces) % 2 == 1:
    print(True)
else:
    print(False)
print(len(after_remove_spaces))









