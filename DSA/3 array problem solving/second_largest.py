
# arr = [10, 25, 7, 40, 30]

# largest = arr[0] # 10
# second = arr[0] #10

# for i in arr: # i = 10 
#     if i > largest: # 10 != 10 take i = 25
#         second = largest # second = 10
#         largest = i # largest = 25  
#     elif i > second and i != largest: # 30 > 10 but != 40
#         second = i # 30 

# print("Largest =", largest)
# print("Second Largest =", second)



# topic - 1 

# Q-1) find second largest number in array
# 1)
# arr1 = [12, 45, 23, 67, 34, 89, 56]
# largest = arr1[0] # first take 12
# second = arr1[0] # first take 12

# for i in arr1: # take 45
#     if i > largest: # 45 > 12
#         second = largest # 12
#         largest = i # 45
#     elif i > second  and  i != largest: # 23 > 12 but != 45 
#         second = i # 23 

# print("largest :",largest)
# print("second largest : ",second)

#2)
# arr2 = [5, 10, 15, 20, 25]

# largest = arr2[0]
# second =arr2[0]

# for i in arr2:
#     if i > largest:
#         second = largest
#         largest = i 
#     elif i > second and i != largest:
#         second = i
# print("largest :",largest)
# print("second largest ;",second)

#3)
# arr3 =[45,34,54,32,76,43]
# largest = arr3[0] # first take 45
# second = arr3[0] # first take 45

# for i in arr3:# i = 34 first
#     if i > largest: # 34 !> 45 then take 54
#         second = largest # 45
#         largest = i # 54
#     elif i > second and  i != largest: # 76 > 45 but != 54
#         second = i # 54
# print("largest:",largest)
# print("second largest:",second)


#4) 
# arr4 = [24,45,43,32,56,54]

# largest = arr4[0] # first take 24
# second = arr4[0]  # first take 24 

# for i in arr4:
#     if i > largest: # i = 45 , 45 > 24
#         second = largest  # second = 24 
#         largest = i      # largest = 45
#     elif i > second and  i != largest : # 43 > 24 but != 45
#         second = i  # change second to 43
# print("largest no is :",largest)
# print("second largest no is :",second)


    

#topic - 2
# remove dublicat 

# 1)
# arr = [ 10,20,10,30,20,40]

# arr1 = [] # empty array

# for i in arr: # check i = 10  in arr
#     if i not in arr1:# check i = 10 is in arr1 or not 
#         arr1.append(i) # add 10 in arr1
# print("new array is :",arr1)

# 2) 

# arr = [ 12,34,56,34,56,12,78,16]

# arr1 = []
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)
# print("new array is :",arr1)

# 3)
# arr = [23,45,67,45,44,23,45]

# arr1 = []
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)
# print(" new array is:",arr1)



# topic 3
 # move all zero in the last of array

# arr = [0,5,0,3,8,0,2]

# result = [] #  empty list
# zero_count = 0 

# for i in arr:
#     if i  == 0: # check i is equal to zero
#         zero_count += 1 # count how many zero
#     else:
#         result.append(i) # if not equal to zero then add in result
# for i in  range(zero_count):
#     result.append(0) # all zero move in the last of array

# print(result)


# arr = [0,7,5,6,0,8,0,9,0]

# result = []
# zero_count = 0 

# for i in arr: # o in arr
#     if i == 0: # check i is equal to zero
#         zero_count += 1 # count zero  in  zero_count variable 
#     else:
#         result.append(i) # if i is not equal to 0 then added in result array
# for i in range(zero_count):
#     result.append(0) # zero add in last of array reult
# print(result)



# Q-3
# arr = [2,0,7,6,0,4,0,3,0]
# result = []
# zero_count= 0

# for i in arr:
#     if i == 0:
#         zero_count += 1
#     else:
#         result.append(i)
# for i  in range(zero_count):
#     result.append(0)

# print(result)



# topic find missing number from 1 to n number 

#Q-1
# arr = [0,1,2,3,5,6]
# n = 6 # check number from 1 to 6
# for i in range(1,n+1): # check i is avaible in 1 to 7
#     if i not in arr: # check i is not arr
#         print("missing number is :",i) # missing number


#Q-2
# arr1 = [6,7,8,10,11,12]
# n = 12
# for i in range(1,n+1):
#     if i not in arr1:
#         print("missing number is",i)

#Q-3
# arr2 = [1,2,4,5,6,7]
# n = 7
# for i in range(1,n+1):
#     if i not in arr2:
#         print("missing number is:",i)

