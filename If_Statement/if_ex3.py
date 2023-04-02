# Ask user to give you two integer numbers. 
# Find the sum of these two integer numbers. 
# If sum of these two integer is smaller than 10 
# print sum of these two numbers is 10 
# if sum of these two number is between 10 - 19 inclusive, 
# print sum of these two numbers is 20
# For all other conditions 
# print the actual sum of these two numbers.

users_number1 = int(input("Please enter a number: "))
users_number2 = int(input("Please enter a number: "))
#sum_of_two = users_number1 + users_number2
if users_number1 + users_number2 < 10 :
    print("Sum of these two numbers is 10")
elif 10 <= users_number1 + users_number2 <= 19:  # 10<=sum_of_two<=19:
    print("Sum of these two numbers is 20")

else:
    print("Sum of these two numbers is ",(users_number1+users_number2))
    #print(f"Sum of these two numbers is {sum_of_two}")




