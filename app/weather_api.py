import os
import random
import requests
from config import BASE_URL

def get_current_temperature(city):
    """ 
    Fetches the current temperature for a given city from the WeatherAPI service. 
    
    WeatherAPI requires a valid API key in order to properly function. This key will be read from an environment
    variable with the name WEATHER_API_KEY. If this variable does not exist, a random temperature value will be returned
    instead.

    Parameters:
        city (str): The city to fetch the temperature for.

    Returns:
        A number representing the current temperature in degrees Celsius.
    """

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
