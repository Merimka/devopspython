# Ask user to enter a string.
# Print the length of string.
# print the 4th letter of the of the string



str = input("Please,enter a string")
print("The leghth of the text you have entered is",len(str))
print("The 4th letter of the text you have entered is",str[3])


# When the index number you are trying to access doesn't exist in str
# python will generate IndexError

#Print the last character from the given string without negative
#indexing.    012345
#Example     "STRING"
#             123456
#There are 5 characters in the string and last index is 4
#Last index can be found by subtracting 1 from the length of string.
#len(str)-1 will always result in last index from the string

print("The last character you have entered is ",(len(str)-1))
#print(str[-1]) # to find last character




