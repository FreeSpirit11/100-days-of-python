##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import random
import pandas
import datetime as dt

my_email="my697253@gmail.com"
password="xxfrwtezcpgvqgls"

df=pandas.read_csv("birthdays.csv")
birthday_info={row["name"]:{"email": row.email, "month":row.month, "day": row.day} for (index, row) in df.iterrows()}

now = dt.datetime.now()
for (bday_name, bday_dates) in birthday_info.items():
    if bday_dates["month"]==now.month and bday_dates["day"]==now.day :
        file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as birthday_letter:
            msg=birthday_letter.read()
            birthday_msg=msg.replace("[Name]", bday_name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=bday_dates["email"],
                                msg=f"subject:Happy Birthday! \n\n{birthday_msg}")


#imp notes Yes, that's correct! In `pandas`, the `name` attribute of a Series object (which represents a row or a column
# in a DataFrame) returns the label of the Series. When you use `row.name` to access a value in a row of a DataFrame,
# `pandas` actually returns the label of the row, not the value in the `name` column.

#To access the value in a specific column for each row in a `pandas` DataFrame, you should use square brackets and the
# column name as a string, like this: `row['column_name']`. In your case, to access the value in the `name` column for
# each row, you should use `row['name']`.
#Therefore, it’s recommended to always use square brackets and the column name as a string to access the values in a
# specific column for each row in a pandas DataFrame.

