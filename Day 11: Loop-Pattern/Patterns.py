
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 21

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


#
# 12345
# 1234
# 123
# 12
# 1

# 1
# 2 2
# 3 3 3
# 4 4 4 4


# Program to print:
#    1
#   2 2
#  3 3 3
# 4 4 4 4

# Program to print:
#       1
#      2 3
#     4 5 6
#    7 8 9 10

# Program to print:
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1


# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)
   
   
# *****
# ****
# ***
# **
# *   
 
# for i in range(5,0,-1):
#     print("*"*i)
    
#         *
#       * *
#     * * *
#   * * * *
# * * * * *    
    
# for i in range(1,6):
#     print(" "*(6-i), end="")  
#     print("*"*i) 
    
# 1
# 2 2
# 3 3 3
# 4 4 4 4    
max = 9
for i in range(1,max):
    for j in range(0,i): 
        print(i, end=" ")
    print()
    
# 1     -> i = 1, j = 0, 
# 2 2   -> i = 2, j = 0
# 3 3 3 
# 4 4 4 4 


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 21
num = 1
max = 10
for i in range(1,max):
    for j in range(0,i):
        print(num, end=" ")
        num+=1
    print()
    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")   
    print()     