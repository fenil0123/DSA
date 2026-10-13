# find non-repeating charcter
text = "abcdabef"

for i in text:
    if  text.count(i) == 1:
        print("non-repeting word is ", i)
    else:
        print("repeating word is",i)


#4. Practice questions
# 1. Find the first non-repeating character in "programming".

word = "programming"
for i in word:
    if word.count(i) == 1:
        print("non-repeating word is ",i)
    else:
        print("repeating word is",i)

# 2. Find the first non-repeating character in "aabbccde".
name = "aabbccde"

for i in name:
    if name.count(i) == 1:
        print("non-repaeting word is ",i)
    else:
        print("repeating word is",i)

# 3. Take a string from the user and print its first non-repeating character. If none exists, print "No non-repeating character".

str = input("Enter one word:")
for i in str:
    if str.count(i) == 1:
        print("non-repeating word is ",i)
    else:
        print("repeating word is",i)