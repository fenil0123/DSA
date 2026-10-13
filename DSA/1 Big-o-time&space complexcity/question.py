# 1). Find complexity of a single loop.
# r = 8
# for i in range(r):
#     print(i)
    
# print("time complexcit is o(n)")


# 2). Find complexity of nested loops.
# n = 9 
# for i in range(n):
#     for j in range(n):
#         print(i,j)
# print(" time copmlexcity : o(logn)" )


# 3). Compare O(1), O(log n), O(n), O(n²).
#o(1)
# a = 10
# b = 22
# c = a + b
# print(c)

#o(logn)
# l = 6 
# for i in range(l):
#     i = i/2
#     print(i)

#o(n)
# n =  6
# for i in range(n):
#     print(i)

#o(n^2)
# k = 2
# for i in range(k):
#     for j in range(k):
#        print(i,j)


# 4). Write a Python program using a single for loop to print numbers from 1 to n.
# n = int(input("Enter n Number: "))
# for i in range(3,n+1):
#     print(i)



# 5) Write a Python program using a single loop to calculate the sum of numbers from 1 to n.
# n = int(input("Enter n Number:"))
# sum = 0
# for i in range(n):
#     sum = sum + i
#     print(sum)



# 6)  Write a Python program using a loop to print all even numbers from 1 to n.
# n = int(input("Enter n Number: "))
# for i in range(1,n + 1):
#     if i % 2 == 0:
#         print(i)
   


#  7)Write a Python program using a loop to print all odd numbers from 1 to n.
# n = int(input("Enter n Number: "))
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print(i)

# 8) Write a Python program using a loop to find the factorial of n.
# n = int(input("Enter a Number: "))
# factorial = 1
# for i in range(1,n + 1):
#     factorial = factorial * i
#     print(factorial)


# 9) Write a Python program using a loop to find the largest number in a list.
# list = [4,3,9,5,6,4,7]
# largest = list[0]
# for i in list:
#     if i > largest:
#         largest = i
#         print(i)

# 10) Write a Python program using a loop to find the samll number in a list.
# list = [6,5,4,7,8,3,2,8]
# small = list[0]
# for i in list:
#     if i < small:
#         small = i
#         print(small)
# 11)Write a Python program using a loop to count how many elements are present in a list.
# list = [1,2,3,4,5,6]
# count = 0
# for i in list:
#     count = count + 1
#     print(count)
# 12) ssssssWrite a Python program using two nested loops to print all pairs of elements from a list.
n = int(input("Enter a Number:"))
for i in range(n):
    for j in range(n):
        print(i,j)
# Write a Python program using nested loops to print this pattern:






