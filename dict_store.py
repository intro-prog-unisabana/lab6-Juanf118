# Write your code here!


data = {"temp": 25,
        "color": "blue"
        }
def temp_and_color(values):
 #temp = print (data.get("temp"))
 #color = print (data.get("color"))


 return data.get("temp"), data.get("color")

print(temp_and_color(data.values()))