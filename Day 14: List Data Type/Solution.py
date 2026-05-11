# ==========================================
# LIST PROGRAMS – SOLUTIONS
# ==========================================

# Q1. Print all elements of a list one by one

nums = [10, 20, 30, 40, 50]

for value in nums:
    print(value)

# ------------------------------------------
# Q2. Find sum manually (No sum())

nums = [1, 2, 3, 4, 5]

total = 0

for value in nums:
    total += value

print("Sum:", total)

# ------------------------------------------
# Q3. Count even numbers

nums = [1,2,3,4,5,6,7,8]

count = 0

for value in nums:

    if value % 2 == 0:
        count += 1

print("Even count:", count)

# ------------------------------------------
# Q4. Create separate even and odd lists

nums = [1,2,3,4,5,6,7,8]

even = []
odd = []

for value in nums:

    if value % 2 == 0:
        even.append(value)

    else:
        odd.append(value)

print("Even list:", even)
print("Odd list:", odd)

# ------------------------------------------
# Q5. Find max manually

nums = [5,8,2,15,3]

largest = nums[0]

for value in nums:

    if value > largest:
        largest = value

print("Maximum value:", largest)

# ------------------------------------------
# Q6. Find minimum manually

nums = [5,8,2,15,3]

smallest = nums[0]

for value in nums:

    if value < smallest:
        smallest = value

print("Minimum value:", smallest)

# ------------------------------------------
# Q7. Print all consecutive pairs

nums = [1,2,3]

for i in range(len(nums)-1):

    print(nums[i], nums[i+1])

# ------------------------------------------
# Q8. Find consecutively repeating value

nums = [1,2,2,3,4,4,5]

for i in range(len(nums)-1):

    if nums[i] == nums[i+1]:
        print("Consecutive repeating value:", nums[i])

# ------------------------------------------
# Q9. Remove duplicates in the list

nums = [1,2,2,3,4,4,5]

unique = []

for value in nums:

    if value not in unique:
        unique.append(value)

print("Without duplicates:", unique)

# ------------------------------------------
# Q10. Find second smallest manually

nums = [8,3,1,6,2,9]

smallest = min(nums)

remaining = []

for value in nums:

    if value != smallest:
        remaining.append(value)

second_smallest = min(remaining)

print("Second smallest:", second_smallest)

# ------------------------------------------
# Q11. Simple Bubble Sort

nums = [5,2,8,1,3]

for i in range(len(nums)):

    for j in range(len(nums)-1):

        if nums[j] > nums[j+1]:

            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

print("Sorted list:", nums)

# ------------------------------------------
# Q12. Rotate list left side once

nums = [1,2,3,4,5]

first = nums[0]

for i in range(len(nums)-1):

    nums[i] = nums[i+1]

nums[-1] = first

print("Left rotated list:", nums)

# ------------------------------------------
# Q13. Rotate list right side twice

nums = [1,2,3,4,5]

for k in range(2):

    last = nums[-1]

    for i in range(len(nums)-1, 0, -1):

        nums[i] = nums[i-1]

    nums[0] = last

print("Right rotated list:", nums)

# ==========================================
# KEY LEARNINGS
# ==========================================

# append() --> adds element to list

# range(len(list))
# --> helps access index positions

# Bubble Sort:
# compares adjacent elements
# swaps if order is wrong

# Rotation:
# shifting elements left/right

# Consecutive values:
# compare current with next element

# Manual logic improves problem solving
# ==========================================