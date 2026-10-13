# 1) for loop(o(n))
# I) simple loop 

# n = 6
# for i in range(n):
#     print(i)

# II) hard loop

# n = int(input("Enter value of n: "))

# for i in range(n):
#     print(i)


# 2) while loop(o(n))

# n = 9
# i = 0
# while i < n:
#     print(i)
#     i += 1

# 3) nested loop 
# loop inside the loop (o(n^2))

# n = 4 
# for i in range(n):
#     for j in range(n):
#       print(i,j)

#loop inside the loop twice (o(n^3))

# n = 3
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print(i,j,k)

# 4) divide and multiply by 2 loop (o(logn))
#  divide
# n = 6
# for i in range(n):
#     i = i / 2
#     print(i)

# multiply 
# n = 8
# for i in range(n):
#     i = i*2
#     print(i)
    
# 5) nested loop with diffrent size (o(n*m)) 
# n = 3
# m = 6
# for i in range(n):
#     for j in range(m):

#         print(i,j)


# 6) two seprate loop 
# n = 9 
# for i in range(n):
#     print(i)
# for j in range(n):
#     print(j)  

# 7) create new loop
# n = 6 
# result = []
# for i in range(n):
#     result.append(i * 2)
#     print(result)