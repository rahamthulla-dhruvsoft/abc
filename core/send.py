import requests
headers ={}
#headers['Authorization']='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc1MjgxMTQwLCJqdGkiOiJmOTkxNDAwYjdmN2Q0MGFhOTE5ZDkwYmYzZWQxNjYyNiIsInVzZXJfaWQiOjF9.MYZ5UYWrEU2xBQg0tq0RPql_1dT2iC7nqwgnh8llE34'
#r=requests.get('http://127.0.0.1:8000/hello/',headers=headers)

#print(r.text)
r = requests.post('http://127.0.0.1:8000/api/token/', data={'username': 'abc@dhruvsoft.com', 'password': 'Blackhole@pi1'})
response = r.json()
token = response['access']
print(token)