import json

BOOKS_FILE = 'data/books.json'

# === Load books from JSON ===
with open(BOOKS_FILE, 'r') as f:
    books = json.load(f)

# === Print current books ===
print("📚 Book List:")
for book in books:
    print(f"- {book['title']} by {book['author']} ({book['year']})")

# === Add a new book ===
print("\n➕ Add a New Book:")
title = input("Title: ")
author = input("Author: ")
year = int(input("Year: "))

new_book = {
    "title": title,
    "author": author,
    "year": year
}

books.append(new_book)

# === Save updated list ===
with open(BOOKS_FILE, 'w') as f:
    json.dump(books, f, indent=2)

print(f"\n✅ Book '{title}' added and saved.")
