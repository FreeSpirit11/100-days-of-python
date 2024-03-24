# Flask Blog

This is a simple Flask application that allows users to create, edit, view, and delete blog posts. Users can write blog posts using the CKEditor for rich text formatting.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/8283f8a2-2d45-411d-b9f8-b9d87a946604


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
5. Access the application in your web browser at `http://localhost:5003`.

## Usage

- **Home Page**: View all blog posts.
- **New Post**: Create a new blog post.
- **Edit Post**: Edit an existing blog post.
- **Delete Post**: Delete a blog post.
- **About Page**: Information about the blog or the author.
- **Contact Page**: Contact form or information.

## Features

- **Create New Post**: Users can create a new blog post by providing a title, subtitle, author name, blog image URL, and content.
- **Edit Post**: Users can edit existing blog posts by updating the title, subtitle, author name, blog image URL, and content.
- **Delete Post**: Users can delete blog posts.
- **Rich Text Formatting**: CKEditor allows users to format text, add images, and more.
- **About and Contact Pages**: Additional pages for information about the blog or author and a contact form.

## Database

The application uses SQLite for the database. The `BlogPost` table stores blog posts with fields such as title, subtitle, date, body, author, and image URL.
