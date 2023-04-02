"""
Write a Python program that calculate the total value of a certain
number of quarters,dimes,nickels,and pennies,
and then prints the total value in dollars.
"""
# 1- we have give the value of quarters,dimes,nikels,pennies
# 2- Then we need a total_cents collection
# 3- Result has to be in dollars,total_cents convert to total_dollars

quarters =int(input("Enter quarters count: ")) #3
dimes = int(input("Enter dimes count: "))   #2
nickels = int(input("Enter nickels count: ")) #1
pennies= int(input("Enter pennies count: "))  #4  #output 1.04

total_cents = quarters*25 + dimes*10 + nickels*5 + pennies 
total_dollars = total_cents/100
print("The total value is :\"$",total_dollars,"\"")
 


