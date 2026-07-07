from app.providers.coin_provider import CoinProvider

class CoinService:

    def __init__(self, provider: CoinProvider):
        self.provider = provider

    def get_top_coins(self, limit=100):

        coins = self.provider.get_top_coins(limit)

        return [
            coin
            for coin in coins
            if coin.symbol not in {"usdt", "usdc", "dai"}
        ]
