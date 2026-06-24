n = int(input("enter the number : "))
i = 1
while i <= n:
    print(i)
    i += 1
a, b = 0, 1
print("Fibonacci Series")
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
num = int(input("\nEnter number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse =", reverse)

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)

sum_digits = 0
temp = num

while temp > 0:
    sum_digits += temp % 10
    temp //= 10

print("Sum of digits =", sum_digits)
