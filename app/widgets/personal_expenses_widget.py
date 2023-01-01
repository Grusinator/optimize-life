from abc import ABCMeta, abstractmethod

from param import Parameterized, Integer, Boolean

from optimize_life.economic_iterators.cost_of_living import CostOfLiving
from optimize_life.economic_iterators.economic_iterator import EconomicIterator


class PersonalExpensesWidget(Parameterized):
    enabled = Boolean(default=True)
    monthly_expenses = Integer()

    def __init__(self):
        self.model = CostOfLiving
        super().__init__()

    def get_economic_iterator(self) -> EconomicIterator:
        return CostOfLiving(self.monthly_expenses)
