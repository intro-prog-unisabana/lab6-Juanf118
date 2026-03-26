# Write your code here!


data = {"temp": 22.5,
        "color": "blue",
        }
def temp_and_color(values):
    if not isinstance(values, dict):
        return None, None
    if "color" not in values or "temp" not in values:
        return None, None
    return values.get("temp"), values.get("color")
print(temp_and_color(data))