import requests

response = requests.get('https://api.github.com')
print("status Code:", response.status_code)