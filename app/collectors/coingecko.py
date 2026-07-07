import httpx
from app.config import COINGECKO_BASE_URL
from app.models.coin import Coin

class CoinGeckoClient:

    def __init__(self):
        self.base_url = COINGECKO_BASE_URL

    def get_top_coins(self, limit=100):

        url = f"{self.base_url}/coins/markets"

        params = {
            "vs_currency": "inr",
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": False
        }

        response = httpx.get(url, params=params, timeout=30)

        response.raise_for_status()

        data =  response.json()

        coins = []

        for coin in data:
            coins.append(
                Coin(
                    coin_id=coin["id"],
                    name=coin["name"],
                    symbol=coin["symbol"],
                    current_price=coin["current_price"],
                    market_cap=coin["market_cap"],
                    market_cap_rank=coin["market_cap_rank"],
                    total_volume=coin["total_volume"],
                    price_change_percentage_24h=coin["price_change_percentage_24h"]
                )
            )

        return coins
