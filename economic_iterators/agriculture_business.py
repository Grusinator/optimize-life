from typing import Iterator

from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class AgricultureBusiness(EconomicIterator):

    def __init__(self, yearly_income):
        self.yearly_income = yearly_income

    def monthly_iterator(self) -> Iterator:
        yield EconomicSituation(0, self.yearly_income / 12)
