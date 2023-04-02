
#Calculate if given year number is the leap year or not.
# If  it is a leap year we'll print True, if not we'll print False.

# A leap year is a year that is evenly divisible by 4,
# unless it is a century year(divisibly by 100),
#in which case it must also be divisible by 400 to be a leap year.

# When the year is century year,(divisible by 100) then to be able to
# be a leap year it has to be divisible by 400.
# in all other cases just being able to be divided by 4 is enough.

# If the year is divisible by 4 it is a leap year.
# It shouldn't be a century year(1800)
# When it is a century year and also divisible by 400 then
# it is a leap year.

# I should check if the year divisible by 4 but not 100
# I should check if the year is divisible by 400

# When the number is divisible by any other number it given 0 remaining.

year = 2400
is_leap = (year % 4==0 and year % 100 !=0) or (year % 400 == 0)
print("The condition of the given year being a leap year is",is_leap)













