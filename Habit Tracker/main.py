import requests
from datetime import datetime

pixela_endpoint="https://pixe.la/v1/users" 

Username="yp5367"
Token="q2w3e4r5t6y7u8i9o0p"
Graph_ID="yash1805"

user_parameters={
    "token":Token,
    "username":Username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
response=requests.post(url=pixela_endpoint,json=user_parameters)
print(response.text)

graph_endpoint=f"{pixela_endpoint}/{Username}/graphs"

graph_parameters={
    "id":"yash1805",
    "name":"Marathon Practice Tracker",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":Token
}
'''
graph_response=requests.post(url=graph_endpoint,json=graph_parameters,headers=headers) #headers is directly isn't showed up as it is karwgs and not arwgs
print(graph_response.text)
'''
today=datetime(year=2025,month=8,day=28)
print(today.strftime("%Y-%m-%d"))


post_pixel_endpoint=f"https://pixe.la/v1/users/{Username}/graphs/{Graph_ID}"

post_pixel_parameters={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kilometers did you run today? ")
}   
pixel_response=requests.post(url=post_pixel_endpoint,json=post_pixel_parameters,headers=headers)
print(pixel_response.text)

update_yesterday_endpoint=f"https://pixe.la/v1/users/{Username}/graphs/{Graph_ID}/20250828"
update_parameters={
    "quantity":"5.8",
}
update_response=requests.put(url=update_yesterday_endpoint,json=update_parameters,headers=headers)
print(update_response.text)
