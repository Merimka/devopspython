# Ask user fahrenheit is the weather ? If weather is below 32F
#print "It is freezing outside!!!", otherwise print
#"it is not bad weather for Chicago"

weather = int(input("What is the in Fahrenteint: "))
if weather > 32:
    print("it is not bad weather for Chicago")
elif weather < 32:
    print("It is freezing outside!!!")


# Is there a possibility that weather is bigger than and also smaller 
# than 32?
#Since only one of the if statement above can be true,
# It is BEST practice to combine these two if statements.


# Elif will get executed ONLY when the previous condition are false;
# if condition before the elif is True the python interpreter,
# will not check the elif statement. Which result in smoother, 
# and more efficient programming.








