# Write your code here!


data = {"temp": 22.5,
        "color": "blue",
        }
def temp_and_color(data):
    if not isinstance(data, dict):
        return None, None
    if "color" not in data or "temp" not in data:
        return None, None
    return data.get("temp"), data.get("color")
print(temp_and_color(data))