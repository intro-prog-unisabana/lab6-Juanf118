# Write your code here!
employee_info = {"Name": "Juan",
                 "Salary": 30000,
                 "Role": "Developer"}
def employee_print(employee_info):
    for key, value in employee_info.items():
        print(f"{key}: {value}")
    valores_temp = employee_info.pop("Name, Salary, Role")
    after_print = "No other info!"
    employee_info
    print(after_print)
employee_print(employee_info)