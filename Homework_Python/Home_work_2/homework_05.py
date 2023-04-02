"""
Using an input function enter three different ingredients for the product
on the same line. Then ask the user to enter any int number. Change 
the first letter of the ingredients starting from the entered number.
(Ingredients should start with different letters. Please read the example 
carefully )
Example 1:
Please enter three ingredients with spaces:
Milk Peanuts Butter
Please enter the int number:
5
The output is:
5ilk 6eanuts 7utter

Example 2:
Please enter three ingredients with spaces:
Sugar Cocoa Oil
Please enter the int number:
3
The output is:
3ugar 4ocoa 5il
"""

ingredients = input("Enter three different ingredients for the product: ")
int_users =int(input("Enter a number: "))
new_final = ingredients.replace(ingredients[0:1],str(int_users)).replace(ingredients[ingredients.find(' ')+1],str(int_users+1)).replace(ingredients[ingredients.rfind(' ')+1],str(int_users+2))
print("The result of: ",new_final) 














