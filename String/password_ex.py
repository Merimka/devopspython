# Ask user to enter a password
# The password should contains
# both upper and lower case letters
#If it contains both upper and lower case letter
#print True,  otherwise print False



#We are expecting user to enter a both with lower and upper case letter
password= input("Enter a password contains upper and lower case")

# I should write a code if conditions provided or not.
#
# s ='password'
# s==s.lower() -> password == 'password'.lower() -> True
is_all_lower = password == password.lower()

#s ='PASSWORD'
# s ==s.upper() -> "PASSWORD" ->'PASSWORD'.upper()

is_all_upper = password ==password.upper()

# If the given string(password) equals to its upper version
# It means that it is all upper case letters.
# When is_all_lower False it tells that there are upper case in str.
# When is_all_upper False it tells us that there are lower cases in str.



#I want both of these conditions to be False
is_password_good = not is_all_lower and not is_all_upper

print("The condition of given password is",is_password_good)










