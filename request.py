import requests
from config import API_KEY, country_code

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def get_coordinate():
    """return coordinate city"""
    pass


def get_weather_by_city_name(city_name):
    response = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name},'
                                f'RU&appid={API_KEY}')
    return response.json()


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
