import requests
from Jarvis.config import config



def fetch_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_key = config.weather_api_key
    units_format = "&units=metric"

    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    complete_url = base_url + city + "&appid=" + api_key + units_format

    response = requests.get(complete_url)

    city_weather_data = response.json()

    if city_weather_data["cod"] != "404":
        main_data = city_weather_data["main"]
        weather_description_data = city_weather_data["weather"][0]
        weather_description = weather_description_data["description"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        wind_data = city_weather_data["wind"]
        wind_speed = wind_data["speed"]

        final_response = f"""
        The weather in {city} is currently {weather_description} 
        with a temperature of {current_temperature} degree celcius, 
        atmospheric pressure of {current_pressure} hectoPascals, 
        humidity of {current_humidity} percent 
        and wind speed reaching {wind_speed} kilometers per hour"""

        return final_response

    else:
        return "Sorry Sir, I couldn't find the city in my database. Please try again"