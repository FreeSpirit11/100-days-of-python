# Automated Birthday Wisher

The Automated Birthday Wisher is a Python script that automates the process of sending birthday wishes to friends and family via email. It reads birthday information from a CSV file, generates personalized birthday messages using letter templates, and sends them automatically on the recipient's birthday.

https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/c26b62d0-85b3-49fa-aacb-b2b243f4c9ad


## Features

- Automatic Birthday Wishes: The script automatically sends personalized birthday wishes to recipients on their birthday.
- Customizable Letter Templates: You can create different letter templates with placeholders like "[Name]" to personalize the birthday messages.
- CSV Data Input: The birthday information is stored in a CSV file, making it easy to manage and update recipient details.
- Secure Email Configuration: The script uses SMTP (Simple Mail Transfer Protocol) for email communication, and the user's email credentials are stored as environment variables for security.

## How to Use


1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/FreeSpirit11/100-days-of-python.git
   ```

2. Navigate to the directory containing the project files.
   
3. Install the required dependencies.

4. Set up your email and password .

5. Create a CSV file named "birthdays.csv" in the project directory.
   - The CSV file should have columns "name," "email," "month," and "day" for each recipient's name, email, birth month, and birth day, respectively.

6. Customize letter templates in the "letter_templates" folder.
   - Create different letter templates with placeholders like "[Name]" to personalize the birthday messages.

7. Run the main script to send birthday wishes:
   ```shell
   python main.py
   ```
   
8. The script will automatically send birthday wishes to recipients whose birthday matches the current date.

**Note:** Make sure to keep your email and password information safe and secure. Storing them as environment variables ensures that sensitive information is not exposed in your code.

## File Structure

```
automated-birthday-wisher/
  ├── letter_templates/
  |   ├── letter_1.txt
  |   ├── letter_2.txt
  |   ├── letter_3.txt
  |   ├── ...
  ├── birthdays.csv
  ├── main.py
  └── README.md
```

## Acknowledgement

This project is a part of the "100 Days of Code" challenge by Angela Yu

## Author

- [Mansi Yadav](https://github.com/FreeSpirit11)

Feel free to fork, contribute, and use the Automated Birthday Wisher for your personal use. 

Happy birthday wishing! 
