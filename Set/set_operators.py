#  set union method -> will combine elements of both sets.

s1 = {1,3}

s2 = {"str1","str2"}
new_set = s1.union(s2)
print(new_set)  # {1,3,str1,str2}

print(s1) # It is not change after union method 
print(s2) # It is not change after union method


###  set intersection method  -> will return only common elements from both
#sets
new_set = s1.intersection(s2)
print(new_set)

# NOTE: Empty set in python is not shown with empty braces,
# empty set is represented be set function.
# The reason for that is empty braces in python represents a dictionary
# object.


### difference method 
# will return different elements from both sets as a new set.

s1 = {1,3}
s2 = {"str1","str2"}

# The method below will return elements that is in the
# s1 both not in s2
new_set = s1.difference(s2)
print(new_set)


























