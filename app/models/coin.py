from dataclasses import dataclass

@dataclass
class Coin:
    coin_id: str
    name: str
    symbol: str
    current_price: float
    market_cap: int
    market_cap_rank: int
    total_volume: float
    price_change_percentage_24h: float