import requests

input_str = input("Put the url here: ")
response = requests.get(url=input_str)
#print(response.headers)
header = {'Accept':'application/json'}
response = requests.get(url=input_str, headers=header)
json_response = response.json()

print(json_response[0]["message"])
