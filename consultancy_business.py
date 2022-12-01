from typing import Generator

from economic_iterator import EconomicIterator


class ConsultancyBusiness(EconomicIterator):

    def __init__(self, hourly_rate, internal_expenses, allocation):
        self.hourly_rate = hourly_rate
        self.internal_expenses = internal_expenses
        self.allocation = allocation

    def monthly_economy(self):
        return self.hourly_rate * self.allocation - self.internal_expenses

    def monthly_iterator(self) -> Generator:
        yield self.monthly_economy()