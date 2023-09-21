from _datetime import datetime
import requests
from dotenv import load_dotenv

import os

load_dotenv()
PIXELA_END_POINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("MY_USERNAME")
USER_AUTH_TOKEN = os.environ.get("USER_AUTH_TOKEN")
# # # #Creating a user
user_parameters = {
    "token": "1324rgenmjhko53",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# response = requests.post(url=PIXELA_END_POINT, json=user_parameters)
# print(response.text)

# # # # Creating a Graph
createGraph_END_POINT = f"{PIXELA_END_POINT}/{USERNAME}/graphs"
graph_parameters = {
    "id": "graph0001",
    "name": "Coding Graph",
    "unit": "hour",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": USER_AUTH_TOKEN,
}
# response = requests.post(url=createGraph_END_POINT, json=graph_parameters, headers=headers)
# print(response.text)
# # # # Adding pixel to the graph
updateUser_END_POINT = f"{createGraph_END_POINT}/graph0001"

addData_parameters = {
    # "date": datetime.now().strftime("%Y%m%d"),
    "date": "20230918",
    "quantity": "6",
}
# response = requests.post(url=updateUser_END_POINT, json=addData_parameters, headers=headers)
# print(response.text)

# # # #Updating the users pixel
modifyData_parameters = {
    "quantity": "3"
}
modifyData_END_POINT = f"{updateUser_END_POINT}/20230920"
# response = requests.put(url=modifyData_END_POINT, json=modifyData_parameters, headers=headers)
# print(response.text)

