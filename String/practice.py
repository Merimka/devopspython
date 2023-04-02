#Ending index in the slicing is not included.
#If I up len()-1 as ending index in the slicing, the last
#character from the string will not be included in the sliced str.
#      01234 
str = "Hello"
print(str[0:len(str)])



string = "Python"
print(string.replace("Pyt","Java"))

# What should be the output of the code above?
#Javahon
print(string.replace("Java","Python"))

# Even tough the value we are trying to change doesn't exist in the 
#string the python will not generate an error but also
#will not change anything as well

number_of_students = 36
str = "Total number of student is " ,number_of_students
print(type(str))

