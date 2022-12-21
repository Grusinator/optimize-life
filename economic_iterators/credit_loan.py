from typing import Iterator

from economic_iterators.base_loan import Loan
from economic_situation import EconomicSituation


class CreditLoan(Loan):

    def __init__(self, amount, interest_rate):
        self.amount = amount
        self.debt = 0
        self.interest_rate = interest_rate
        self.started = False

    def monthly_iterator(self) -> Iterator:
        if not self.started:
            self.started = True
            self.debt = self.amount
        yield EconomicSituation(0, company_capital=-(self.interest_rate * self.debt) / 12)

    def payback(self, economic_situation: EconomicSituation):
        payback_amount = min(self.debt, economic_situation.company_capital)
        self.debt -= payback_amount
        economic_situation.company_capital -= payback_amount
        print(f"payed back {payback_amount:,.0f}, debt is now: {self.debt:,.0f}")
