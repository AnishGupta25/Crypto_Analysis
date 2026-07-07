from app.clients.base_api_client import BaseAPIClient
from app.config import BINANCE_BASE_URL
from app.models.coin import Coin
from app.providers.coin_provider import CoinProvider

class BinanceClient(CoinProvider):

    def __init__(self, http_client: BaseAPIClient):
        self.http = http_client

    def get_top_coins(self, limit=100):

        data = self.http.get("/ticker/24hr")

        coins = []

        for ticker in data:

            if not ticker["symbol"].endswith("USDT"):
                continue

            symbol = ticker["symbol"].replace("USDT", "").lower()

            coins.append(
                Coin(
                    coin_id=symbol,
                    name=symbol.upper(),
                    symbol=symbol,
                    current_price=float(ticker["lastPrice"]),
                    market_cap=None,
                    market_cap_rank=None,
                    total_volume=float(ticker["quoteVolume"]),
                    price_change_percentage_24h=float(ticker["priceChangePercent"])
                )
            )

            if len(coins) >= limit:
                break

        return coins