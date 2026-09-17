"""
In this module we are practising the requests module present in Python.
"""

import requests

url = "https://jsonplaceholder.typicode.com/users"

params = {
    "id": 1
}

response = requests.get(url, params=params)

print("We got the status code : ", response.status_code)
print("URL : ", response.url)
print("Content : ", response.content)
print("We got the text : ", response.text)
print("The response.json() returns : ", response.json())
print("Type of the response is : ", type(response))
print("Type of the responses.json() returns ", type(response.json()))
print("Here we are printing entire response obj : \n", response)
