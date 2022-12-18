from typing import Generator, Iterator

from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class CostOfLiving(EconomicIterator):
    def __init__(self, monthly_expenses):
        self.monthly_expenses = monthly_expenses

    def monthly_iterator(self)-> Iterator:
        yield EconomicSituation(- self.monthly_expenses)