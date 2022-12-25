from typing import Iterator

from optimize_life.economic_iterators.base_loan import Loan
from optimize_life.economic_situation import EconomicSituation


class CreditLoan(Loan):

    def __init__(self, amount, interest_rate):
        self.amount = amount
        self.interest_rate = interest_rate
        self.started = False
        self.debt = 0
        self.total_payed_interest = 0

    def monthly_iterator(self) -> Iterator:
        if not self.started:
            self.started = True
            self.debt = self.amount
        interest = self.calculate_montly_interest()
        self.total_payed_interest += interest
        yield EconomicSituation(0, company_capital=-interest)

    def calculate_montly_interest(self) -> int:
        return int(self.interest_rate * self.debt / 12)

    def payback(self, economic_situation: EconomicSituation):
        payback_amount = min(self.debt, economic_situation.company_capital)
        payback_amount *= 0.78  # payment of company taxes
        self.debt -= payback_amount
        economic_situation.company_capital -= payback_amount
        self.create_debug_message(payback_amount)

    def create_debug_message(self, payback_amount):
        print(f"payed back {payback_amount:,.0f}, debt is now: {self.debt:,.0f}")
