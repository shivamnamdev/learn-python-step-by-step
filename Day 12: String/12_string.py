# String: stream of data enclosed within "" or '' 
var = "123"
var1 = '1sfgfg1.3.13wfg$^#^#'
var2 = "this is my string"
print(var)
var = "sdfgdsfg"
print(var)

# Concept 1: Accessing character/item in the string using index
print(var[0])
print(var[-8])
# TypeError: 'str' object does not support item assignment
# var[0] = "k"

# Concept 2: mutable vs immutable
print(ord(var[0]))

var = "working"
print(ord(var[0]))
print(chr(119))

#Concept 3: Operator + *
# + -> Concatenation
# * -> Repeation


# Concept 4: String slicing
# string[start : stop(ex) : step]
var = "This is my string variable"
print(var[0]) # T
print(var[5]) # i
print(var[0:4]) #This 
print(var[5:7]) #is
print(var[11:17]) #string
print(var[-3:]) #ble
print(var[5:]) #is my string variable
print(var[::3]) #Tssytnvil
print(var[::-1]) #elbairav gnirts ym si sihT
print(var[16:10:-1]) #gnirts

# Concept 5: Functions
var = "akanksha"
print(var.capitalize())
print(var.count('a'))
print(var.replace('a','O',2))
print(var.upper())
print(var.lower())
print(var.index("k",2))
var = "Making"

var = var[0:2] + "d" + var[-3:]
print(var)

var = "Hakuna Matata"
# a -> o