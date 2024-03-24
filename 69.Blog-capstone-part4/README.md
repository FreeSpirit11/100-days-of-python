# Flask Blog

This is a Flask web application for creating and managing blog posts. Users can register, log in, create, edit, and delete blog posts. The application also allows users to leave comments on posts and includes a contact form for sending messages to the administrator.

https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/a84a3239-2077-4699-9fd3-239eefda3151


## Features

- **User Authentication**: Users can register, log in, and log out. Passwords are securely hashed before being stored in the database.
- **Authorization**: Certain routes, such as creating, editing, and deleting posts, are restricted to administrators only.
- **Create, Edit, Delete Posts**: Authenticated administrators can create, edit, and delete blog posts.
- **Comments**: Users can leave comments on blog posts. Only authenticated users can comment.
- **Contact Form**: Users can send messages to the administrator using the contact form.

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python installed on your system.
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables for email configuration (`EMAIL_KEY` and `PASSWORD_KEY`) if using the contact form feature.
5. Run the application:
   ```
   python main.py
   ```
6. Access the application in your web browser at `http://localhost:5002`.

## Usage

- **Home Page**: Displays a list of all blog posts.
- **Register**: Allows users to register by providing their name, email, and password.
- **Login**: Allows registered users to log in with their email and password.
- **Logout**: Logs out the current user.
- **Post Details**: Displays the details of a single blog post, including comments.
- **Create Post**: Authenticated administrators can create new blog posts.
- **Edit Post**: Authenticated administrators can edit existing blog posts.
- **Delete Post**: Authenticated administrators can delete blog posts.
- **About Page**: Provides information about the website or the author.
- **Contact Page**: Allows users to send messages to the administrator.

## Dependencies

- Flask: Micro web framework for Python.
- Flask-Bootstrap: Integration of Bootstrap with Flask.
- Flask-CKEditor: Rich text editor for Flask.
- Flask-Gravatar: Gravatar integration for Flask.
- Flask-Login: User session management for Flask.
- Flask-SQLAlchemy: SQLAlchemy integration for Flask.
- WTForms: Forms validation and rendering library for Flask.
- Werkzeug: WSGI utility library for Python.

## Acknowledgements

This project is a part of the "100 Days of Code" challenge by Angela Yu.
