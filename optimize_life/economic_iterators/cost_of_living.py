from typing import Iterator

from optimize_life.economic_iterators.economic_iterator import EconomicIterator
from optimize_life.economic_situation import EconomicSituation


class CostOfLiving(EconomicIterator):
    def __init__(self, monthly_expenses):
        self.monthly_expenses = monthly_expenses

    def monthly_iterator(self) -> Iterator:
        yield EconomicSituation(- self.monthly_expenses)
