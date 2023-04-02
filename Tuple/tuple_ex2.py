a = (2,3,5,7,10,11,0,1)
# Sort this tuple and print out the result. 

# Can we change the order of items in a tuple? 
# No we cannot because tuples are immutable.

# If I can convert this tuple in to a list object, then I could sort it. 
#   HOW?
a = list(a)
print("Type of a is",type(a),f"and value of a is {a} on line 10")


a.sort()
print("Type of a is",type(a),f"and value of a is {a} on line 14")


a = tuple(a)
print("Type of a is",type(a),f"and value of a is {a} on line 18")