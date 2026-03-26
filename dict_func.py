# Write your code here!
employee_info = {"Name": "Juan",
                 "Salary": 30,
                 "Role": "Developer"}
def employee_print():
    for key, value in employee_info.items():
        print(f"{key}: {value}")
        print("No other info!")
employee_print()