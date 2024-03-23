# Movie Collection Flask App

This Flask application allows users to manage a collection of movies, including adding, editing, rating, and deleting entries. It utilizes SQLAlchemy for database management and integrates with The Movie Database (TMDb) API to fetch movie details.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/353f122b-f9a9-494d-9f9a-3e5e5e105c43


## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python and pip installed on your system.
3. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
4. Obtain an API key from [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api) and replace  `MOVIE_DB_API_KEY` variable with your API key.
5. Run the application:
    ```
    python main.py
    ```
6. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage

- **Home Page**: View all movies in the collection with their titles, release years, descriptions, and ratings. Movies are sorted by rating.
- **Rate Movie**: Add or update the rating and review of a movie.
- **Add Movie**: Search for a movie title using The Movie Database (TMDb) API and add it to the collection.
- **Delete Movie**: Remove a movie from the collection.

## File Structure

- `main.py`: Contains the Flask application code including routes, database setup, and API integration.
- `templates/`: Directory containing HTML templates for rendering pages.
- `static/`: Directory for static files such as CSS stylesheets or client-side scripts.
- `instance/movies-collection.db`: SQLite database file storing movie data.

## Dependencies

- Flask: Micro web framework for Python.
- Flask SQLAlchemy: Flask extension for working with SQLAlchemy database.
- Flask WTF: Flask extension for form handling.
- Flask Bootstrap: Flask extension for integrating Bootstrap.
- WTForms: Library for building web forms in Flask applications.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- Bootstrap: Front-end framework for designing responsive and mobile-first websites.
- Requests: HTTP library for making API requests.

## Credits

This project is inspired by the Flask tutorial series by Angela Yu on Udemy.
