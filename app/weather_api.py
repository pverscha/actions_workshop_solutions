import os
import random
import requests
from config import BASE_URL

def get_current_temperature(city):
    """ Fetches the current temperature for a given city. """

    API_KEY = os.environ.get('WEATHER_API_KEY')

    # If the key did not exist, we will return a random temperature value (that can be used to test this script)
    if not API_KEY:
        print("No API key found, returning random temperature value.")
        return random.randint(-10, 40)

    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data['current']['temp_c']
