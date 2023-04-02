# Create a function that returns average of numbers from given list.
# When we are calculating the average we shouldn't include
# largest and smallest element in the list.
# If the largest or smallest number duplicated just not use one copy

# Fact1: In order to find the average we have to find sum of each element
# in the list, then divide the sum by length of the list.
# Fact2: If I sort element in a list, first element will be 
# smallest, and last element will be largest element.



def find_average(numbers):
    numbers.sort()
    numbers.pop(0)
    numbers.pop(len(numbers)-1)
    sum = 0
    for num in numbers:
        sum = sum + num
    avg = sum / len(numbers)
    return avg

list = [12,7,9,3]
print(f"avarage of list is {list} is",find_average(list))





























