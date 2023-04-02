# Range function with one parameter
print (range(5))
# The code above will give us numbers from 0 to 5 (5 is not included)
print(type(range(10))) # <class 'range'>

# Just check the first 5 index number of the string.
str ="table"
for index in range(5):
    print(str[index])

# Range function with 2 parameters
#range(1,4) ->1,2,3
#Print all the even number from 1 to 10 inclusive

for number in range(1,11):
    if number % 2 == 0:
     print(number)
print()


#NOTE: Indentation after while, for, if statement required, however
# indentation doesn't have to be 4 space.
# In order to make code more understandable and readable,
#it is best to use 4 space all time

# Range function with with 3 parameters.
# range(start,stop,step)
# range(2,11,2)
# Print all the even numbers from 1 to 10 inclusive

for number in range(2,11,2):
   print(number)















