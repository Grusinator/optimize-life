from abc import ABCMeta, abstractmethod

from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class Loan(EconomicIterator, metaclass=ABCMeta):
    @abstractmethod
    def payback(self, economic_situation: EconomicSituation):
        pass
