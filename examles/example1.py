from myweather import MyWeather
import os
import dotenv as dv

APIKEY = os.environ["OPENWEATHERAPI"]
weather = MyWeather()
