"""
1. Ask the user to enter a random word using input function.
2. Then ask the user to input the number of letters that word consists of.
3. Lastly ask the user for a letter that they want to learn its index.
4. Your code should print True if the user entered a right number of letters in
the word. Print False if the wrong number is entered.
5. Your code should print the index of the entered letter, if the word doesn’t
contain the letter then the code should print -1.
6. Please look at the example output below to understand how your code
should work.
EXAMPLE OUTPUT:
Enter a random word
Techtorial -> this line represents user's input
Enter number of letter that word consists
10 -> this line represents user's input
True
Enter a letter that you want to find an index
a -> this line represents user's input
8
"""
users_random_word = input("Enter a random word: ")
user_number_of_letter = int(input("Enter number of letters that word contains: "))
entered_letter= input ("Enter a letter that they want to learn its index: ")
if len(users_random_word) == user_number_of_letter:
    print("True")
else:
    print("False")

if entered_letter in users_random_word:
    index_tofind = users_random_word.index(entered_letter)
    print(index_tofind)
else:
    print("-1")







