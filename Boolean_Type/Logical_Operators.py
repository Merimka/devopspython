
b1 = True
b2= False
print(b1 and b2) # False  ##(the both side isn't true that is why is false)

print(b1 and True) # True

print(b2 and b2) #

#I want to see if i I can go eat today.
# I have given parameters which are money, if i have time
have_time = False
have_money = False
can_i_go = have_time and have_money
print("Value of variable can_i_go is",can_i_go) # False
 

#______OR
#I need to exercise every day. to able to exercise
#every day I have to check 2 parameters which are if I have gym card
#or gym equipment at home. In both times I can exercise daily

have_gym_eq = True
have_gym_card = False
can_I_exercise = have_gym_eq or have_gym_card
print("Value of variable can_I_exercise is ",can_I_exercise)  # True

#_____ NOT operator
#makes boolean value take the opposite value in an equation.

b2 = True
print(b2 and not False) # True
print(not b2 and True) # False
print("The value of b2 is",b2) #The value of b2 is True

#Note b2 didn't change it's value because boolean is an immutable
#type, which means value will be protected unless reassigned.




















