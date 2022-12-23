from dataclasses import dataclass
from enum import Enum, auto

from economic_iterators.base_loan import Loan
from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


@dataclass
class EconomicStrategy:
    pay_off_loans = True
    transfer_income_to_private: bool = True


class PredictFutureEconomy:
    def __init__(self, economic_situation: EconomicSituation, *conditions: EconomicIterator,
                 economic_strategy: EconomicStrategy = EconomicStrategy()):
        self.economic_situation = economic_situation
        self.conditions = list(conditions)
        self.economic_strategy = economic_strategy
        self.month = 0
        self.history = []

    def predict_future_economy(self, n_months=12) -> EconomicSituation:
        for i in range(self.month, self.month + n_months):
            self._step_one_month_ahead()
            self.create_monthly_debug_message()
        return self.economic_situation

    def create_monthly_debug_message(self):
        years, months = divmod(self.month, 12)
        message = f"year: {years + 1}, month {months}, {self.economic_situation}"
        print(message)

    def _step_one_month_ahead(self):
        self.month += 1
        self.build_historic_snapshot()
        self.calculate_monthly_result_for_all_conditions()
        self.economic_situation.ensure_enough_money_on_private()
        if self.economic_strategy.pay_off_loans:
            self.pay_off_loans()
        if self.economic_strategy.transfer_income_to_private:
            self.economic_situation.transfer_to_private()

    def calculate_monthly_result_for_all_conditions(self):
        for condition in self.conditions:
            self.economic_situation += condition.monthly_iterator().__next__()

    def pay_off_loans(self):
        for condition in self.conditions:
            if isinstance(condition, Loan):
                condition.payback(self.economic_situation)

    def build_historic_snapshot(self):
        debt = sum([condition.debt for condition in self.conditions if isinstance(condition, Loan)])
        total_payed_interest = sum(
            [condition.total_payed_interest for condition in self.conditions if isinstance(condition, Loan)])
        self.history.append((self.month, self.economic_situation.private_capital,
                             self.economic_situation.company_capital, debt, total_payed_interest))
