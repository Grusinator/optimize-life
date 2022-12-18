from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class PredictFutureEconomy:
    def __init__(self, economic_situation: EconomicSituation, *conditions: EconomicIterator, prioritize_private=True):
        self.economic_situation = economic_situation
        self.conditions = list(conditions)
        self.prioritize_private = prioritize_private
        self.month = 0

    def predict_future_economy(self, n_months=12) -> EconomicSituation:
        for i in range(self.month, self.month + n_months):
            self._step_one_month_ahead()
            years, months = divmod(self.month, 12)
            message = f"year: {years + 1}, month {months}, {self.economic_situation}"
            print(message)
        return self.economic_situation

    def _step_one_month_ahead(self):
        self.month += 1
        for condition in self.conditions:
            self.economic_situation += condition.monthly_iterator().__next__()
            if self.prioritize_private:
                self.economic_situation.transfer_to_private()
