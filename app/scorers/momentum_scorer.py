from app.models.coin import Coin
from app.scorers.base_scorer import BaseScorer

class MomentumScorer(BaseScorer):
    def score(self, coin: Coin):
        price_change = coin.price_change_percentage_24h

        if price_change is None:
            return 0.0

        if price_change > 20:
            return 100.0

        if price_change > 10:
            return 50.0

        if price_change > 0:
            return 25.0

        if price_change > -20:
            return 10.0
        
        return 0.0