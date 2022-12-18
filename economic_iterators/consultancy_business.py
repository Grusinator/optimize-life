from typing import Iterator

from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class ConsultancyBusiness(EconomicIterator):

    def __init__(self, hourly_rate, internal_expenses, allocation: float):
        """
        :param hourly_rate: kr/hour
        :param internal_expenses: kr
        :param allocation: hours pr month
        """
        self.hourly_rate = hourly_rate
        self.internal_expenses = internal_expenses
        self.allocation = allocation

    def monthly_result(self):
        return self.hourly_rate * self.allocation - self.internal_expenses

    def monthly_iterator(self)-> Iterator:
        company_money = self.monthly_result()
        yield EconomicSituation(0, company_money)