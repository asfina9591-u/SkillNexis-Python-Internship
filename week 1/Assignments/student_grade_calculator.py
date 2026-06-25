def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

marks = []
for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))

print("Average =", sum(marks)/len(marks))
print("Grade =", calculate_grade(marks))
