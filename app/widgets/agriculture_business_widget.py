from param import Parameterized, Integer, Boolean

from optimize_life.economic_iterators.agriculture_business import AgricultureBusiness
from optimize_life.economic_iterators.economic_iterator import EconomicIterator
from optimize_life.economic_iterators.job import Job


class AgricultureBusinessWidget(Parameterized):
    enabled = Boolean(default=True)
    yearly_income = Integer()

    def get_economic_iterator(self) -> EconomicIterator:
        return AgricultureBusiness(self.yearly_income)
