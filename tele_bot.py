from aiogram.types import message
from aiogram.types.message import Message
from config import tg_bot_token, open_weather_token
import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hi,Write me name of city and I will send you a weather ")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
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

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f"Weather in the city: {city}\nTempriture: {cur_weather}C°\n"
        f"Humidity: {humidity}%\nPressure: {pressure}\nWind: {wind}\n"
        f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of the day: {length_of_the_day}\n"
        f"Have a good day!")
    except:
        await message.reply('Check name of city')

    


if __name__=='__main__':
    executor.start_polling(dp)

