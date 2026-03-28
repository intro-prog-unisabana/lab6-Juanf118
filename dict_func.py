# Write your code here!
employee_info = {"Name": "Juan",
                 "Salary": 30000,
                 "Role": "Developer",
                 "Years at Company": 5,
                 "Department": "IT"}
def employee_print(employee_info):
    for key, value in employee_info.items():
        print(f"{key}: {value}")
    print("No other info!")
employee_print(employee_info)