from app.models.coin import Coin
from app.utils.math_operations import clamp_score
from app.scorers.base_scorer import BaseScorer

class MarketCapScorer(BaseScorer):
    def score(self, coin: Coin):
        rank = coin.market_cap_rank
        if rank is None or rank < 1:
            return 0.0
        
        return clamp_score(101 - rank)