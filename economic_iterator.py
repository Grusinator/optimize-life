from abc import abstractmethod, ABC
from typing import Generator


class EconomicIterator(ABC):

    @abstractmethod
    def monthly_iterator(self) -> Generator:
        pass

