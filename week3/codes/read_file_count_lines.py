# Read a file and count total lines
filename = "sample.txt"

with open(filename, "r") as f:
    lines = f.readlines()

print("Total Lines:", len(lines))
