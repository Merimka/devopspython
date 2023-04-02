

#removeprefix will remove provided text from the begginning of string.

s = "Hello Python"
print(s.removeprefix("Hello "))

# The text provided in removeprefix method should exactly match
# the beginning of string. Otherwise it won't remove anything.
print(s.removeprefix("Hell ")) #Hello Python
print(s.removeprefix("Python")) 

print(s) #Hello Python


# ---- ------- -------------------------------------- -----------------------#

# removesuffix methon will remove the provided text from the end of
# string. The provided in removesuffix method should exactly 
# match end of string. Otherwise it won't remove anything.

s ="Hello Python"

print(s.removesuffix("Python")) # 'Hello '
print(s.removeprefix("hon"))  # 'Hello Pyt'

print(s.removesuffix("Hello ")) #"Hello Python"

print("Hello".removesuffix("llo")) #He
print("Hello".removeprefix("llo"))  #Hello
print("Hello".removeprefix("He"))  #llo

print("Hello Python".removeprefix("Hello Python")) #empty

print("Hello Python".removesuffix("Hello Python")) #empty





