import mainfolder.definition as df
# from definition import * 
# from mainfolder.definition import divide, multiple

print("*"*10)
print("From here functions2 file begins")

print(df.add(5,7))
print(df.multiple(5,2))
print(df.a)
# print(divide(8,2))
# print(multiple(2,4))

print(__name__)
print(type(__name__))

print(__builtins__)


# File ->  A python file
# Module -> Python file has functions/variables to be imported
# Package -> Folder has multiple modules
__name__ = "__notmain__"
print(__name__)

