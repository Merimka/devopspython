
# update method ------------------------------------------------------------------
# This method is used to add or update key-value pairs from another
# dictionary object.
# If provided key exist in a dictionary it will update the value 
# in the dictionary, if not it will be added as new pairs.

dict = {
    'key1' : 'value1',
    'key2' : 'value',
}
dict.update({'key':'value3'})
print(dict) # -> {'key1' : 'value1','key2': 'value2','key3':'value3'}
dict.update({'key1':10})
print(dict) #->{'key1':10,'key2': 'value2','key3':'value3'}

print(''' #----------------------------------------------------------------------#''')

#pop method-------------------------------------------------------------------
# pop method remove key pair value from the dictionary.
# It takes one parameter as key
# pop method returns a string object,
# If the key provided is not present in dictionary,this method
# will generate an error
student ={
    "course"     :"DevOps",
    "name"       : "John",
    "start_date" :"Aprel",
    "end_date"   : "May"
}

print(student.pop("name"))
print(student)
print(''' #----------------------------------------------------------------------#''')

# popitem _____________________________________________________
# popitem() method removes last inserted pair from dictionary, and returns as a tuple.
student ={
    "course"     :"DevOps",
    "name"       : "John",
    "start_date" :"Aprel",
    "end_date"   : "May"
}
#print(student.popitem())
last_key,last_value = student.popitem()
print(last_key,"->",last_value) # end_date -> May

print(student) # {'course':'DevOps','name':'john','start_date':'April'}







