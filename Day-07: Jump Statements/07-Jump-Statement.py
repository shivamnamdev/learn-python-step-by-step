# Two types of jump statements:
# 1. Break --> to get exit out of the immediate loop
# 2. Continue --> 

# When initialised variable in the condition doesn't play a role
# of a jump of the interpretor

a = 1
while True:
    # a = a + 1
    if a == 5 or a == 7:
        a += 1
        continue
    print(a)
    a += 1 # short hand of the above line
    if a >10:
        break
    print("another line")

