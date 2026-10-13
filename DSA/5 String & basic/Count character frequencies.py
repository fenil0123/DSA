#Character frequency means counting how many times each character appears in a string.

text = "banana"
frequency = {} # empty dictionary

for i in text: # check i in text
    if i in frequency: 
        frequency[i] += 1 # if i is alredy in dicrionary then value of it increase by 1
    else:
        frequency[i] = 1 # if i is not found in twice then value is as it 

print(frequency) # print dictionary

# Q-1
# Count the frequency of each character in "apple".
text = "apple"
frequency = {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)

# Count the frequency of each character in "programming".
str = "programming"
fre = {}

for i in str:
    if i in fre:
        fre[i] += 1
    else :
        fre[i] = 1
print(fre)

# Take a string from the user and count how many times each character appears.

name = input("Enter any single word of name:")
nam = {}
for i in name:
    if i in nam:
        nam[i] += 1
    else:
        nam[i] = 1
print(nam)