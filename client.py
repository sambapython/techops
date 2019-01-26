import requests
resp=requests.get("http://localhost:8000/customers/")
print(resp.json())