#Q-1)

# find the sum of elements from index 1 to index 3 using a loop.
arr = [10,20,30,40,50]

start = 1
end = 3
total = 0

for i in range(start,end+1):
    total = total + arr[i]
print(total)

 # Q - 2
    # topic subarray 
# Write a Python program to calculate the sum of the subarray from index 2 to index 4.
arr1 = [5, 10, 15, 20, 25, 30]
start = 2
end = 4
sum = 0 

for i in range(start,end+1):
    sum = sum + arr1[i]
print(sum)


 # Q - 3
# topic prefix sum
# Write a program to create a prefix sum array.
arr = [2, 4, 6, 8, 10]
prefix = []
total1 = arr[0] 
for i in arr:
    total1 = total1 + i
    prefix.append(total1)
print(prefix)

# Q - 4
# Given the array below, calculate the sum for two different ranges using a loop.

# Query 1: Start index 0, end index 2. Expected sum: 60
arr = [10, 20, 30, 40, 50]
start = 0 
end = 2
cal = 0 
for i in range(start , end +1):
    cal = cal + arr[i]
print(cal)

# Query 2: Start index 1, end index 4. Expected sum: 140

arr1= [10, 20, 30, 40, 50]
start = 1
end = 4

calculate = 0 
for i in range(start,end + 1):
    calculate = calculate + arr1[i]
print(calculate)


# Q - 5
# create a prefix sum array first, then use it to find the sum from index 1 to index 3 without looping through 
# the selected elements again.
arr = [5, 10, 15, 20, 25]
prefix = []
total = arr[0] 
for i in arr:
    total = total + i
    prefix.append(total)
print(prefix)
start = 1
end = 3
sum = 0
for i in range(start,end + 1):
    sum = sum + i 
print(sum)
