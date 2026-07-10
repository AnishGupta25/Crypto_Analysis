from app.models.coin import Coin
from app.models.coin_score import CoinScore
from app.scorers.market_cap_scorer import MarketCapScorer
from app.scorers.liquidity_scorer import LiquidityScorer
from app.scorers.momentum_scorer import MomentumScorer
class ScoringService:
    def __init__(self):
        self.market_cap = MarketCapScorer()
        self.liquidity = LiquidityScorer()
        self.momentum = MomentumScorer()

    def calculate_market_cap_score(self,coin: Coin) -> float:
        return self.market_cap.score(coin)

    def calculate_liquidity_score(self, coin: Coin) -> float:
        return self.liquidity.score(coin)

    def calculate_momentum_score(self, coin: Coin) -> float:
        return self.momentum.score(coin)

    def calculate(self, coin: Coin) -> CoinScore:
        market_cap_score = self.calculate_market_cap_score(coin)
        liquidity_score = self.calculate_liquidity_score(coin)
        momentum_score = self.calculate_momentum_score(coin)

        total_score = (market_cap_score * 0.4 + liquidity_score * 0.4 + momentum_score * 0.2)
        return CoinScore(
            coin=coin,
            market_cap_score=market_cap_score,
            liquidity_score=liquidity_score,
            momentum_score=momentum_score,
            overall_score=total_score
        )

