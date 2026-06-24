def greet():
    print("hello")

def add(a, b):
    return a + b

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def palindrome(text):
    return text == text[::-1]

greet()
print(add(10, 20))
print(factorial(5))
print(palindrome("aadf"))