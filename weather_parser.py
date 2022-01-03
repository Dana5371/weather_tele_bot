from config import open_weather_token
import requests
from pprint import pprint
import datetime

def get_weather(city, open_weahter_token):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
            )
        data = r.json()
        # pprint(data)


        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f"Weather in the city: {city}\nTempriture: {cur_weather}C°\n"
        f"Humidity: {humidity}%\nPressure: {pressure}\nWind: {wind}\n"
        f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of the day: {length_of_the_day}\n"
        f"Have a good day!")
    except Exception as ex:
        print(ex)
        print('Check name of city')


def main():
    city = input("Enter a city: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()