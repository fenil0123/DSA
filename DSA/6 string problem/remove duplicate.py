# remove repeat  element in word
text = "banana"
result = ""

for i in text:
    if i  not in result :
        result = result + i
print(result)

#4. Practice questions
# 1. Remove duplicate characters from "apple".
word = "appple"
result = "" 
for i in word:
    if i not in result:
        result = result + i
print(word)

# 2. Remove duplicate characters from "programming".
name = "programming"
result = ""
for i in name:
    if i not in result:
        result = result + i
print(result)

# 3. Take a string from the user and remove duplicate characters while keeping their original order.

str = input("Enter one word:")
result = "" 
for i in str:
    if i not in result:
        result = result + i
print(result)
