import keyword


print("Welcome to the Session")
print(22)
print(22.5)

# Keywords - reserved words or reserved names
print(keyword.kwlist)

# Data types:
name = "Poonam" # text - string
rollno = 10.    # number - Integer
marks = 14.2    # decimal - Float
Result = True   # Boolean - boolean


#Collections
lists  = [1,2,4,7,4]
sets = {1,6,3,2}
tuples = (1,7,3,"sddgdg")
dictionary = {"key": "Value","key2":2}

# Program loads in the RAM and run it, After the execution it unloaded
# Values - Constant and Variable

# Declaring a variable
######### Exercise 1 #########
a = 22
b = True
print(a)
print(b)
a = "string value"
print(type(a))
print(type(b))

######### Exercise 2 #########

a, b, c = 10, 20, "String"
print(a,b,c)


######### Exercise 3 #########
#a, b, c = 100

#print(a, b, c)

######### Exercise 4 #########
a, b = 10, 20

a, b  = b, a
print(a, b)

a, b, c = 10, 20, 23
print(a,b,c)