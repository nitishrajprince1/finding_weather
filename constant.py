from dotenv import load_dotenv
import os


load_dotenv()
WEATHER_API_KEY = os.getenv('API_KEY', '')
