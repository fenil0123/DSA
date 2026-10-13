
# # Input first 3x3 matrix
# print("Enter elements of the first matrix:")

# A = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         num = int(input(f"Enter element [{i}][{j}]: "))
#         row.append(num)
#     A.append(row)


# print("\nEnter elements of the second matrix:")

# B = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         num = int(input(f"Enter element [{i}][{j}]: "))
#         row.append(num)
#     B.append(row)


# C = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(A[i][j] + B[i][j])
#     C.append(row)


# print("\nAddition of two matrices:")
# for row in C:
#     print(row)




#  prctice 
# D = []
# for i in range(3):
#     ROW = []
#     for j in range(3):
#         num = int(input(f"Enter element [{i}][{j}]:"))
#         ROW.append(num)
#     D.append(ROW)
# print(D)

# E = []
# for i in range(3):
#     ROW = []
#     for j in range(3):
#         num = int(input(f"Enter element [{i}][{j}]:"))
#         ROW.append(num)
#     E.append(ROW)
# print(E)

# Q = []
# for i in range(3):
#     ROW = []
#     for j in range(3):
#         ROW.append(D[i][j] + E[i][j])
#     Q.append(ROW)
# print(Q)

# text = "banana"
# frequency = {}
# for i in text:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# print(frequency)



text = " banana"
result = ""
for i in text:
    if i not in result:
        result = result + i
print(result)