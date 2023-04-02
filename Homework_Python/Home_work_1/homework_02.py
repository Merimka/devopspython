"""
Write a Python program that will have a 5-digit number variable, and then
prints the reversed version of that number.

For example,
If the value of the number variable is 12345, the program should reverse
the order of the digits and print the result as 54321.
Note: Your code should work for every five digit number.
"""


num = int(input("Enter a 5 digit numbers: ")) # 5 digit comming from user
reverse_num = int(str(num)[::-1]) # users  number convert to str and reverse to
                                  # print
print("The program reverse number is",reverse_num)



