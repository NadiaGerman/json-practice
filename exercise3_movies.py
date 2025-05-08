import json

MOVIES_FILE = 'data/movies.json'

# === Load movie data ===
with open(MOVIES_FILE, 'r') as f:
    movies = json.load(f)

# === Search for a movie ===
search = input("🔍 Enter a movie title to search: ").strip().lower()
found = False
for movie in movies:
    if search in movie["title"].lower():
        print(f"🎬 {movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
        found = True

if not found:
    print("❌ Movie not found.")

# === Ask if user wants to add a new movie ===
add_choice = input("\nWould you like to add a new movie? (y/n): ").strip().lower()

if add_choice == 'y':
    print("\n➕ Add a New Movie:")
    title = input("Title: ")
    try:
        year = int(input("Year: "))
        rating = float(input("Rating (0.0 - 10.0): "))
    except ValueError:
        print("⚠️ Invalid input. Aborting.")
        exit(1)

    new_movie = {
        "title": title,
        "year": year,
        "rating": rating
    }

    movies.append(new_movie)

    # Save updated list
    with open(MOVIES_FILE, 'w') as f:
        json.dump(movies, f, indent=2)

    print(f"✅ '{title}' added to the movie list.")
else:
    print("ℹ️ No movie added.")
