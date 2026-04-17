# When you know the number of iteration --> For Loop
# When you don't know the number of iteration bu the
# condition till which the loop should be running --> While Loop

# for student in class:
#     action

# Sytax
# for <instance> in <Collection>:
#     statement

r = range(1,10)
print(r)

for number in range(1,6):
    print(number)
  
# c, c++, Java
# for(i=1;i<10;i++) {
#     action
# }
  
# TypeError: 'int' object is not iterable    
# a = 10    
# for integer in a:
#     print(integer)  

alpha = "abcde"
for a in alpha:
    print(a)
    
# range(1,10) ---> (1,2,3,4,5,6,7,8,9)
# range(6) -----> (0,1,2,3,4,5) 
# range(1,10,2) --------> (1,3,5,7,9)
print("*********")
for i in range(6):
    print(i)
print("*********")
    
for i in range(1,10,2):
    print(i) 
    
print("*********")
for i in range(10,0,-1):
    print(i)   
    
# TypeError: 'float' object cannot be interpreted as an integer    
# print("*********")
# for i in range(10.0,0.0,-1):
#     print(i)      

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            print(i,j,k)
        
# 1 1 ----> i=1, j=1
# 1 2 ----> i=1, j=2
# 2 1 ----> i=2, j=1
# 2 2 ----> i=2, j=2


  
    