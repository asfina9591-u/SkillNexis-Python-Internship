# Create a JSON file and read data
import json

data = {
    "name": "Asfina",
    "course": "Python Internship",
    "week": 3
}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)

print("Loaded JSON:", loaded)
