
# Let's create aunction that takes any count of number or numbers
# find sum off all given numbers.
# The function can get 4 number parameter or 12
# In order to be flexible with amount of value(parameters),
# we could take we will use * symbol before the name.

def find_sum(*numbers):
    print(type(numbers)) # tuple
    # I should treat this numbers  variable as a tuple
    # In the tuple how can i find the sum of the all numbers.
    sum = 0
    for num in numbers:
        sum +=num
    return sum
print(find_sum(30,20))     















