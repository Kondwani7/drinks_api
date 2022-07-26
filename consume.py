#used to consume operations in our API
import requests
response = requests.get('http://localhost:8000/server/')
print(response.json())