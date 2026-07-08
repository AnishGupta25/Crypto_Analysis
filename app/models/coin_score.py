from dataclasses import dataclass
from app.models.coin import Coin

@dataclass
class CoinScore:
    coin: Coin
    market_cap_score: float
    liquidity_score: float
    momentum_score: float
    overall_score: float