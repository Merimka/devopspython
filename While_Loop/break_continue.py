# When the code executes break statement the loop will stop, even 
# the condition for lopp is True.

while True:
    print("Example of break statement")
    break


# How many times do you think the loop above will iterate?
# The loop above will iterate 1 time.

#Continue
# In order to start next iteration in the loop rather than waiting for
# all loop of a body to execute we can use continue statement.

# Let's print all numbers from 1 to 20 inclusive, if they are an 
# odd number
#NOTE: Odd numbers means cannot be divisible be 2.
#Such as, 1,3,5,7,9,11 etc.

count = 1
while count <= 20:
    #If it is odd I have to print, when the number is even we don't have to do anything
    if count % 2 == 0: # Which means the count is an even number
        count+=1
        continue
    print(f"{count} is an odd number.")
    count+=1

#NOTE: Contunie statement is not used commonly, when coding.
# Most of the time contunie statement  doesn't change the output,however it makes the
#code little bit faster.

# pass is used for having an empty indented body, contunie is used for jumping to yhe next
# iteration.












