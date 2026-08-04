employee={}
EmployeeID=input("Enter Employee ID: ")
employee["ID"]=EmployeeID
EmployeeName=input("Enter Employee Name: ")
employee["Name"]=EmployeeName
EmployeeDepartment=input("Enter Employee Department: ")
employee["Department"]=EmployeeDepartment
salary=int(input("Enter Employee Salary: "))
employee["SALARY"]=salary
print("Employee's name is: ", EmployeeName)
salary+=salary*0.10
print("Employee's salary after 10% increment is: ", salary)
email=input("Enter Employee Email: ")
employee["Email"] = email
print("Employee Record:")
print(employee)
