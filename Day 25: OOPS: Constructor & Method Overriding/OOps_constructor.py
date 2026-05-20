# OOPS Concepts: constructor
# Constructor: Is a Class method, which is use to initialize the values

class patient:
    # Class Variables
    name = "Unknown"
    age = 0
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def update_name(self, name):
        self.name = name
        
    # def add_patient(self, name, age):
    #     # print(patient.name)
    #     # print(patient.age)
    #     # print(self)
    #     self.name = name 
    #     self.age = age
        

p1 = patient("Rahul", 40)
p2 = patient("Raj", 35)

# print(p1)
# print(p2)

# p1.add_patient("Rahul", 40)
# ---> add_patient(p1, "Rahul", 40)
# p2.add_patient("Raj", 35)
# ---> add_patient(p2, "Raj", 35)

print(patient.name) # Class Variable
print(patient.age)
print(p1.name) # Instance Variable
print(p1.age)

print(p2.name)
print(p2.age)

p1.update_name("Yash")
print(p1.name)
p2.update_name("Rudra")
print(p2.name)


