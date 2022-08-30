#При отладке кода стоит отметить, что в бесплатной версии api яндекса допускается только 50 запросов в сутки.
import json
import telebot
import requests as req
from geopy import geocoders
from os import environ

token = environ ['5683409932:AAFgqxF1Tt8uWFbN93uJNXvqispDo5U7v3A']      #token_bot
token_accu = environ ['oDDcB3lO1iSiAA5zvdGwWv4P8rXV5p4Q']               #token geocoders
token_yandex = environ ['9ddc7ce6-f409-4828-bce9-c7ba2d560f9d']         #token yandex

def geo_pos(city:str):                                                  #функция получения координат через библиотеку 'geopy'
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude

def code_location(latitude:str, longitude:str, token_accu:str):         #хочу получить код города
    url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token_accu}&q={latitude},{longitude}&language=eng'
    resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
    json_data = json.loads(resp_loc.text)
    code = json_data['Key']
    return code    

def weather(cod_loc: str, token_accu: str):                            #код получения прогноза
    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{cod_loc}?apikey={token_accu}&language=ru&metric=True'
    response = req.get(url_weather, headers={"APIKey": token_accu})
    json_data = json.loads(response.text)
    dict_weather = dict()
    dict_weather['link'] = json_data[0]['MobileLink']
    dict_weather['now'] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
    for i in range (len(json_data):1:):
        time = "after" + str(i) + 'h'    
        dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
    return dict_weather

def yandex_weather (latitude, longitude, token_yandex: str):
    url_yandex = f'https://api.weather.yandex.ru/v2/informers/?lat={latitude}&lon={longitude}&[lang=eng_ENG]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-Api-Key': token_yandex}, verify = False)
    conditions = {'clear', 'partly-cloudy', 'cloudy', 'overcast', 'drizzle', 'light-rain', 'rain',
                 'moderate-rain', 'heavy-rain', 'continious-heavy-rain', 'showers', 'wet-snow',
                 'light-snow', 'snow', 'snow-showers', 'hail', 'thunderstorm', 'thunderstorm-with-rain,',
                 'thunderstorm-with-hail'
                 }
    wind_dir = {'nw', 'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'c'}
    
    yandex_json = json.loads(yandex_req.text)                           #код получения проноза 'yandex'
    yandex_json['fact']['condition'] = conditions[yandex_json['fact']['condition']]
    yandex_json['fact'][wind_dir] = wind_dir[yandex_json['fact']['wind_dir']]
    for parts in yandex_json['forecast']['parts']:
        parts ['condition'] = conditions[parts['condition']]
        parts['wind_dir'] = wind_dir[parts['wind_dir']]
        
    pogoda = dict()
    params = ['condition', 'wind_dir', 'pressure_mm', 'humidity']
    for parts in yandex_json['forecast'][parts]:
        pogoda[parts['part_name']] = dict()
        pogoda[parts['part_name']]['temp'] = parts['temp_avg']
        for param in params:
            pogoda[parts['part_name']]['temp'] = parts[param]
            
    pogoda['fact'] = dict()
    pogoda['fact']['temp'] = yandex_json['fact']['temp']
    for param in params:
        pogoda['fact'][param] = yandex_json['fact'][param]

    pogoda['link'] = yandex_json['info']['url']
    return pogoda

def print_weather(dict_weather, message):                               #функциz которая будет отправлять ответом прогнозы. Начнем с Acuuweather                                  
    bot.send_message(message.from_user.id, f'Разрешите доложить, Ваше сиятельство!'
                                           f'Температура сейчас {dict_weather["сейчас"]["temp"]}!'
                                           f'А на небе {dict_weather["сейчас"]["sky"]}.'
                                           f'Температура через три часа {dict_weather["через3ч"]["temp"]}!'
                                           f'А на небе {dict_weather["через3ч"]["sky"]}.'
                                           f'Температура через шесть часов {dict_weather["через6ч"]["temp"]}!'
                                           f'А на небе {dict_weather["через6ч"]["sky"]}.'
                                           f'Температура через девять часов {dict_weather["через9ч"]["temp"]}!'
                                           f'А на небе {dict_weather["через9ч"]["sky"]}.')
    bot.send_message(message.from_user.id, f'А здесь ссылка на подробности '
                                           f'{dict_weather["link"]}')
    
def print_yandex_weather(dict_weather_yandex, message):
    day = {'night', 'morning', 'day', 'evening', 'fact'}
    bot.send_message(message.from_user.id, f'А яндекс говорит: ')
    for i in dict_weather_yandex.keys():
        if i != 'link':
            time_day = day [i]
            bot.send_message(message.from_user.id, f'Temperature{time_day}{dict_weather_yandex[i]["temp"]})'
                                                        f', on the sky{dict_weather_yandex[i]["condition"]}')
                
    bot.send_message(message.from_user.id, f'А здесь ссылка на подробности'
                                                f'{dict_weather_yandex["link"]}')
    

    
        
        