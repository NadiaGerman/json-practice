import json

STUDENTS_FILE = 'data/students.json'

# === Load student data ===
with open(STUDENTS_FILE, 'r') as f:
    students = json.load(f)

# === Print average grade for each student ===
print("📊 Student Averages:")
for student in students:
    name = student["name"]
    grades = student["grades"]
    avg = sum(grades) / len(grades)
    print(f"- {name}: {avg:.2f}")
