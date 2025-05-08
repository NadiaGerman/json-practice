import json

BOOKS_FILE = 'data/books.json'

def load_books():
    with open(BOOKS_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=2)

def show_books(books):
    print("\n📚 Book List:")
    for book in books:
        print(f"- {book['title']} by {book['author']} ({book['year']})")

def add_books(books):
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

def main():
    books = load_books()

    while True:
        print("\n📘 MENU:")
        print("1. Show all books")
        print("2. Add new books")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            show_books(books)
        elif choice == '2':
            add_books(books)
            save_books(books)
            print("💾 Books saved.")
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
