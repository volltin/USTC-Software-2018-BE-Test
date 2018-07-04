import requests

response = requests.post("http://127.0.0.1:8000/user/login/", data = {'username':"b",'password':"b","login_time":1})

print(response)
print(response.headers)
print(response.text)

#response = requests.post("http://127.0.0.1:8000/user/login/", data = {'username':"b",'password':"c"})

#print(response)
#print(response.text)


