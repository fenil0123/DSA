text = "hello"
vowels = 0 
constant = 0
for i in text:
    if i in "aeiou":
        vowels  += 1
    else:
        constant += 1
print("vowels:",vowels)
print("constant:",constant)

#Practice questions

# Count vowels and consonants in "computer".

text = "computer"
vowels = 0 
constant = 0 
for i in text:
    if  i in "aeiou":
        vowels += 1
    else:
        constant += 1

print("vowels:",vowels)
print("constant:",constant)


# Count vowels and consonants in "PROGRAMMING".

text = "PROGRAMMING"

vowels = 0
constant = 0 
for i in text:
    if i in "aeiou":
        vowels += 1
    else:
        constant += 1
print("vowels:",vowels) 
print("constant:",constant)
# Take a sentence from the user and count its vowels and consonants.
str = input("Enter any single word:")
vowels = 0 
constant = 0
for i in str:
    if i in "aeiou":
        vowels += 1
    else:
        constant += 1
print("vowels:",vowels)
print("constant:",constant)