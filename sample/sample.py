import getweather as gw
import message as msg

API_KEY = ''  # sign up at https://openweathermap.org/ to get an API key
city_name = 'London'
country_code = 'GB'

# cnt parameter in base_url specifies how many 3-hour periods to retrieve data for. 16 ensures 2 full days worth of data.
# the parse_weather func in getweather trims down the retrieved periods to only the 8 for the following day.
# therefore the program can run at any time of day and only will keep data on tomorrow's weather
base_url = f'http://api.openweathermap.org/data/2.5/forecast/?q={city_name},{country_code}&appid={API_KEY}&mode=JSON&cnt=16&units=metric'


def main():
    weather_data_raw = gw.request_weather(base_url)
    parsed_weather = gw.parse_weather(weather_data_raw)
    weather_message = msg.make_message(parsed_weather)
    msg.send_message(message=weather_message)

if __name__ == '__main__':
    main()
