from abc import abstractmethod, ABC
from typing import Generator, Iterator

from economic_situation import EconomicSituation


class EconomicIterator(ABC):

    @abstractmethod
    def monthly_iterator(self) -> Iterator:
        pass

    def execute_strategy(self, *args, **kwargs):
        pass
