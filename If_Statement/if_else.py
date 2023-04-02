# If the given grade for student is A print
# "that's an excellent grade."
# If the given grade for students is B print
# "That's a good grade."
# In all other grades just print
# "Your grade should be improved."

# Only one of the above condition can be True
# That's why best practice would be combining all in one if-else statement

grade = input("Please enter your grade letter: ->").upper()  # if user gives lower case
# We used .upper method after the input becausee in our if statement
#we are expecting grade text to be given in an upppercase letter.
#any input will be converted to upper case so that our code can worj in both situation.



if grade == 'A':
    print("That's an excellent grade.")
elif grade == 'B':
    print("That's a good grade.")
else:
    #When the grade is not  A nor is B, then this else statement gets executed.
    print("Your grade should be improved.")

#Python way of saying in 'all other condition' is using else statement.
# Else statement gets executed when all previous conditions are False.

# What happens when use enter a lower case grade?
















