from typing import Iterator

from optimize_life.economic_iterators.mortgage_loan import MortgageLoan
from optimize_life.economic_situation import EconomicSituation


class CompanyInvestmentLoan(MortgageLoan):
    loan_to_value_ratio = 0.9

    def monthly_iterator(self) -> Iterator:
        yield EconomicSituation(0, company_capital=self.pay_loan_one_month())
