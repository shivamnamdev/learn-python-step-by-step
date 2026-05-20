# OOPS Concepts: Object Oriented Programming System

# Class
# Object
# Inheritance
# Polymorphism
# Encapsulation
# Abstraction


class patient:
    # Class Variables
    name = "Unknown"
    age = 0

    def add_patient(self, name, age):
        # print(patient.name)
        # print(patient.age)
        # print(self)
        self.name = name 
        self.age = age
        

p1 = patient()
p2 = patient()

# print(p1)
# print(p2)

p1.add_patient("Rahul", 40)
# ---> add_patient(p1, "Rahul", 40)
p2.add_patient("Raj", 35)
# ---> add_patient(p2, "Raj", 35)

print(patient.name) # Class Variable
print(patient.age)
print(p1.name) # Instance Variable
print(p1.age)

print(p2.name)
print(p2.age)