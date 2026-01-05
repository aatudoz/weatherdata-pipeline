import requests
import os
from dotenv import load_dotenv

load_dotenv()
#Hiding API Key
api_key = os.getenv("WEATHERSTACK_API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Rovaniemi"

def get_data():
    # Extracting the json data from the Weatherstack API.
    # Fetches all current data from Rovaniemi.
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")    
        raise

#data = get_data()
#print(data)

# Can only call the API 100 times in a month, so we use this mock data to develop the pipeline.
def mock_data():
 return {'request': {'type': 'City', 'query': 'Rovaniemi, Finland', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Rovaniemi', 'country': 'Finland', 'region': 'Lapland', 'lat': '66.500', 'lon': '25.717', 'timezone_id': 'Europe/Helsinki', 'localtime': '2026-01-04 12:04', 'localtime_epoch': 1767528240, 'utc_offset': '2.0'}, 'current': {'observation_time': '10:04 AM', 'temperature': -22, 'weather_code': 260, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0007_fog.png'], 'weather_descriptions': ['Freezing fog'], 'astro': {'sunrise': '10:53 AM', 'sunset': '01:51 PM', 'moonrise': '12:00 AM', 'moonset': '12:00 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 99}, 'air_quality': {'co': '178.85', 'no2': '3.25', 'o3': '49', 'so2': '1.75', 'pm2_5': '3.75', 'pm10': '4.75', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 5, 'wind_degree': 10, 'wind_dir': 'N', 'pressure': 1005, 'precip': 0, 'humidity': 84, 'cloudcover': 0, 'feelslike': -27, 'uv_index': 0, 'visibility': 10, 'is_day': 'yes'}}