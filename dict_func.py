# Write your code here!
employee_info = {"Name": "Juan",
                 "Salary": 30,
                 "Role": "Developer"}
def employee_print(employee_info):
    for key, value in employee_info.items():
        print(f"{key}: {value}")
    after_print = "No other info!"
    print(after_print)
employee_print(employee_info)