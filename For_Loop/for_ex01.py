# Print given string without its vowels using for loop and continue
# statement.

str = input("Enter any string: ")

# I should check each letter individually so that i can evaluate
# whether they are consonant or vowel.
vowels ="aeiouAEIOU"
for anythinisfine in str:
    if anythinisfine in vowels:
        #What that say about element(el) ?
        # It says that element is a vowel
        continue
    print(anythinisfine,end=" ")

print() # To get rid of percent sign that appeats otherwise.











