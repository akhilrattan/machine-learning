marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"
print(grade)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)
print("Largest number:", largest)

year = int(input("Enter year: "))
if (year % 4 == 0):
    print("leap year")
else:
    print("not leap year")