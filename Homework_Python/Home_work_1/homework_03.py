"""
Write a Python program that has a variable called inches. Next,
convert that variable to meters, and then print the result as meters.

Note: One inch is equivalent to 0.0254 meters.

For example, if the variable is 50 inches, the program should convert it 
to meters using the conversion factor 0.0254, resulting in a 
length of 1.27 meters, and then print the result as "1.27 meters".
Note: Your code should be able to work even the value of inch 
variable changes.
"""
var_inches = int(input("Enter a variable as inches: ")) # User gives var_inches
var_meters = var_inches * 0.0254   # Convert to inch to meter
print("The result in meters is \"",var_meters,"meters\"")





