
# Parameters are the datas that are given for a function(method),
# in that function usually implementations are done according to
# parameters.

# create a method that takes one parameters as a full_name
# and returns upper case version of that parameter.

def upper_case_name(full_name):
    return full_name.upper()

# string is immutable
name = "John Jessie"
print(upper_case_name(name))  # upper case of the name JOHN JESSIE

new_variable = upper_case_name(name)
print(new_variable) # JOHN JESSIE
print(name) # "John Jessie"

# Our method takes one parameter at a time, since two is given below,
# it will generate an error.
#upper_case_name("Saul Goodman","Yusuf Turan")

# Number of parameters given to fuction should exactly match.
# therefore, code below generate an error.
# upper_case_name()








