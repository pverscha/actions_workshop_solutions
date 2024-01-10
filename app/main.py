import sys
from weather_api import get_current_temperature

def main():
    city = sys.argv[1]
    try:
        temperature = get_current_temperature(city)
        print(f"The current temperature in {city} is: {temperature}°C")
    except Exception as e:
        print("Error occurred:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
