from abc import ABC, abstractmethod

class BaseScorer(ABC):
    @abstractmethod
    def score(self, coin):
        pass