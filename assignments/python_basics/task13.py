students = {}

def create_student():
    name = input("enter the name : ")
    rollno = input("enter the roll number : ")
    student_info = (name,rollno)
    marks = list(map(int, input("eneter the marks : ").split()))
    subject = set(input("enter the subjects : ").split())
    if len(marks) == len(subject):
        students[rollno] = {
            "info": student_info,
            "subjects": subject,
            "marks": marks
        }
        print("student added !")
    else:
        print("invalid subjects")



def search_students():
    rollno = input("enter the roll no to search : ")

    if rollno in students:
        data = students[rollno]
        print("the name of student is : ",data["info"][0])
        print("roll no is : ", data["info"][1])
        print("the subject is : ",data["subjects"])
        print("the marks obtained are : ",data["marks"])
    else:
        print("no such student exists")

def calc_averagemarks():
    rollno = input("enter the student roll no : ")
    print("the average marks for student is : ")
    markssum = sum(students[rollno]["marks"])
    average_marks =  markssum / len(students[rollno]["marks"])
    print(average_marks)

def display_info():
    highest_marks = 0
    topper_name = ""
    for i in students.values() :
        av = sum(i["marks"])/len(i["marks"])
    
        if av > highest_marks:
            highest_marks = av
            topper_name = i["info"][0]
    print("toppers name : ", topper_name)
    print("highest marks ; ",highest_marks)

while True:
    print("press 1 to add student")
    print("press 2 to search student")
    print("press 3 to calculate averga marks student")
    print("press 4 to view the topper details")
    print("press 5 to exit")

    a = input("enter your choice")
    if(a == "1"):
        create_student()
    elif(a == "2"):
        search_students()
    elif(a =="3"):
        calc_averagemarks()
    elif(a == "4"):
        display_info()
    elif(a == "5"):
        break
    else:
        print("type valid number")