from app.models.coin import Coin
from app.scorers.base_scorer import BaseScorer

class LiquidityScorer(BaseScorer):
    def score(self, coin: Coin):
        volume = coin.total_volume
        if volume is None:
            return 0.0
        if volume > 1_000_000_000:
            return 100.0
        elif volume > 100_000_000:
            return 75.0
        elif volume > 10_000_000:
            return 50.0
        elif volume > 1_000_000:
            return 25.0
        else:
            return 0.0