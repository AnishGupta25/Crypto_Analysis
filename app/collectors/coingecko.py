from app.clients.base_api_client import BaseAPIClient
from app.config import COINGECKO_BASE_URL
from app.models.coin import Coin
from app.providers.coin_provider import CoinProvider

class CoinGeckoClient(CoinProvider):

    def __init__(self, http_client: BaseAPIClient):
        self.http = BaseAPIClient(COINGECKO_BASE_URL)

    def get_top_coins(self, limit=100):

        params = {
            "vs_currency": "inr",
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": False
        }

        data = self.http.get(
            "/coins/markets",
            params=params
        )

        coins = []

        for item in data:

            coins.append(
                Coin(
                    coin_id=item["id"],
                    name=item["name"],
                    symbol=item["symbol"],
                    current_price=item["current_price"],
                    market_cap=item["market_cap"],
                    market_cap_rank=item["market_cap_rank"],
                    total_volume=item["total_volume"],
                    price_change_percentage_24h=item["price_change_percentage_24h"]
                )
            )

        return coins
