# Book Collection Flask App

This Flask application allows users to manage a collection of books, including adding, editing, and deleting entries. It utilizes SQLAlchemy for database management and follows a simple CRUD (Create, Read, Update, Delete) functionality.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/8f29b243-dfc1-4579-a606-d63199ba096e


## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python and pip installed on your system.
3. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the application:
    ```
    python main.py
    ```
5. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage

- **Home Page**: View all books in the collection with their titles, authors, and ratings. You can add, edit, or delete books from this page.
- **Add Book**: Add a new book to the collection by providing its title, author, and rating.
- **Edit Book**: Update the rating of an existing book.
- **Delete Book**: Remove a book from the collection.

## File Structure

- `main.py`: Contains the Flask application code including routes and database setup.
- `templates/`: Directory containing HTML templates for rendering pages.
- `static/`: Directory for static files such as CSS stylesheets or client-side scripts.
- `Book-collection.db`: SQLite database file storing book data.

## Dependencies

- Flask: Micro web framework for Python.
- Flask SQLAlchemy: Flask extension for working with SQLAlchemy database.
- SQLite: Lightweight relational database management system.
- WTForms: Library for building web forms in Flask applications.
- Bootstrap: Front-end framework for designing responsive and mobile-first websites.

## Credits

This project is inspired by the Flask tutorial series by Angela Yu on Udemy.
