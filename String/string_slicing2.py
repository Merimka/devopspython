
#Slicing with the steps

s ="Techtorial"
substr = s[3:8:2] #hoi
print(substr)

sub = s[2:4-1]

print(sub)

#Since slicing will go from right to left because of the negative step
# The code will not be able to find index 4 atfer starting from
#index number 2. Therefore the variable sub will be an empty string

#   0123456789
s ="Techtorial"
substr2 = s[4:2-1]
print(substr2) # th

# Question
# What will be the output of the code above?
print(s[:] == s)  # True
# What will be the output of the code below?
#This all same thing just different way to write 

print( s[:]==s[::1] == s ==s[0:len(s):1] == s[0:len(s)])
#True

print(s[::-1]) # lairorcheT ##Will reverse of "Techtorial"
