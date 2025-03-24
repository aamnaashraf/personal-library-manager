import json
import os
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

def load_library():
    """Load library data from JSON file if it exists."""
    if os.path.exists('library.json'):
        with open('library.json', 'r') as f:
            return json.load(f)
    return []

def save_library(books):
    """Save library data to JSON file."""
    with open('library.json', 'w') as f:
        json.dump(books, f)

def display_book(book):
    """Display a single book in a formatted and attractive way."""
    print(Fore.CYAN + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + "║" + Fore.YELLOW + f" Title: {book['title']}".ljust(50) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f" Author: {book['author']}".ljust(50) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f" Year: {book['year']}".ljust(50) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f" Genre: {book['genre']}".ljust(50) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f" Read: {'✔️' if book['read'] else '❌'}".ljust(50) + Fore.CYAN + "║")
    print(Fore.CYAN + "╚" + "═" * 50 + "╝")

def add_book(books):
    """Add a new book to the library."""
    print(Fore.GREEN + "\n➕ Add a New Book")
    book = {
        'title': input(Fore.YELLOW + "Enter title: ").strip(),
        'author': input(Fore.YELLOW + "Enter author: ").strip(),
        'year': int(input(Fore.YELLOW + "Enter publication year: ")),
        'genre': input(Fore.YELLOW + "Enter genre: ").strip(),
        'read': input(Fore.YELLOW + "Have you read this book? (yes/no): ").lower() == 'yes'
    }
    books.append(book)
    print(Fore.GREEN + f"\n✅ '{book['title']}' has been added to your library!")

def remove_book(books):
    """Remove a book from the library by title."""
    title = input(Fore.RED + "\n❌ Enter title of the book to remove: ").strip()
    initial_count = len(books)
    books[:] = [book for book in books if book['title'].lower() != title.lower()]
    
    removed = initial_count - len(books)
    if removed:
        print(Fore.RED + f"\n❌ Removed {removed} copy(ies) of '{title}'")
    else:
        print(Fore.RED + f"\n❌ No books found with title: '{title}'")

def search_books(books):
    """Search books by title or author."""
    search_type = input(Fore.BLUE + "\n🔍 Search by (1) Title or (2) Author? [1/2]: ")
    search_term = input(Fore.BLUE + "Enter search term: ").lower().strip()

    results = []
    for book in books:
        if search_type == '1' and search_term in book['title'].lower():
            results.append(book)
        elif search_type == '2' and search_term in book['author'].lower():
            results.append(book)

    if results:
        print(Fore.BLUE + f"\n🔍 Found {len(results)} matching book(s):")
        for book in results:
            display_book(book)
    else:
        print(Fore.BLUE + "\n🔍 No matching books found.")

def display_stats(books):
    """Display library statistics."""
    total = len(books)
    read = sum(book['read'] for book in books)
    
    print(Fore.MAGENTA + "\n📊 Library Statistics")
    print(Fore.MAGENTA + f"📚 Total books: {total}")
    if total > 0:
        print(Fore.MAGENTA + f"📖 Percentage read: {(read/total)*100:.1f}%")
    else:
        print(Fore.MAGENTA + "📖 Percentage read: 0.0%")

def main():
    
    books = [
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'genre': 'Classic', 'read': True},
        {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'genre': 'Dystopian', 'read': False},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'genre': 'Fiction', 'read': True},
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813, 'genre': 'Romance', 'read': False},
        {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951, 'genre': 'Literary Fiction', 'read': True},
    ]
    
    # Load additional books from file if available
    books.extend(load_library())
   # Welcome message with gradient colors
    print(Fore.RED + Style.BRIGHT + "✨" * 20)
    print(Fore.RED + Style.BRIGHT + "✨ " + Fore.YELLOW + "Welcome to " + Fore.GREEN + "Personal Library Manager!" + Fore.RED + " ✨")
    print(Fore.RED + Style.BRIGHT + "✨" * 20)
    
    while True:
        print(Fore.CYAN + "\n📚 Main Menu")
        print(Fore.CYAN + "1. ➕ Add a book")
        print(Fore.CYAN + "2. ❌ Remove a book")
        print(Fore.CYAN + "3. 🔍 Search books")
        print(Fore.CYAN + "4. 📖 Display all books")
        print(Fore.CYAN + "5. 📊 Show statistics")
        print(Fore.CYAN + "6. 🚪 Exit")
 
        choice = input(Fore.YELLOW + "\nEnter your choice [1-6]: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            if books:
                print(Fore.GREEN + "\n📚 Your Library:")
                for book in books:
                    display_book(book)
            else:
                print(Fore.RED + "\n📚 Your library is empty!")
        elif choice == '5':
            display_stats(books)
        elif choice == '6':
            save_library(books)
            print(Fore.YELLOW + "\n🚪 Library saved. Goodbye! 👋")
            break
        else:
            print(Fore.RED + "\n❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()