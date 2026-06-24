def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print("Factorial =", factorial(5))

for i in range(6):
    print(fibonacci(i), end=" ")

print("\nPower =", power(2, 5))

print(reverse_string("Python"))