import requests

response = requests.post("http://127.0.0.1:8000/user/register/", data = {'username':"b",'password':"b"})
print(response)
print(response.json())