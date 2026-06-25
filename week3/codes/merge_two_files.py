# Merge two text files
file1 = "file1.txt"
file2 = "file2.txt"
output = "merged.txt"

with open(file1, "r") as f1, open(file2, "r") as f2, open(output, "w") as out:
    out.write(f1.read() + "\n" + f2.read())

print("Files merged into merged.txt")
