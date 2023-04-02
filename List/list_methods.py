## List methods

# We'll cover the commonly used list methods that alter the original value
# of lists.

# append method -> will add elements to the end of list.
l = [1,2]
l.append(3)
print(l) #[1,2,3]
# Since the list mutable, the original value of the list changed
# without reassigning

# --------------------------------------------------------------------------------------
##  insert method-> will add new item to the list in the given index
#insert(indexNumber,newElement)
# It will add new element WITHOUT REPLACING any exicting element

l = [1,2]
l.insert(1,"text")
print(l) # [1,"text",2]

# ----------------------------------------------------------------------------------

## remove method -> remove method removes SPECIFIED ITEM from the list.

words = ["AI","DevOps","Technology"]
# If I would like to remove on of these elements, I can just place 
# What I would like to remove in a remove method.
# words.remove("Technology")
#NOTE:!!! When remove method is used with an object that is NOT IN THE LIST,
# it will GENERATE AN ERROR.
words.remove("Technology")
print(words) #["AI","DevOps"]


#----------------------------------------------------------------------------------
## pop method -> will remove element from specified INDEX
words = ["AI","DevOps,Technology"]
words.pop(1)
print(words) #["AI","Technology"]

#words.pop(4)
#NOTE!!! When pop method used with index that doesn't exist in a list.
# it will GENERATE AN ERROR.


#----------------------------------------------------------------------------------
#What is the difference between append and insert methods? 

#Append method takes only one parameter as a new value, and adds 
#that value at the end of the list. 
#On the other hand, insert method will take two parameters. 
#First one is index number and second one is the new value. 
#It adds new value to specified index WITHOUT REPLACING any existing element.




#What is the difference between remove and pop method? 

#remove method takes one parameter as an existing value from list then
#removes that first occurence of that value from the list. 

#pop method also takes one parameter but as an index number. Then 
#removes element from specified index number. If no parameter 
#used for pop method, pop method will REMOVE THE LAST ELEMENT in the list.

#---------------------------------------------------------------------------------




















