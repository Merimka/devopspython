# create a method to find highest common factor of two given numbers.
# highest common factor is biggest commond divisor of two given numbers.
# 24 18 -> 6 There is no bigger than 6 that could evenly divie 24 and 18.
# 32 12 -> 4
# 24 12 -> 12

# 1- What is the limit of the numbers I should check as possible HCF ?
# 2- I have two numbers given,my limit as possible HCF should be one of the
# numbers and below.
# 3-It should chose one of the numbers start checking from that number to number 1.
# 4- When writing a code, first do necessities of the code. Then optimize
# 5- There are the necessity of the program
# 6- lowes iteration possible.# What is the  biggest possible common divisor.
# 7- bigger number divied by 2 is the biggest possible divisor unless they are the same


def find_HCF(num1,num2):
    possible_hcf= num1
    while True:
        if num1 % possible_hcf == 0 and num2 % possible_hcf == 0:
            # If is not a possibility that possible hcf can divide both,
            # it is a certainty.
            return possible_hcf
        
        # I should tell the code look next possible option
        possible_hcf -=1

print(find_HCF(24,32))
print(find_HCF(32,24))
print(find_HCF(32,12))



















