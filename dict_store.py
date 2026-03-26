# Write your code here!


data = {"temp": 22.5,
        "color": "blue",
        }
def temp_and_color(values):
    if "temp" in data and "color" in data:

        return data.get("temp"), data.get("color")
    if "temp" not in data and "color" not in data:
        return None, None

print(temp_and_color(data))