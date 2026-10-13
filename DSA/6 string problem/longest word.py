sentance = "python is easy to understand language."

word = sentance.split()
longest = ""
for word in word:
    if len(word) > len(longest):
        longest = word
print(longest)



# 4. Practice questions


# 1. Find the longest word in "my name is tommy  shalby ".
sentance = "my name is tommy  shalby "
later = sentance.split()
long = ""
for later in later:
    if len(later) > len(long):
        long = later
print(long)

# 2. Find the longest word in "Python developer writes code".

speech = "Python developer writes code"
title = speech.split()
result = ""
for title in title :
    if len(title) > len(result):
        result = title
print(result)
# 3. Take a sentence from the user and print its longest word and its length.
user = input("Enter one line sentance:")
check = user.split()
final = ""
for check in check:
    if len(check) > len(final):
        final = check
print(final)