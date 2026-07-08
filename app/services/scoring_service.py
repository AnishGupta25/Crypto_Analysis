from app.models.coin import Coin
from app.models.coin_score import CoinScore
class ScoringService:
    def __init__(self):
        pass

    def calculate_market_cap_score(self,coin: Coin) -> float:
        rank = coin.market_cap_rank
        if rank is None:
            return 0.0
        score = max(0, 101 - rank)
        return score

    def calculate_liquidity_score(self, coin: Coin) -> float:
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
        
    def calculate_momentum_score(self, coin: Coin) -> float:
        price_change = coin.price_change_percentage_24h

        if price_change is None:
            return 0

        if price_change > 20:
            return 100

        if price_change > 10:
            return 50

        if price_change > 0:
            return 25

        if price_change > -20:
            return 10
        
        return 0
    
    def calculate(self, coin: Coin) -> CoinScore:
        market_cap_score = self.calculate_market_cap_score(coin)
        liquidity_score = self.calculate_liquidity_score(coin)
        momentum_score = self.calculate_momentum_score(coin)

        total_score = (market_cap_score + liquidity_score + momentum_score) / 3
        return CoinScore(
            coin=coin,
            market_cap_score=market_cap_score,
            liquidity_score=liquidity_score,
            momentum_score=momentum_score,
            overall_score=total_score
        )
