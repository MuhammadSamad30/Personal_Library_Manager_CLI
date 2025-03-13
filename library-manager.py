import json
import os

data_file = 'library.txt'


def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []


def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file)


def add_book(data):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    data.append(new_book)
    save_data(data)
    print(f'Book {title} added successfully!')


def remove_book(data):
    title = input('Enter the title of the book you want to remove: ')
    for book in data:
        if book['title'] == title:
            data.remove(book)
            save_data(data)
            print(f'Book {title} removed successfully!')
            return
    print(f'Book {title} not found!')


def search_book(data):
    title = input('Enter the title of the book you want to search: ')
    for book in data:
        if book['title'] == title:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read: {'Yes' if book['read'] else 'No'}")
            return
    print(f'Book {title} not found!')


def display_all_books(data):
    if data:
        for book in data:
            status = 'Read' if book['read'] else 'unread'
            print(
                f'{book['title']} by {book['author']} {book['year']} {book['genre']} - {status}')
    else:
        print('No books found!')


def display_statistics(data):
    total_books = len(data)
    total_read = len([book for book in data if book['read']])
    percentage_read = (total_read / total_books) * \
        100 if total_books > 0 else 0

    print(f'Total books: {total_books}')
    print(f'percentage read: {percentage_read:.2f}%')


def main():
    data = load_data()

    while True:
        print('')
        print('Welcome to your Personal Library Manager! - Created by Muhammad Samad')
        print('')
        print('1. Add a book')
        print('2. Remove a book')
        print('3. Search for a book')
        print('4. Display all books')
        print('5. Display statistics')
        print('6. Exit')
        print('')

        choice = input('Enter your choice:')
        if choice == '1':
            add_book(data)
        elif choice == '2':
            remove_book(data)
        elif choice == '3':
            search_book(data)
        elif choice == '4':
            display_all_books(data)
        elif choice == '5':
            display_statistics(data)
        elif choice == '6':
            print('Bye Have a great day!')
            break
        else:
            print('Invalid choice!')


if __name__ == '__main__':
    main()
