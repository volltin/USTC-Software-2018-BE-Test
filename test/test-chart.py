import requests
import json

numbers = [1,2,3,4,6,1,4,5]
data = {"number":json.dumps(numbers)}
response = requests.post("http://127.0.0.1:8000/chart/simple/",data=data)

print(response)

with open("tmp.png","wb") as f:
    f.write(response.content)