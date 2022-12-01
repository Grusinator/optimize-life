from typing import Generator

from economic_iterator import EconomicIterator


class Job(EconomicIterator):

    def __init__(self, salary):
        self.salary = salary

    def monthly_iterator(self) -> Generator:
        yield self.salary