
num =  21

#  
print(type(num))   # <class 'int'>

#After the division operator
new_var = num / 3
print(type(new_var))  # class 'float'

# since the result of division (/) operator is not guarenteed to be 
# Whole number,  python will always assign result of/  operator
#with a float number.
#____________________________
result_floor = num // 3
print(type(result_floor))    # int type

result_intFloat=3.0 + 5
print(type(result_intFloat))  


# Any arithmetic operator betwee float and a integer will result in 
# Float type



c= 3+0j
print(type(c))  # <class 'complex'>
#____________________
ex = "A text"
print(type(ex))  #<class 'str'>










