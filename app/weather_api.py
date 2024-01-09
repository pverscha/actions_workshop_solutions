import os
import requests
from config import BASE_URL

def get_current_temperature(city):
    """ Fetches the current temperature for a given city. """

    params = {
        "key": os.environ['WEATHER_API_KEY'],
        "q": city
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data['current']['temp_c']
