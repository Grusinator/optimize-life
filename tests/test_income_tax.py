import pytest

from income_tax import IncomeTax


@pytest.mark.parametrize("income_before_tax, exp_income_after_tax", (
        (0, 0),
        (40000, 36800.0),
        (200000, 126400.0),
        (1000000, 494000.0)
))
def test_income_tax(income_before_tax, exp_income_after_tax):
    income = IncomeTax().calculate_income_after_tax(income_before_tax)
    assert income == exp_income_after_tax
