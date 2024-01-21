import requests
import json

# API_Key = "f3cd11432dabdb4ccae3c0a1347c07a1"
#
# print("Breitengrad:")
# lat = input()
# print("Längengrad:")
# lon = input()


class MyWeather:
    def __init__(self, api_key, lat, lon, setgraddegree):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.setgraddegree = setgraddegree
        self.request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}"
        self.response = self.requests.get(self.request_url)
        self.data = self.response.json()
        # print(data)

    def description(self):
        weather_describtion = self.data["weather"][0]["description"]
        return weather_describtion

    def degreefunc(self):
        if self.setgraddegree == "Grad":
            temperature = round(self.data["main"]["temp"] - 273.15)
        if self.setgraddegree == "Fahrenheit":
            temperature = round(self.data["main"]["temp"])
        return temperature
