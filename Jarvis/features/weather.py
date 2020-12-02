import requests
import json


def main_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_key = "9d7cde1f6d07ec55650544be1631307e"
    units_format = "&units=metric"

    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    complete_url = base_url + city + "&appid=" + api_key + units_format

    response = requests.get(complete_url)

    city_weather_data = response.json()

    if city_weather_data["cod"] != "404":
        main_data = city_weather_data["main"]
        weather_description_data = city_weather_data["weather"]
        weather_description = weather_description_data["description"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        wind_data = city_weather_data["wind"]
        wind_speed = wind_data["speed"]

        return (f"The weather in {city} is currently {weather_description} with a temperature of {current_temperature}, atmospheric pressure of {current_pressure}, humidity of {current_humidity} and wind speed reaching {wind_speed} kilometers per hour")

    else:
        return ("Sorry sir, could not find city in my database. Please try again..")