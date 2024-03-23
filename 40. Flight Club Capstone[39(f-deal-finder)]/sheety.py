# import requests
# import os
#
# BEARER = os.environ["API_Bearer_Sheety"]
# USERNAME = os.environ["API_Username_Sheety"]
#
# PROJECT="copyOfFlightDeals"
# SHEET="users"
#
# base_url = "https://api.sheety.co"
#
# def post_new_row(first_name,last_name,email,phone_num):
#   headers={
#     "Authorization": f"Bearer {BEARER}",
#     "Content-Type": "application/json"
#   }
#   url = f"{base_url}/{USERNAME}/{PROJECT}/{SHEET}"
#   body={
#     "user":{
#       "firstName":first_name,
#       "lastName":last_name,
#       "email":email,
#       "phone no.":phone_num
#     }
#   }
#   response=requests.post(url,
#                          headers=headers,
#                          json=body)
#   response.raise_for_status()
