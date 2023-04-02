# List are iterable object. Therefore they can easyly be used with for
# loop

# for name in iterable_object:
#       print(name) #this would print each element from given iterable object


list = ["str1",'str2',3,4,5.6]
for item in list:
    print(item)

# Print only string object from given list.

for element in list:
    #print(type(type(element)))
    if type(element) == str:  # doesn't represent an object or variable,it represent str #file in python
        print(f"string object {element}")

# print only integer object from given list

for element in list:
    if type(element) == int:
        print(f"integer object {element}")

