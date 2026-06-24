student = {
    "name": "Akhil",
    "age": 21,
    "marks": [80, 90, 85]
}

student["city"] = "Mandi"

student["age"] = 22

del student["city"]

print("Keys:", student.keys())
print("Values:", student.values())

key = input("Enter key to search: ")

if key in student:
    print("Found:", student[key])
else:
    print("Not Found")

avg = sum(student["marks"]) / len(student["marks"])
print("Average Marks =", avg)

sorted_dict = dict(sorted(student.items()))
print(sorted_dict)