# anagrams
text = "fenil"
name = "lenif"

if sorted(text) == sorted(name):
    print("word is anagrams")
else:
    print("word is not anagrams")


# . Practice questions
# 1. Check whether "race" and "care" are anagrams.
name1 = "race"
name2 = "care"
if sorted(name1) == sorted(name2):
    print("name1 and name2 is anagrams")
else:
    print("its not anangrams word")



# 2. Check whether "earth" and "heart" are anagrams.
str1 = "earth"
str2 = "heart"
if sorted(str1) == sorted(str2):
    print("str1 and str2 are word is anagrams")
else:
    print("word is not anagrams")

# 3. Take two strings from the user and check whether they are anagrams.
string1 = input("Enter one word:")
string2 = input("Enter one more word:")
if sorted(string1) == sorted(string2):
    print("string1 and string2 are anagrams")
else:
    print("user enter word is not anagrams")