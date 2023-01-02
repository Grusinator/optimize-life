from abc import ABCMeta, abstractmethod

from param import Parameterized, Integer, Boolean

from optimize_life.economic_iterators.cost_of_living import CostOfLiving
from optimize_life.economic_iterators.economic_iterator import EconomicIterator
from optimize_life.economic_iterators.job import Job


class JobWidget(Parameterized):
    enabled = Boolean(default=True)
    monthly_salary = Integer()

    def get_economic_iterator(self) -> EconomicIterator:
        return Job(self.monthly_salary)
