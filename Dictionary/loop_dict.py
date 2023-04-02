
student ={
    "course"     :"DevOps",
    "name"       : "John",
    "start_date" :"Aprel",
    "end_date"   : "May"
}
# I would like to print all the keys in this dictionary.

for k in student.key():
    val = student.get(k)
    print("type of key is ",type(k),f"and the value of key is{k} and value of the key is {val}")


# The usage of for loop above is not optimized.

# items method

print(type(student.items()))
print(student.items())
for k,v in student.items(): #key=k; value= v
    print(f"The key is{k},the value is{v}")











