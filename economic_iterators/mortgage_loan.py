from collections import Iterator

from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class MortgageLoan(EconomicIterator):
    loan_to_value_ratio = 0.8

    def __init__(self, amount, interest_rate, kurs, payment, timespan=30):
        self.amount = amount
        self.interest_rate = interest_rate
        self.kurs = kurs
        self.down_payment = payment
        self.timespan = timespan
        self.debt = 0
        self.n_instalments = timespan * 12
        min_payment = amount * (1 - self.loan_to_value_ratio)
        if self.down_payment < min_payment-1:
            raise ValueError(f"payment of {self.down_payment:,.0f} is too small, it must be at least {min_payment:,.0f}")

    def pay_loan_one_month(self):
        monthly_payment = 0
        if self.debt == 0:
            self.debt = self.amount - self.down_payment
            monthly_payment -= self.down_payment

        interest = (self.debt * self.interest_rate) / 12
        monthly_payment -= interest
        instalment = self.amount / self.n_instalments
        monthly_payment -= instalment
        self.debt -= instalment
        return monthly_payment

    def monthly_iterator(self) -> Iterator:
        yield EconomicSituation(self.pay_loan_one_month())
