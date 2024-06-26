# Automatic Job Application LinkedIn

Automate job applications on LinkedIn using Selenium. This Python script signs in, searches for jobs, and applies for them, simplifying the job hunting process.

https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/570c7a69-1729-48cc-a1b7-98546c38d288

## Getting Started

Follow these steps to set up and run the script on your machine.

### Prerequisites

Make sure you have the following installed:

- Python
- Selenium
- Chrome WebDriver (Ensure it matches your Chrome browser version)
- Chrome Browser

You can install Selenium using pip:

```bash
pip install selenium
```

### Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing the project files.
3. Modify the following variables in the script to match your LinkedIn credentials and job preferences:

    - `USERNAME`: Your LinkedIn email or username.
    - `PASSWORD`: Your LinkedIn password.
    - `DESIRED_JOB`: The type of job you're looking for.

4. Run the script:

```bash
python  main.py
```

5. Manually solve any CAPTCHA that might appear during the process.

6. The script will open LinkedIn, sign in, search for jobs, and apply for easy-to-apply positions.

7. Monitor the script's progress and take actions as necessary.

### Notes

- This script is designed to automate LinkedIn job applications, but it currently saves jobs without applying. You can modify it to apply for jobs by clicking the "Apply" button if needed.
- The decision to save jobs instead of applying is based on the preference of the author to avoid unintended job applications from their LinkedIn account.
- This script may not work for all job listings, especially if the website structure changes. Please use it responsibly.

## Acknowledgments

- Selenium: [https://pypi.org/project/selenium/](https://pypi.org/project/selenium/)
- LinkedIn: [https://www.linkedin.com](https://www.linkedin.com)
- This project is a part of the "100 Days of Code" challenge by Angela Yu.


## Author
- [Mansi Yadav](https://github.com/FreeSpirit11/automatic-job-application-linkedn)
