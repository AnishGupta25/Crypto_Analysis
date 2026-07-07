from abc import ABC, abstractmethod
from app.models.coin import Coin

class CoinProvider(ABC):

    @abstractmethod
    def get_top_coins(self, limit: int = 100) -> list[Coin]:
        pass