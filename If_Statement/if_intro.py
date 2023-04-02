
b = False
if b:
    print("The condition given is True")

print("There is no indentation so this line not effective by if")

#NOTE: Anything that returns(gives) boolean cab be put after if.
if True:
    print("This is line #1")
    print("This is line #2")
    print("This is line #3")

#Whenever we use comparison operators they will give us a bool value,
# Therefore,  we could use comparison operators after if keyword.
"""
if True:
    print("This is line #1")
    print("This is line #2")
    print("This is line #3")

    print("This is line #5")
print("This is line #6")
    print("This is line #7") ##unexpected indent
"""
#What will be the output of the code above?
# This will generate an error.

#Indent a lines want to belong a certain control
#flow statement or methods. Such as if,while,for def(methods) etc.

if True:
    print("This is line #1")
    print("This is line #2")
    print("This is line #3")

    print("This is line #5")
    print("This is line #6")
# Which  line be printed? 
# line#1,2,3,4,5,6

if False:
    print("This is line #1")
    print("This is line #2")
    print("This is line #3")

    print("This is line #5")
print("This is line #6")

# Which  line be printed? 

#Only line # 6 will be printed,because it is not effected by if.


