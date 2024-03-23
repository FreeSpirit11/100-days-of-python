# Flask Cafe Finder

This project is a Flask application that allows users to add and view cafes. Users can submit details about cafes, such as their name, location, opening and closing times, and ratings for coffee quality, wifi strength, and power socket availability.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FreeSpirit11.git
   ```

2. Navigate to the project directory:

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python main.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Features

- **Add Cafe**: Users can add new cafes along with their details.
- **View Cafes**: Users can view a list of all cafes submitted.
- **Cafe Ratings**: Users can rate cafes based on coffee quality, wifi strength, and power socket availability.
- **CSV Storage**: Cafe data is stored in a CSV file for easy retrieval and persistence.

## File Structure

- `main.py`: Main Flask application file containing routes and form handling.
- `templates/`: Directory containing HTML templates for different pages.
- `cafe-data.csv`: CSV file to store cafe data.
- `requirements.txt`: File listing all required Python packages.

## Acknowledgements

This project is a part of #100daysofcode by Angela Yu on udemy.
