import pytest

from optimize_life.economic_iterators.mortgage_loan import MortgageLoan



def test_mortgage_loan():
    with pytest.raises(ValueError):
        MortgageLoan(1000, 0.01, 100, 199)