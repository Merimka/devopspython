# Ask user to give a string filled with cat and dog words
# From the given string if the number of dogs
# and cats is the same print True,
# other wise print False


# catdog -> True
#catcatdog -> False
given_text = input("Give a string filled with cat and dog wirds: ")
number_of_cat = given_text.count("cat") #0
number_of_dog = given_text.count("dog") # 0
print(number_of_dog == number_of_cat)


# If the it find the provided character ot the string it will return
# total number of those character. If those character does not exist
# in string it will return 0.
print("".count("Academy")) # -> 0
print("Academy".count("Academy")) # -> 1






















