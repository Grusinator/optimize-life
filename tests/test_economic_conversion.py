import pytest

from optimize_life.economic_conversions import EconomicConversion
from optimize_life.economic_situation import EconomicSituation
from optimize_life.income_tax import IncomeTax


class TestEconomicConversion:

    @pytest.mark.parametrize("transfer_amount, expected", (
            (2000, 1100),
    ))
    def test_transfer_to_private(self, transfer_amount, expected):
        economic_situation = EconomicSituation(0, company_profit=3000)
        income_tax = IncomeTax()
        economic_conversion = EconomicConversion(income_tax, economic_situation)
        economic_conversion.transfer_from_company_profit_to_private_via_income_tax(transfer_amount)
        assert economic_situation.private_capital == expected

    @pytest.mark.parametrize("private_capital, private_company_loan, company_profit, company_capital, expected", (
            (-1000, 0, 2000, 0, 45),
            (-1000, 0, 0, 2000, 1),
            (-1000, 2000, 0, 2000, 0),
            (-3000, 2000, 2000, 4000, 45),
            # (-8000, 2000, 2000, 2000, 0),

    ))
    def test_ensure_enough_on_private(self, private_capital, private_company_loan, company_profit, company_capital,
                                      expected):
        economic_situation = EconomicSituation(private_capital, company_profit=company_profit,
                                               company_capital=company_capital,
                                               private_investment_loan=private_company_loan)
        income_tax = IncomeTax()
        economic_conversion = EconomicConversion(income_tax, economic_situation)
        economic_conversion.ensure_enough_money_on_private()
        # with pytest.raises(expected):
        assert round(economic_situation.private_capital) == expected
