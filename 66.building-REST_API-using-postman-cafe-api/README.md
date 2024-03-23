# Cafe API with Flask

This Flask API allows users to interact with a database of cafes. Users can perform operations such as retrieving a random cafe, searching for cafes by location, adding new cafes, updating coffee prices, and deleting cafes.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/25cd0a63-3b4b-4f55-8611-bd54a5bc3397


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
5. Access the API endpoints using an HTTP client such as Postman or cURL.

## Usage

### Endpoints

- **GET /random**: Retrieve a random cafe from the database.
- **GET /all**: Retrieve all cafes from the database.
- **GET /search**: Search for cafes by location.
  - Parameters: loc (location)
- **POST /add**: Add a new cafe to the database.
  - Parameters: name, map_url, img_url, location, sockets, toilet, wifi, calls, seats, coffee_price
- **PATCH /update-price/<cafe_id>**: Update the coffee price of a cafe.
  - Parameters: coffe_price
- **DELETE /report-closed/<cafe_id>**: Delete a cafe from the database.
  - Parameters: api_key

## Database Schema

The database contains a single table `Cafe` with the following fields:
- id: Integer (Primary Key)
- name: String
- map_url: String
- img_url: String
- location: String
- seats: String
- has_toilet: Boolean
- has_wifi: Boolean
- has_sockets: Boolean
- can_take_calls: Boolean
- coffee_price: String

## Error Handling

The API handles various HTTP error codes such as 404 (Not Found) and 403 (Forbidden) for invalid requests or unauthorized access.

## Security

The `/report-closed` endpoint requires an `api_key` parameter to prevent unauthorized deletion of cafes.

## Credits

This project is inspired by the Flask tutorial series by Angela Yu on Udemy.
