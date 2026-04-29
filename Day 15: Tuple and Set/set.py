# Set
# A collection of unique values - no duplicacy
# Mutable data type
# Unordered
# we user {} to contain set 

# Example 1: how to create a set
data = {1,2,3,4,5}
print(data)
print(type(data))
# emptyset = {} -> dict
emptyset = set()
print(type(emptyset))
multiplevalue = {1,5,2,2,2,2,1,6}
print(multiplevalue)

# Example 2: adding values in the set
num = {1,2,3,4,5}
num.add(7)
num.add(2)
print(num)

# Example 3: remove values in the set
num = {1,2,3,4,5}
num.remove(2)
# num.remove(7) KeyError: 7
print(num)

num.discard(7)
num.discard(3)
print(num)

# Example 5: Set operations
a = {1,2,3,4,6,7,9}
b = {4,5,7,8,10}
print(a | b) # union
print(a & b) # intersection
print(a - b) # difference
print(b - a)


List = "Shopping bag (values are changable)"
Tuple = "Locked Box(Fixed)"
Set = "Unique Collection (No duplicacy)"