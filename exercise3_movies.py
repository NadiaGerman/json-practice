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

    with open(MOVIES_FILE, 'w') as f:
        json.dump(movies, f, indent=2)

    print(f"✅ '{title}' added to the movie list.")
else:
    print("ℹ️ No movie added.")

# === Ask if user wants to update a movie rating ===
update_choice = input("\nWould you like to update a movie rating? (y/n): ").strip().lower()

if update_choice == 'y':
    update_title = input("Enter the title of the movie to update: ").strip().lower()
    for movie in movies:
        if update_title == movie["title"].lower():
            try:
                new_rating = float(input(f"Enter new rating for '{movie['title']}': "))
                movie["rating"] = new_rating
                with open(MOVIES_FILE, 'w') as f:
                    json.dump(movies, f, indent=2)
                print(f"✅ Updated rating for '{movie['title']}' to {new_rating}")
            except ValueError:
                print("⚠️ Invalid rating. Must be a number.")
            break
    else:
        print("❌ Movie not found.")
else:
    print("ℹ️ No rating updated.")
# === Ask if user wants to see top-rated movies ===
report_choice = input("\n📊 Would you like to see the top 3 rated movies? (y/n): ").strip().lower()

if report_choice == 'y':
    print("\n🏆 Top 3 Movies:")
    sorted_movies = sorted(movies, key=lambda m: m['rating'], reverse=True)
    for movie in sorted_movies[:3]:
        print(f"- {movie['title']} ({movie['year']}): ⭐ {movie['rating']}")
else:
    print("ℹ️ Report skipped.")
