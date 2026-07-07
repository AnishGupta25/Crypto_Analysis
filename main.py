from app.collectors.coingecko import CoinGeckoClient

client = CoinGeckoClient()

coins = client.get_top_coins(10)

for coin in coins:
    print(coin)
