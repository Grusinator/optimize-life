from typing import Iterator

from optimize_life.economic_iterators.economic_iterator import EconomicIterator
from optimize_life.economic_situation import EconomicSituation
from optimize_life.income_tax import IncomeTax


class Job(EconomicIterator):

    def __init__(self, salary):
        self.salary = salary

    def monthly_iterator(self) -> Iterator:
        income_after_tax = IncomeTax().calculate_income_after_tax_monthly(self.salary)
        yield EconomicSituation(income_after_tax)
