#Let's ask user to enter a word
#The print that word

print("Please,enter a word")
word = input()
print("The word that user entered is",word)

print("The data type of variable word is",type(word)) # to know the type we use type()

#Let's ask user to enter a number

print("Please,enter any number")
num = input()
print(num) #-> 23
print(type(num)) # -> <class'str'>


#We understand that input()will always return the value as string.
#What should we do when we need other other date types such as int,float?

# How can we convert string into an integer variable?
print("Please,enter only number not starting with 0")
num1= int(input())
# If user enters anything other then number code will generate error.

print("Casted result of input function is",num1)
print("Casted result of input function is",type(num1))

















