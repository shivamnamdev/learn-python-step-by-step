#  Input function
######### Example 1 ###########

a= input()
print(a)

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
print(a + b)


######## Example 2 ###########
c = input("Enter the first value: ")
print(type(c))


# Len function
name = "Akanksha"
print(len(name))

######### Example 1 ##########
print("Single Value")
print("value1", "Value2", "value3")

######### Example 2 ##########
a = 30
b = 40

print("My marks are",a,"out of",b)

# ######### Example 3 ##########
a = 30
b = 40

# print("My marks are",a,"out of",b)
print("My marks are {} out of {}" .format(a,b))
print("My marks are {} out of {}" .format(b,a))



print("typing enter", end='-')
print("next line?")

print("My marks are", a, end =" ")
print("out of", b)