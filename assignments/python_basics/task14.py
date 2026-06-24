employee = {}

def employee_record():
    name = input("\nenter the employee name : ")
    employee_id = input("enter the employee id : ")
    description = input("enter the description of employee : ")
    salary = int(input("enter the salary of the employee : "))

    employee[employee_id] = {
        "name": name,
        "description": description,
        "salary": salary
    }

    print("employee added")
    
def display_employees():
    for emp_id, data in employee.items():
        print(emp_id, data)

def search_emp():
    empid = input("enter the employee id to see the details")
    if empid in employee:
        print("the name of the empoyee is : ", employee[empid]["name"])
        print("the description of the empoyee is : ", employee[empid]["description"])
        print("the salary of the empoyee is : ", employee[empid]["salary"])
    else:
        print("invalid detials")

def update_employee():
    empid = input("enter the employee id to update")

    employee[empid]["name"] = input("enter the new name : ")
    employee[empid]["salary"] = input("enter the new salary : ")
    employee[empid]["description"] = input("enter the new desription : ")

    print("updated successfully")

def delete_employee():
    empid = input("enter the employee id to delete")

    if empid in employee:
        del employee[empid]
    print("deleted")

def calc_average():
    totalsum = 0
    for data in employee.values():
        totalsum += data["salary"]
    print(totalsum / len(employee))

while True:
    print("press 1 to add employee")
    print("press 2 to display employee")
    print("press 3 to search employee")
    print("press 4 to update employee")
    print("press 5 to delete employee")
    print("press 6 to find average salary of employees")
    
    a = input("enter your choice")
    if(a == "1"):
        employee_record()
    elif(a == "2"):
        display_employees()
    elif(a =="3"):
        search_emp()
    elif(a == "4"):
        update_employee()
    elif(a == "5"):
        delete_employee()
    elif(a == "6"):
        calc_average()
    else:
        print("type valid number")