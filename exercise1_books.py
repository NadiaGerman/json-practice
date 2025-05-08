import json

BOOKS_FILE = 'data/books.json'

# === Load books from JSON ===
with open(BOOKS_FILE, 'r') as f:
    books = json.load(f)

# === Print current books ===
print("📚 Book List:")
for book in books:
    print(f"- {book['title']} by {book['author']} ({book['year']})")

# === Ask user if they want to add books ===
choice = input("\nWould you like to add books? (y/n): ").strip().lower()

if choice == 'y':
    while True:
        print("\n➕ Add a New Book:")
        title = input("Title: ")
        author = input("Author: ")
        try:
            year = int(input("Year: "))
        except ValueError:
            print("⚠️ Invalid year. Try again.")
            continue

        new_book = {
            "title": title,
            "author": author,
            "year": year
        }

        books.append(new_book)
        print(f"✅ Added '{title}' by {author} ({year})")

        again = input("Add another book? (y/n): ").strip().lower()
        if again != 'y':
            break

    # === Save updated list ===
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=2)

    print("\n📁 All new books saved.")
else:
    print("\nℹ️ No changes made.")
