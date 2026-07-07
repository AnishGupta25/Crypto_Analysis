from app.collectors.coingecko import CoinGeckoClient
from app.services.coin_service import CoinService

provider = CoinGeckoClient()
service = CoinService(provider)
coins = service.get_top_coins(10)

for coin in coins:
    print(coin)
    print("\n")
    #print(f"{coin.name} ({coin.symbol}): {coin.current_price} INR")