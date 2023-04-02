"""
Using the input function ask the user to enter one sentence with
three words and print the index number of each words last character and
then print the sum of each index number that you found.
For Example:
Input:
"Importance of Human" --> it can be any three-word sentence.
Output:
9 --> index number of 'e'
12 --> index number of 'f'
18 --> index number of 'n'
The sum: 39
"""

user_entered_sentence =input("Enter a one sentence with three words: ")
first_word_index = user_entered_sentence.find(" ")-1 # first word
second_word_index = user_entered_sentence.rfind(" ")-1   #second word
last_word_index = len(user_entered_sentence)-1   # third
result = first_word_index + second_word_index + last_word_index  # sum
print("The sum:",result)




