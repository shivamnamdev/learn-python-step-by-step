a = 10
z = "welcome"

# Collection
# List 
# Tuple 
# Set 
# Dictionary 

# List
#  A list is a collection -> group of items(basic data types or another collection)
# In python lists we use square brackets []
# list is mutable


# Example 1: how to create list
mylist1 = [10,20,30,40,50]
mylist2 = ["apple", "banana", "orange"]
mylist3 = ["apple", 10, 20.5, True]
mylist4 = list()

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)


#  Example 2: How to access items from the list
mylist = ["apple", 10, 20.5, True]

print(mylist[1])
print(mylist[-1])
print(mylist[0][1])
# if "a" in mylist[0]:
#     print("yes it is")

# Example 3: Range of indexes
mylist = ["apple", "banana", "orange", "cherry", "mango", "melon"]
print(mylist[1:4])
print(mylist[-3:-1])

# Example 4: Change Item values
mylist = ["apple", "banana", "orange", "cherry", "mango", "melon"]
print(mylist)
mylist[0] = "dragon fruit"
print(mylist)


# Example 5: Item iteration
mylist = ["apple", 10, 10, "orange", "cherry", "mango", "melon"]
for i in mylist:
    print(i)

# Example 6: using membership operator
mylist = ["apple", 10, 10, "orange", "cherry", "mango", "melon"]

if "appl" in mylist:
    print("yes it is")
else:
    print("not present")

# Example 7: how to check the length of the list
print(len(mylist))


# Example 8: Adding element
# append
mylist = ["apple", "cherry", "mango", "melon"]
mylist.append("orange")
print(mylist) #['apple', 'cherry', 'mango', 'melon', 'orange']

#insert
mylist.insert(1, "dragon fruit")
print(mylist) # ['apple', 'dragon fruit', 'cherry', 'mango', 'melon', 'orange']


#extend

# Example 9: Remove element
# using pop
mylist = ["apple", "cherry", "mango", "melon"]
mylist.pop() #['apple', 'cherry', 'mango']
print(mylist) 
print(mylist.pop(1))#cherry
print(mylist) #['apple', 'mango']