from param import Parameterized, Integer, Boolean

from optimize_life.economic_iterators.consultancy_business import ConsultancyBusiness
from optimize_life.economic_iterators.economic_iterator import EconomicIterator


class ConsultancyBusinessWidget(Parameterized):
    enabled = Boolean(default=True)
    hourly_rate = Integer(default=750)
    internal_expenses = Integer()
    allocation = Integer(default=1800)

    def get_economic_iterator(self) -> EconomicIterator:
        return ConsultancyBusiness(self.hourly_rate, self.internal_expenses, self.allocation)
