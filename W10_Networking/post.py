import requests

input_str = input("Put your message here: ")
url = "https://webhook.site/fd8b66ac-5777-456b-8cab-df2174b77d68"
myobj = {"message":input_str}

x = requests.post(url,json=myobj)