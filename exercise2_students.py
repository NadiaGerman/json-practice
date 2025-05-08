import json

STUDENTS_FILE = 'data/students.json'

# === Load student data ===
with open(STUDENTS_FILE, 'r') as f:
    students = json.load(f)

# === Print average grade for each student ===
print("📊 Student Averages:")
top_student = None
top_average = 0

for student in students:
    name = student["name"]
    grades = student["grades"]
    avg = sum(grades) / len(grades)
    print(f"- {name}: {avg:.2f}")

    if avg > top_average:
        top_average = avg
        top_student = name

# === Print top student ===
print(f"\n🏅 Top Student: {top_student} with an average of {top_average:.2f}")
