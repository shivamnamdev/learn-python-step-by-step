# Tuple
#  A tuple is a collection -> group of items(basic data types or another collection)
# In python tuple, we use paranthesis ()
# tuple is immutable

l = [1,5,3,7,3,7]
t = (1,5,3,7,3,7)

print(type(l))
print(type(t))


#Example 2: Update won't work
# t = (1,5,3,7,3,7)

# TypeError: 'tuple' object does not support item assignment
# t[3] = 54
# print(t)

# Example 3: access tuple values
t = (1,5,3,7,3,7)

print(t[1]) # 5
print(t[-2]) # 3
print(t[1:4]) # (5,3,7)

# Use case
location = (123.80, 241.80)

# example 4: functions
print(t.count(7))
print(t.index(7,4))

# Parsing/Iteration
t = (1,5,3,7,3,7)

for i in t:
    print(i)
    
for i in range(len(t)):
    print(t[i])   
    
     
# how can we change tuple value if we want to
t = (1,5,3,7,3,7)

updatet = list(t) 
print(updatet)  
updatet[2] = 6
print(updatet)
t = tuple(updatet) 
print(t)