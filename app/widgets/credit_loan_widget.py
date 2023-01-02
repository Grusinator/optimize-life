from param import Parameterized, Integer, Boolean, Number

from optimize_life.economic_iterators.credit_loan import CreditLoan
from optimize_life.economic_iterators.economic_iterator import EconomicIterator


class CreditLoanWidget(Parameterized):
    enabled = Boolean(default=True)
    amount = Integer()
    interest_rate = Number(default=0.05, bounds=(0.00, 0.1), step=0.01)

    def get_economic_iterator(self) -> EconomicIterator:
        return CreditLoan(self.amount, self.interest_rate)
