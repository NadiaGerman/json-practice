import json

MOVIES_FILE = 'data/movies.json'

# === Load movie data ===
with open(MOVIES_FILE, 'r') as f:
    movies = json.load(f)

# === Ask user to search for a movie ===
search = input("🔍 Enter a movie title to search: ").strip().lower()

# === Search and print results ===
found = False
for movie in movies:
    if search in movie["title"].lower():
        print(f"🎬 {movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
        found = True

if not found:
    print("❌ Movie not found.")
