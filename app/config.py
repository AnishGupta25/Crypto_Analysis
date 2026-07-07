from dotenv import load_dotenv
import os

load_dotenv()

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
BINANCE_BASE_URL = "https://api.binance.com/api/v3"
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")