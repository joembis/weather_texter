import requests
from datetime import datetime as dt
from datetime import timedelta


def request_weather(url):
    """request the weather from openweathermap.org API. Returns a dict of the json file"""
    response = requests.get(url)
    response_dict = response.json()
    return response_dict


def parse_weather(weather_data_raw):
    """parse the useful weather data from dict of the openweathermap.org json data.
    returns another, slimmed down dict with the chosen elements"""

    parsed_weather = {}
    parsed_weather['sunrise'] = dt.fromtimestamp(weather_data_raw.get("city").get("sunrise")).time()
    parsed_weather['sunset'] = dt.fromtimestamp(weather_data_raw.get("city").get("sunset")).time()


    for period in weather_data_raw['list']:
        # limiting the parsed weather data to weather for the next day
        if dt.fromtimestamp(period.get("dt")).date() == dt.today().date() + timedelta(days=1):
            time_period = dt.fromtimestamp(period.get("dt"))
           #  the dict key for each period is a 2-dight 24-hour time, e.g 15 for 3.00pm
            parsed_weather[str(time_period.time())[:2]] = [
                str(time_period.time())[:2],
                round(period.get("main").get("temp")),
                period.get("weather")[0].get("main").center(15),
                str(period.get("clouds").get("all")).zfill(3),
                str(round(period.get("wind").get("speed"))).zfill(3)
            ]
    return parsed_weather
