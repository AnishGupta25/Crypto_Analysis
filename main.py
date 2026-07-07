from app.collectors.coingecko import CoinGeckoClient
from app.collectors.binance import BinanceClient
from app.services.coin_service import CoinService
from app.clients.base_api_client import BaseAPIClient
from app.config import COINGECKO_BASE_URL,BINANCE_BASE_URL

http_client = BaseAPIClient(BINANCE_BASE_URL)
provider = BinanceClient(http_client)
service = CoinService(provider)
coins = service.get_top_coins(10)

for coin in coins:
    print(coin)
    print("\n")