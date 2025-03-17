import json
import os

data_file = "library.txt"


def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []


def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)


def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    publication_year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    new_book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read_status": read_status,
    }
    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully!")


def remove_book(library):
    title = input("Enter the title of the book to remove: ").lower()
    initial_length = len(library)
    library = [book for book in library if book["title"].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed successfully!")
    else:
        print(f"Book '{title}' not found.")


def search_library(library):
    search_by = input("Search by (title/author): ").lower()
    if search_by not in ["title", "author"]:
        print("Invalid search criteria. Please choose 'title' or 'author'.")
        return
    search_term = input(f"Enter the {search_by}: ").lower()
    results = [book for book in library if search_term in book[search_by].lower()]
    if results:
        for book in results:
            status = "Read" if book.get("read_status") else "Unread"
            print(
                f"Matching Book: {book.get('title')} by {book.get('author')} - {book.get('publication_year')} - {book.get('genre')} - {status}"
            )
    else:
        print(f"No matching books found for '{search_term}' in the {search_by} field.")


def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book.get("read_status") else "Unread"
            print(
                f"{book.get('title')} by {book.get('author')} - {book.get('publication_year')} - {book.get('genre')} - {status}"
            )
    else:
        print("The library is empty.")


def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book.get("read_status")])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")


def main():
    library = load_library()
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
