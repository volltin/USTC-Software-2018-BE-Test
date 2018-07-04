import requests

s = requests.session()

response = s.post("http://127.0.0.1:8000/user/login/", data = {'username':"b",'password':"b"})

print(response)
print(response.headers)
print(response.text)

print(s.cookies)

response = s.get("http://127.0.0.1:8000/user/profile/")

print(response)
print(response.headers)
print(response.text)

response = requests.get("http://127.0.0.1:8000/user/profile/")

print(response)
print(response.headers)
print(response.json())

