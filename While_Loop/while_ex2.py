# Ask user  to enter a string that has 2 words and doesn't start
# with empty space. If user entered a space in the beginning or 
# a string that has more than or less than 2 words re-ask \
# to enter a string.

shoul_I_user = True

while shoul_I_user:
    print("Enter a string that has 2 word and doesn't start with empty space.")
    input_str = input()
    # String doesn't start with:
    if not input_str.startswith(' ') and (input_str.strip().count(" ") == 1):
        print(f"You have entered a correct string by entering{input_str}")
        shoul_I_user = False











