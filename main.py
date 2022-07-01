from API import BOT_TOKEN
from API2 import API_TOKEN
from telebot import types
import requests, telebot

bot = telebot.TeleBot(BOT_TOKEN)

def get_forecast(city, message):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_TOKEN,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    a = response.json()
    try:
        main_weather = a['weather'][0]['main']
        weather_desc = a['weather'][0]['description']
        temp = a['main']['temp']
        tempreal = a['main']['feels_like']
        windspeed = a['wind']['speed']

        st = 'The weather in ' + city + ' is: ' + main_weather + ', ' + weather_desc.capitalize() + '\n'
        st += 'The temperature is: ' + str(temp) + '\n'
        st += 'But feels like: ' + str(tempreal) + '\n'
        st += 'The wind speed is: ' + str(windspeed)
        bot.send_message(message.chat.id, st)
    except:
        bot.send_message(message.chat.id, "Sorry, but there is no weather forecast for this city! Please check your message and try again.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi! Send me the name of your city and I will send you the weather forecast!')

@bot.message_handler(content_types=['text'])
def get_city(message):
    city = message.text
    get_forecast(city, message)

bot.polling(none_stop=True)