import httpx
from app.models.coin import Coin
from app.providers.coin_provider import CoinProvider
from app.config import Binance_BASE_URL

class BinanceClient(CoinProvider):
    def __init__(self):
        self.base_url = Binance_BASE_URL

    def get_top_coins(self, limit=100):
        url = f"{self.base_url}/ticker/24hr"

        response = httpx.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        coins = []

        for ticker in data[:limit]:
            coins.append(
                Coin(
                    coin_id=ticker["symbol"],
                    name=ticker["symbol"],
                    symbol=ticker["symbol"].replace("USDT", "").lower(),
                    current_price=float(ticker["lastPrice"]),
                    market_cap=None,
                    market_cap_rank=None,
                    total_volume=float(ticker["quoteVolume"]),
                    price_change_percentage_24h=float(ticker["priceChangePercent"])
                )
            )

        return coins