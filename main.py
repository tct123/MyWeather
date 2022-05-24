import requests

API_Key = f3cd11432dabdb4ccae3c0a1347c07a1

print("Breitengrad:")
lat = input()
print("Längengrad:")
lon = input()

request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"

response = requests.get(request_url)

if response.status_code == 200:
    data =response.json()
    print(data)
else:
    print("Fehler")