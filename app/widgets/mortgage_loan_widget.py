from param import Parameterized, Integer, Boolean, Number

from optimize_life.economic_iterators.economic_iterator import EconomicIterator
from optimize_life.economic_iterators.mortgage_loan import MortgageLoan


class MortgageLoanWidget(Parameterized):
    enabled = Boolean(default=True)
    amount = Integer()
    interest_rate = Number(default=0.05, bounds=(0.0, 0.1), step=0.01)
    kurs = Integer(100)
    payment = Integer()

    def get_economic_iterator(self) -> EconomicIterator:
        return MortgageLoan(self.amount, self.interest_rate, self.kurs, self.payment)
