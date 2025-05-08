import json

STUDENTS_FILE = 'data/students.json'

# === Load student data ===
with open(STUDENTS_FILE, 'r') as f:
    students = json.load(f)

# === Calculate averages and store leaderboard data ===
leaderboard = []

print("📊 Student Averages:")
for student in students:
    name = student["name"]
    grades = student["grades"]
    avg = sum(grades) / len(grades)
    leaderboard.append((name, avg))
    print(f"- {name}: {avg:.2f}")

# === Find top student ===
top_student = max(leaderboard, key=lambda x: x[1])
print(f"\n🏅 Top Student: {top_student[0]} with an average of {top_student[1]:.2f}")

# === Print leaderboard ===
print("\n🥇 Leaderboard:")
for name, avg in sorted(leaderboard, key=lambda x: x[1], reverse=True):
    print(f"- {name}: {avg:.2f}")
