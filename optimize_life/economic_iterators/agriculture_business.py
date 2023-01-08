from typing import Iterator

from optimize_life.economic_iterators.economic_iterator import EconomicIterator
from optimize_life.economic_situation import EconomicSituation


class AgricultureBusiness(EconomicIterator):

    def __init__(self, yearly_income):
        self._month_counter = 0
        self.yearly_income = yearly_income

    def monthly_iterator(self) -> Iterator:
        is_first_month_of_year = divmod(self._month_counter, 12)[1] == 0
        income = self.yearly_income if is_first_month_of_year else 0
        self._month_counter += 1
        yield EconomicSituation(0, company_profit=income)
