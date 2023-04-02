# Ask user to enter a string.
#print all the vowels and count of vowels from the given string
# vowels in alphabet are a,e,i,o,u

users_string = input("Enter a string: ")
count_of_vowels= 0
index_in_string = 0
vowel_in_given_str = ' '
while index_in_string < len(users_string):
    vowel = "aeiouAEIOU" 
    current_letter = users_string[index_in_string]
    #If the current letter is one of the chars from vowels string
    # it means we have o increase count of vowels.
    # In order to check if current letter exist in vowel str.
    if current_letter in vowel:
        count_of_vowels +=1
        vowel_in_given_str = vowel_in_given_str + current_letter
    index_in_string+=1

print(f"The all vowels in string order is {vowel_in_given_str}")
print(f"Amont of vowel we have in the string is {count_of_vowels}")


#NOTE: We can use in operator which would check if given 
#character exist in a string
