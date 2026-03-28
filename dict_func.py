# Write your code here!
employee_info = {"Name": "Juan",
                 "Salary": 30000,
                 "Role": "Developer",
                 "Years at Company": 5,
                 "Department": "IT"}
def employee_print(employee_info):
    info = dict(employee_info)

    name = info.pop("Name", "N/A")
    salary = info.pop("Salary", "N/A")
    role = info.pop("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    if info:
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")
employee_print(employee_info)