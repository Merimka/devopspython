# Ask user enter two numbers that are not a same .
# And print all numbers that is divisible by 3 and 8 between
# given 2 numbers.


number1= int(input("Enter a positive integer number: "))
number2= int(input("Enter a number bigger than first number: "))

# I have to check range of given numbers
# Starting from num1 and ending at num2

while number1 < number2:
    # How can I understand if number is divisible by 3 and 8
    # When the remainder gives 0,it means we can divide that number.
    if number1 % 3 ==0 and number1 % 8 == 0:
        print(f"{number1}is divisible by 3 and 8.")
    # For condition update I could increase the value of number1
    number1+=1



























