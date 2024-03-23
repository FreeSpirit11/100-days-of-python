from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

google_sheet_link="https://docs.google.com/spreadsheets/d/1yzIhs0E2pvmA-pkL6IpAltEkhwwi_9dGXMAZ1_9Nwk4/edit#gid=1418962850"
user_registration_link="https://replit.com/@MansiYadav14/FLightDeal2#main.py"
print(f"go to this link for user registration {user_registration_link}")

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager=NotificationManager()

ORIGIN_CITY_IATA = "LON"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,

    )
    stop_over_message=""
    ###################

    if flight is None:
        continue

    ##################
    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert !\n Only €{flight.price}😉 to fly from" \
                  f" {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-" \
                  f"{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        ######################
        if flight.stop_overs == 1:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
            
        #############################
        users=data_manager.get_user_data()
        for user in users:
            subject = "Flight Club ✈"
            msg = f"subject:{subject} \n\n{message}"
            encoded_msg=msg.encode("utf-8")
            notification_manager.send_emails(encoded_msg, user['email'])
        #######################

            notification_manager.send_sms(message,user['phone_num'])
            




