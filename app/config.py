from dotenv import load_dotenv
import os

load_dotenv()

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
Binance_BASE_URL = "https://api.binance.com/api/v3"
Binance_API_KEY = os.getenv("Binance_API_KEY")