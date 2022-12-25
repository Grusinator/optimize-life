from abc import ABCMeta, abstractmethod

from optimize_life.economic_iterators.economic_iterator import EconomicIterator
from optimize_life.economic_situation import EconomicSituation


class Loan(EconomicIterator, metaclass=ABCMeta):
    debt: int
    total_payed_interest: int

    @abstractmethod
    def payback(self, economic_situation: EconomicSituation):
        pass
