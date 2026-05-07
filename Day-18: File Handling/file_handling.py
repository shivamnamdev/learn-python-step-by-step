# Primary vs Secondary Memory
# RAM -> Consciousness -> Temporary memory
# Storage -> Persisted Memory -> Permanent memeory

# Data types/Structures - so far we have covered are nothing but for Primary Memory(RAM)
# File -> Secondary Storage( save it and check it later even after program terminates)


# File is container that stores data permanently
# Example: Data.txt, Data.csv, report.log, config.json

# 3 step life cycle:
# - Open the file -> Open the notebook
# - Perform operations (read/write) -> using the notebook
# - Closing the file -> Closing the notebook


# Purpose
# - Read, Write, Append, Execute


# Example 1: How to read a file
file = open('Testing.txt','r')
print(file.read())
file.close()
# print(file.read()) ValueError: I/O operation on closed file.

# Example 2: With wrong file name
# file = open('Testing1.txt','r') FileNotFoundError: [Errno 2] No such file or directory: 'Testing1.txt'

# Example 3: How to write a file
file = open('Writing.txt','w')
# print(file.read()) io.UnsupportedOperation: not readable
file.write("This is my updated file")
print(file.write(" number of item"))
print(file.read())
file.close()
# file.write("SHouldn't print") ValueError: I/O operation on closed file.

# Standard Input: input() stdin -> cmndline
# Standard Output: print() stdout -> cmndline

# Example 4: Append a File
file = open("Writing.txt",'a')
# print(file.read()) io.UnsupportedOperation: not readable
file.write("\nAppend a new data")
file.close()

# Example 5: Append a newly created file
file = open("Writings.txt",'a')
file.write("\nAppend a new data")
file.close()

# Example 6: Execute the file
file = open("execute.txt",'x')
# file = open("execute.txt",'x') FileExistsError: [Errno 17] File exists: 'execute.txt'
file.write("Append a new data")
# print(file.read()) io.UnsupportedOperation: not readable
file.close()

# r+ -> read + write
# w+ -> write + read
# a+ -> append + read

# New Line from github web editor