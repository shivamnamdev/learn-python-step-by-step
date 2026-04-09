# Conditions Statements

# if condition
# if-else condition
# elif condition


# if condition is true then -> do this action

# C, C++, Java
# if (condition){
#     action
# } 

# Python
# if true-condition:
#   do this
#   do this
#   do this
# line outside the if block


if False:
    print("This statement should run")
print("this block is outside the if statment")    

if 0:
    print("0 should run only when if condition is true")
print("this 0 is outside the if statment")    

if "":
    print("empty string should run only when if condition is true")
print("this empty string is outside the if statment") 

if 0.0:
    print("0.0 should run only when if condition is true")
print("this 0.0 is outside the if statment") 


# Python
# if true-condition:
#   do this
#   do this
#   do this
# else ---> (false):
#   do this
#   do this
# line outside the if block


mark = 80
if mark > 75:
    print("You are passed")
else:
    print("you are not eligible")
  
weather = "not raining"
is_rain_heavy = False

if "raining" is weather:
   if is_rain_heavy is True:
       print("take the raincoat")
   else:
       print("use umbrella")
else:
    print("go and have fun")
                

# Python
# if 1st-condition:
#   do this
# elif 2nd-condition:
#   do this
# elif 3rd-condition:
#   do this
# else ---> (false):
#   do this
#   do this
# line outside the if block
               
mark = 75
if mark > 75:
    print("distinction")
elif mark > 45:
    print("div2")
elif mark > 60:
    print("div1")
elif mark > 75:
    print("distinction")        
else:
    print("you are failed")               