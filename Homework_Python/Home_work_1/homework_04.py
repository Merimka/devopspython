"""
Write a python program to convert minutes variable into a number 
of years and days.
Test Data
Number of minutes: 3456789
Expected Output :
3456789 minutes is approximately 6 years and 210 days
"""
#Convert minutes to years
#Convert minutes to days
#Convert years to days then subtract from total days 
#To find remaining days

var_minutes = int(input("Number of minutes: "))
var_years = var_minutes // 525600      #3456789 minutes is 6 years
var_days = var_minutes //1440              #3456789 minutes is 2400 days
var_remaining_days = (var_days - (365 * var_years))   #6 years 365*6 = 2190 days  2400 - 2190 = 210 days
print(var_minutes,"minutes is approximately",var_years,"years and",var_remaining_days,"days")







