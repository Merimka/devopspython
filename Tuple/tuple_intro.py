# Tuples are immutable storages for python. We could memorize them as
# immutable brother of list.

# To create a tuple we could use one of tree ways below.

# Generic -----------------------------------------------
nums =(1,2)

# Without paranthesis -> We could just separate value with comma

nums = 1,2

# We could use tuple() function to create tuples
# List of objects
list_of_elements = ["str",[],{}]
# I want to create a tuple out of list, regardless of what is stored in a list.
tuple_of_elements = tuple(list_of_elements)
print(type(tuple_of_elements))

# Accessing elements
# In order to access elements, we can use index numbers

words = ("word1","word2")
#print(words[3]) -> What would this line print? IndexError
#to print all elemenrs from a tuple, (to access and maybe do some implementations with #each element) we could use loop

# Easiest way loop in a tuple would be using for loop.
tuple_values = (1,2,3,4,3,5,3)








