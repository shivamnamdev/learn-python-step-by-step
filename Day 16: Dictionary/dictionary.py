
# Dictionary
# A collection which store data in the form of key-value pair
# We define dictionary using {"key": Value}
# key -> immutable, unique(like a set)
# Value -> mutable
# no index value logic
# Order -> matters

name = "Nischal Sharma"
age = 31
rollno = 22
city = "Bhopal"

student = ["Nischal Sharma", 31, 22, "Bhopal"]

# Example 1: Declare Dictionary
student_dict = {
    "name": "Nischal Sharma",
    "age": 31,
    "roll_no": 22,
    "city": "Bhopal"
}

print(student_dict)
print(type(student_dict))

student_dict1 = {
    "name": "Nischal Sharma",
    "age": 31,
    "roll_no": 22,
    "city": "Bhopal",
    "name": "Amit Chouhan",
    "city": "Indore",
}

print(student_dict1)

#Example 2: Update
student_dict = {
    "name": "Nischal Sharma",
    "age": 31,
    "roll_no": 22,
    "city": "Bhopal"
}

student_dict["name"] = "Sonal"
print(student_dict)

# Example 3: Delete
print(student_dict.pop('roll_no'))
print(student_dict)
# print(student_dict.pop('roll_no')) KeyError: 'roll_no'

del student_dict['city']
print(student_dict)
# del student_dict['city'] KeyError: 'city'

# Example 4: Functions
student_dict = {
    "name": "Nischal Sharma",
    "age": 31,
    "roll_no": 22,
    "city": "Bhopal"
}
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

print("*"*20)

# Example 5: Parsing via loops
for k in student_dict.keys():
    print(k)
# name
# age
# roll_no
# city
for v in student_dict.values():
    print(v)
# Nischal Sharma
# 31
# 22
# Bhopal
for k, v in student_dict.items():
    print(k, v)
# name Nischal Sharma
# age 31
# roll_no 22
# city Bhopal    

# Example 6: Adding a value

student_dict['result'] = "Pass"
print(student_dict)
          
# Example 7: Nested Dictionary
student_marks = {
    "Science":{"internals": 80, "externals": 10},
    "Maths": {"internals": 74, "externals": 11}
}         
#Example 8: Accessible Ways
print(student_marks['Maths']['internals'])
print(student_marks['Science'].get("internals","This key is not present"))

#Example 9: Possible Keys values

student = {
    "string": True,
    1: True,
    1.2: True,
    True: True,
    (1,2): True,
    # [1,5]:True, TypeError: unhashable type: 'list'
    # {1,6,3}:True TypeError: unhashable type: 'set'
    # {"key": 3}: False TypeError: unhashable type: 'dict'
}
print(student)


marks = {
    "science": 75,
    "maths": 81,
    "english": 78
}
maxvalue = 0
for key,value in marks.items():
    if maxvalue == 0:
        maxvalue = value
        maxkey = key
    elif value > maxvalue:
        maxkey = key
        maxvalue = value 
    else:
        continue     
print(maxkey) 