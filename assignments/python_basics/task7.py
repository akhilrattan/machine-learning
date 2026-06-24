text = input("Enter string: ")
print("Length =", len(text))
print("Upper =", text.upper())
print("Lower =", text.lower())
print("Reverse =", text[::-1])
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
vowels = "aeiouAEIOU"
v = 0
c = 0
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels =", v)
print("Consonants =", c)