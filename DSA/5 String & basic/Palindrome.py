# Palindrome

text = "madam"
reverse = ""
for i in text:
    reverse = i + reverse

if text == reverse:
    print("1 word is palindrome.")
else:
    print(" 2 word is not palindrome.")

# Check whether "level" is a palindrome.

text = "level"
reverse =  ""
for i in text:
    reverse = i + reverse 
if text == reverse:
    print(" 2 word is palindrome.")
else:
    print(" 2 words is not palindrome.")

# Check whether "python" is a palindrome.

text = "python"
reverse = ""
for i in text:
    reverse = i + reverse
if text == reverse : 
    print("3 word is palindrome.")
else:
    print(" 3 word is not palindrome.")
# Take a word as input from the user and check whether it is a palindrome.
str = input("Enter any single words :")
reverse = ""
for i in str:
    reverse = i + reverse
if text == reverse:
    print("user enter word is palindrome.")
else:
    print("user enterd word is not palindrome.")

