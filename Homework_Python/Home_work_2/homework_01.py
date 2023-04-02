"""
Please use method chaining for the following Strings.
Methods are provided next to the String.
String “ Snicker " —> strip, upper, remove prefix and slice the
string with any number of your choice

String “Cookie” —> lower, replace 'o' with 'u', remove suffix e, 
starts with 'C'
"""
string_given = " Snicker "
result = string_given.strip().upper().removeprefix('SNI')[1:2]
print(result) 

string_cookie = "Cookie"
result2=string_cookie.lower().replace("o", "u").removesuffix("e").startswith("C")
print(result2)





