from typing import Generator

from economic_iterator import EconomicIterator


class CostOfLiving(EconomicIterator):
    def __init__(self, monthly_expenses):
        self.monthly_expenses = monthly_expenses

    def monthly_iterator(self) -> Generator:
        yield - self.monthly_expenses