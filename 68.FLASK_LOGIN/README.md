# Flask User Authentication

This is a Flask application that implements user authentication using Flask-Login and SQLAlchemy. Users can register, log in, log out, and access certain routes only when authenticated.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/0d13feb4-8727-4969-964b-c6ba87ad64fb


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
5. Access the application in your web browser at `http://localhost:5000`.

## Usage

- **Home Page**: Landing page where users can register, log in, or access other routes if already logged in.
- **Register**: Allows users to register by providing their name, email, and password.
- **Login**: Allows users to log in with their email and password.
- **Secrets**: A route accessible only to logged-in users, where they can view their secrets or private information.
- **Logout**: Logs out the current user and redirects to the home page.
- **Download**: Allows logged-in users to download a PDF file.

## Features

- **User Registration**: Users can register by providing their name, email, and password.
- **User Authentication**: Passwords are securely hashed using `generate_password_hash` and compared using `check_password_hash`.
- **Session Management**: Flask-Login manages user sessions and provides login/logout functionality.
- **Restricted Routes**: Certain routes are accessible only to authenticated users using the `@login_required` decorator.
- **Flash Messages**: Flash messages are displayed for registration errors, login errors, and incorrect password attempts.
- **Secure File Download**: Authenticated users can download files from the server.

## Database

The application uses SQLite for the database. The `User` table stores user information such as email, hashed password, and name.
