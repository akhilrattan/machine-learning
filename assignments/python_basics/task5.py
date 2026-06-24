for i in range(1, 101):
    print(i)
print("ever numbers")
for i in range(2, 101, 2):
    print(i)
print("odd numbers")
for i in range(1, 100, 2):
    print(i)
n = int(input("enter the number "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i

print("sum =", sum_n)

for i in range(1, n + 1):
    print(i, "square =", i * i)

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)

number = input("Enter number: ")
print("Digits =", len(number))