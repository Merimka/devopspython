# Reverse a given string using for loop with range function
# Don't use slicing the string

str = input("Enter a string: ")
# Let's just get each index number in string
# 0 to last_index
# 0  to len(str)-1
#NOTE: When negative step is used for range function,start and 
# stop points should reversed. We still have to keep in mind that
# starting index is included and ending index is not.

for index in range(len(str)-1,-1,-1):
    print(str[index],end=" ")
print()

#012345
#python






