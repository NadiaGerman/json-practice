import json

# === Load books from JSON ===
with open('data/books.json', 'r') as f:
    books = json.load(f)

# === Print all books ===
print(" Book List:")
for book in books:
    print(f"- {book['title']} by {book['author']} ({book['year']})")
