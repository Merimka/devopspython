
numbers = [2, 5, 8, 3, 6, 4, 1, 7, 0, 9, 2, 5, 6, 1, 8]
numbers.sort()
# We should find all pairs of numbers that add up to 9.
# At the end of the task, we should only print unique pairs.
# such as
#
# Print all the value from this list using indexes.
set_obj = set()
for index in range (len(numbers)):
    print(numbers[index])
    for index2 in range(index+1,len(numbers)):
        # In this loop value of numbers[index] won't change
        if numbers[index] + numbers[index2] == 9:
            my_pair = (numbers[index2],numbers[index])
            set_obj.add(my_pair)
print(set_obj)







