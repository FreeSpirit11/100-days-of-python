import requests
from datetime import datetime

USERNAME="mansi126"
TOKEN="fiji3453tfbfdbd"
GRAPH_ID="graph1"
pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{graph_endpoint}/{GRAPH_ID}"

today=datetime.now()

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many km did you cycle today? ")
}

response=requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_update_date=pixel_data["date"]
pixel_update_endpoint=f"{pixel_creation_endpoint}/{pixel_update_date}"
new_pixel_data={
    "quantity":"5",
}

# response=requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

pixel_delete_date=20230519
pixel_delete_endpoint=f"{pixel_creation_endpoint}/{pixel_delete_date}"

# response=requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)

'''
Navigate to this site to see you pixela graph ->
https://pixe.la/v1/users/mansi126/graphs/graph1
'''
