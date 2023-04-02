#Ask user to enter a string
#Then print a version or that string without 
#First and last letter.
#You assume that user will give a string lenght more than 2.
#Table -> abl
#Keybord -> eyboar



text = input("Enter a string: ")
#I need to return this without first and last letter.
#I should get a  portion of this string

print(text[1:len(text)-1])
print(text[1:-1]) #Same thing
#Since the python has a negative indexing the code above will give
#without first and last character




