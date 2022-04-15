import requests
from config import API_KEY, country_code, headers


def get_geolocation_by_city_name(city_name):
    response = requests.get(url=f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&'
                                f'limit=10&appid={API_KEY}&lang=ru')
    cities = {}
    count = 0
    for i in response.json():
        cities[count] = {}
        cities[count]['name'] = i['name']
        cities[count]['lat'] = i['lat']
        cities[count]['lon'] = i['lon']
        cities[count]['country'] = i['country']
        cities[count]['state'] = i['state']
        count += 1

    return cities


def get_weather_by_geolocation_openweather(lat, lon):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&'
        f'appid={API_KEY}&units=metric')
    return response.json()


def get_weather_by_geolocation_yandex(lat, lon):
    response = requests.get(f'https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}&[lang=ru_RU]',
                            headers=headers, verify=True)
    return response.json()
