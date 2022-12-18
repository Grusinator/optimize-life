from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class PredictFutureEconomy:
    def __init__(self, economic_situation: EconomicSituation, *conditions: EconomicIterator):
        self.economic_situation = economic_situation
        self.conditions = conditions

    def predict_future_economy(self, stop=12) -> EconomicSituation:

        for i in range(stop):
            for iter in self.conditions:
                self.economic_situation += iter.monthly_iterator().__next__()
        return self.economic_situation
