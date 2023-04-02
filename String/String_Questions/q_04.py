# Ask user to give two differnt string values
# If the first strng contains the second string
# print True, if not print False.



str1 = input ("Enter the first string value: ") #table
str2 = input ("Enter the second string value: ") #this is a nice table 

# How can I find if str1 contains str2 ?
# We simply add two string together withv space in between. Then
# assign it to anothee strin variable.
#str3 = str1 + " " + str2 #it's not gonna work

# We found number of the first string in the second string.
# If the str2 is in str1 the count of str2 in str1 should be bigger
# than 0
condition = str1.count(str2) == 1
print(condition) # False





