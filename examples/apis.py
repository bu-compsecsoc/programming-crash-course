import requests

r = requests.get("https://api.ipify.org?format=json")
data = r.json()
ip = data["ip"]
print("Your IP is", ip)
