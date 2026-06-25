# Student Management System using CSV
import csv

filename = "students.csv"

def add_student(name, roll, marks):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, roll, marks])

def search_student(roll):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == roll:
                return row
    return "Not Found"

def delete_student(roll):
    rows = []
    found = False
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] != roll:
                rows.append(row)
            else:
                found = True
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return "Deleted" if found else "Not Found"

# Example usage
add_student("Asfina", "101", "85")
print(search_student("101"))
print(delete_student("101"))
