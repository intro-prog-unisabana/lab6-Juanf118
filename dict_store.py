# Write your code here!


data = {"temp": 22.5,
        "color": "blue",
        "status": "ok"
        }
def temp_and_color(values):
    if "temp" not in data and "color" not in data:
          return None

    return data.get("temp"), data.get("color")

print(temp_and_color(data.values()))