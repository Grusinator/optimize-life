from typing import Generator, Iterator

from economic_iterators.economic_iterator import EconomicIterator
from economic_situation import EconomicSituation


class Job(EconomicIterator):

    def __init__(self, salary):
        self.salary = salary

    def monthly_iterator(self)-> Iterator:
        yield EconomicSituation(self.salary)