import requests
url = "http://localhost:8000/api/leaves/"
'''
resp = requests.post(url,
	json={"desc":"api leave",
		"type":3,
		"user":8,
		"leavedate":"2019-02-23"})
'''
'''
resp=requests.put(url+"8/",json={"desc":"api leave update"})
print(resp)
print(resp.json())
'''
'''
resp=requests.delete(url+"8/")
print(resp)
print(resp.json())
'''

resp = requests.get(url+"7/")
print(resp)
print(resp.json())
