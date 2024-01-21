import requests
import json

API_Key = "f3cd11432dabdb4ccae3c0a1347c07a1"

print("Breitengrad:")
lat = input()
print("Längengrad:")
lon = input()

request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"

response = requests.get(request_url)


data =response.json()
#print(data)
weather_describtion = data["weather"][0]["description"]
print(weather_describtion)
setgraddegree = "Grad"
if setgraddegree == "Grad":
    temperature = round(data["main"]["temp"]-273.15)
if setgraddegree == "Fahrenheit":
    temperature = round(data["main"]["temp"])
print(temperature)