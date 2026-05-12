# Exception: Exception is an even, which will cause program termination
# Types of Exception: 
#    - Syntax Error -> Solution: IDE updates the syntax errors - Terminates
#    - Runtime Error -> (ValueError, FileNotFoundError, TypeError) - Terminates
#    - Logical Error -> AI Assisted IDEs(VsCode, Cursor, Antigravity)

# Purpose:
#  - Stop the program termination
#  - Handle the Exception


# print("This is the first message")
# print("This is the first message" # syntax error
# print("This is the first message") 

# value = int(input("Enter a value:"))
# print(10/value)

# try:
#   risky code
# except Defined-Exception:
#   perform only, when exaception occurs, raise exception
# else:
#   perform only, when no exception occurs
# finally:
#   performs anyhow

# # Example 1: Without explicitly mentioning the exception
# try:
#     value = input("Enter a value:")
#     print(10/value)
# except:
#     print("you are diving with zero")    
    
# Example 2: with explicitly mentioning the exception    
# try:
#     value = int(input("Enter a value:"))
#     print(10/value)
# except ZeroDivisionError:
#     print("you are diving with zero")    


# Example 3: with inbuilt error message
# try:
#     value = input("Enter a value:")
#     print(10/value)
# except Exception as e:
#     print("you are diving with zero", e)     
    
# print("This is outside the try except block")   # This line will run

# # Example 4: with multiple explicitly mentioned exceptions  
# try:
#     value = int(input("Enter value: "))
#     print(10/value)
# except ZeroDivisionError:
#     print("you are diving with zero")
# except TypeError:
#     print("you cannot divide with the different type")
# except ValueError:
#     print("you cannot use unexpected value")   
    
# print("This is outside the try except block") 



# Example 4: use with else and finally block
# try:
#     value = int(input("Enter value: "))
#     print(10/value)
# except ZeroDivisionError:
#     print("you are diving with zero")
# except TypeError:
#     print("you cannot divide with the different type")
# except ValueError:
#     print("you cannot use unexpected value")  
# else:    
#     print("no exception occurs")
# finally:
#     print("This would run anyhow")
     

# print("This is outside the try except block")             



# Program

# try:
#     file = open("testings.txt",'r')
# except FileNotFoundError as f:
#     print("Use existing file", f)   
# else:
#     print(file.read())
#     file.close()  
# finally:
#     print("Program terminates")   
    
      
# # Creating Custom Exception

# age = int(input("Enter the age of the voter: ")  )
# if age > 18:
#     print("You can vote")
# else:
#     raise Exception("You are not eligible to vote")     
        
# Handling the custom Exceptions
age = int(input("Enter the age of the voter: ")  )
try:
    if age < 18:
        raise Exception("You are not eligible to vote") 
    print("you can vote")            
except Exception as e:
    print("Error Occurs due to: ", e)    