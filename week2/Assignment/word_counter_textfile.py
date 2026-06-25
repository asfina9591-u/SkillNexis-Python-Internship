# Word Counter from Text File
filename = "sample.txt"

with open(filename, "r") as f:
    text = f.read()

words = text.split()
lines = text.split("\n")
chars = len(text)

print("Words:", len(words))
print("Lines:", len(lines))
print("Characters:", chars)
