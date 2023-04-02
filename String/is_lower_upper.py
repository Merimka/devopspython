
s = "Python"
print(s.islower()) #-> False
# This will print False because string has upper case letter.
s = "python"
print(s.islower()) #-> True

s = "python is fun"
print(s.islower()) # ->True

s.upper()
print(s.isupper()) # -> False
#Unless reassigned value of string NEVER changes.

s = s.upper() # 
print(s.isupper()) # -> True

# islower returns True when all LETTERS in string is lower case,
# isupper returns True when all LETTERS in string is upper case.
#NOTE !!!!!! When there is no LETTER in string, both method will return
#False
print("123456".islower()) #-> False
print("123456a".islower()) # -> True

























