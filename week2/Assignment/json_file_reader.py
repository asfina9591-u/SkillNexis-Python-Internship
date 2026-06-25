# JSON File Reader
import json

filename = "data.json"

with open(filename, "r") as f:
    data = json.load(f)

print("Formatted Output:")
for key, value in data.items():
    print(f"{key}: {value}")
