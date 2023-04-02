# We need to write a program to give most efficuent
# coin exchange for given dollar amount.
# Such as if we need to convert
# 1 dollar in to a coin exchange you would 4 quarters.
# Coin values
#quarters is 25 cents
#dime is 10 cents
# nickle is 5 cents
# penny is one cent



## Pseudo Code
# Directions on how to solve this question
  # 1 First create variables for each coin
  # 2 To use a single unit (i will convert given amount in to cents)
  # 3 I should start finding with biggest coin value which is quarter
  # 4 In order to find amount of quarter that I have in given amount
  # I should floor divide given_amount with quarter variable 
  # 5 Find remaining_value after quarters
  # 6 I should find amount of dime that I have in remaining after quarters
  # 7 Find remaining after dimes then find amount of nickles
  # 8 Find reamining after nickles that would amount of pennies


given_amount = 3.67
total_cents=int(given_amount * 100)  #367

# I have to find amount of quarter
q = 25 # quarter
amount_of_quarter = total_cents //q
remainder_after_q = total_cents % q

d = 10 # dime
amount_of_dimes = remainder_after_q // d
remainder_after_dime = remainder_after_q % d

n =5 # nickles
amount_of_nickles = remainder_after_dime //n
amount_of_pennies = remainder_after_dime % n

print("Amount of quarters is",amount_of_quarter)
print("Amount of dimes is",amount_of_dimes)
print("Amount of nickles is",amount_of_nickles)
print("Amount of pennies is",amount_of_pennies)


# Use casting on time in this class and get rid of all decimal
#point in the output
# I can get float types from the assignments
# 


















