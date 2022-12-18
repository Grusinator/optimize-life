from collections import Iterator

from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class MortgageLoan(EconomicIterator):
    def __init__(self, amount, interest, kurs, payment, timespan=30):
        self.amount = amount
        self.interest = interest
        self.kurs = kurs
        self.payment = payment
        self.timespan = timespan
        self.debt = 0
        self.n_instalments = timespan * 12

    def pay_loan_one_month(self):
        money = 0
        if self.debt == 0:
            self.debt = self.amount
            money -= self.payment

        money -= self.debt * self.interest
        money -= self.amount / self.n_instalments
        self.debt -= self.amount / self.n_instalments
        return money

    def monthly_iterator(self)-> Iterator:
        yield EconomicSituation(self.pay_loan_one_month())
