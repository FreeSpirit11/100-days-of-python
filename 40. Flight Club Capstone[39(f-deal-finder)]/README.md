# FlightClub ✈️

FlightClub is a Python application that helps users find the best flight deals and notifies them via email and SMS when there are low-price alerts for their desired destinations.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/2baf2fd4-1b2b-4eb1-96e4-7b450c1a9389


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [How the Project Works](#how-the-project-works)
- [File Structure](#file-structure)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

## Introduction

Welcome to FlightClub, the ultimate flight deal finder! This project aims to simplify the process of finding affordable flight tickets to various destinations. Users can register and specify their preferred destinations, and FlightClub will monitor flight prices to notify them when a low-price alert is available for their selected destinations.

## Features

1. Error Handling for a smooth user experience.
2. Seamless User Registration process.
3. Smart Destination Suggestions for quick selection.
4. Low Price Alerts for the best flight deals.
5. Multiple Notification Services (email, SMS).
6. Interactive Command-Line Interface for user-friendliness.
7. Fast and Reliable Flight Data from real-time APIs.
8. User-Centric Approach prioritizing needs and budget.

## Requirements

- Python 3.x
- Required Python modules: requests, twilio

## Getting Started

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/FreeSpirit11/100-days-of-python.git
   ```

2. Navigate to the directory containing the project files.

3. Register for an API key from Kiwi Tequila API and Twilio API, and replace `YOUR_API_KEY` and `YOUR_TWILIO_ACCOUNT_SID` and `YOUR_TWILIO_AUTH_TOKEN` in the `flight_search.py` and `notification_manager.py` files, respectively.

4. Register for a Sheety API Bearer Token and replace `YOUR_API_BEARER_SHEETY` in the `data_manager.py` and `sheety.py` files.

5. Update `YOUR_SHEETY_PRICES_ENDPOINT` and `YOUR_SHEETY_USERS_ENDPOINT` in the `data_manager.py` file with the Sheety API endpoints for prices and users.

## Usage

1. Run the `input_main.py` script to register as a user. Provide your first name, last name, email, and mobile number. Make sure to verify your email before proceeding.

2. Add your preferred destinations using the registration link provided during the user registration process.

3. Run the `main.py` script to check for low-price flight deals to your preferred destinations.

4. FlightClub will monitor flight prices and notify you via email and SMS if there are any deals within your specified price thresholds.

## How the Project Works

FlightClub uses the Kiwi Tequila API to search for flight deals and the Twilio API to send email and SMS alerts to registered users. The project uses the Sheety API to store user and destination data in Google Sheets for easy access and management.

When a user registers, their information is stored in the Google Sheets "users" sheet. Users can also specify their preferred destinations, and FlightClub will use the Tequila API to get the IATA codes for those destinations and store them in the Google Sheets "prices" sheet.

The `main.py` script then checks for flight deals from the user's origin city (LON by default) to the registered destination cities. If any low-price deals are found, FlightClub sends email and SMS alerts to the registered users.

## File Structure

The project file structure is organized as follows:

```
FlightClub/
|-- data_manager.py
|-- flight_data.py
|-- flight_search.py
|-- input_main.py
|-- main.py
|-- notification_manager.py
|-- sheety.py
|-- README.md
```
- `data_manager.py`: Handles data retrieval and updates from Google Sheets using the Sheety API.
- `flight_data.py`: Defines the FlightData class to store flight details retrieved from the flight search API.
- `flight_search.py`: Implements the FlightSearch class to search for the best flight deals using the Kiwi Tequila API.
- `input_main.py`: Accepts user input for registration and destination preferences.
- `main.py`: The main script that orchestrates the flight search and notification processes.
- `notification_manager.py`: Manages sending email and SMS notifications to users for low-price flight alerts.
- `sheety.py`: Communicates with the Sheety API to post new user registrations to the Google Sheet.
- `README.md`: The documentation you are currently reading, providing an overview of FlightClub and its functionalities.
  
## Acknowledgements

FlightClub was made possible by the Kiwi Tequila API, Twilio API, and Sheety API. Special thanks to the creators and maintainers of these tools.

This project is a part of #100daysofcode by Angela Yu on udemy.

## Author

FlightClub was created by [Mansi Yadav](https://github.com/FreeSpirit11).

---
Discover unbeatable flight deals to your dream destinations and jet off on incredible adventures without breaking the bank. Let FlightClub be your travel companion and unlock a world of exciting possibilities at unbeatable prices.
