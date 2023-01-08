import pytest

from optimize_life.economic_iterators.agriculture_business import AgricultureBusiness
from optimize_life.economic_iterators.credit_loan import CreditLoan
from optimize_life.economic_situation import EconomicSituation
from optimize_life.economic_strategy import EconomicStrategy
from optimize_life.income_tax import IncomeTax
from optimize_life.predict_future_economy import PredictFutureEconomy


class TestPredictFutureEconomy:

    @pytest.mark.parametrize("income_before_tax, exp_income_after_tax", (
            (0, 0),
    ))
    def test_predict_future_economy(self, income_before_tax, exp_income_after_tax):
        economic_situation = EconomicSituation(0)
        economic_strategy = EconomicStrategy(
            transfer_business_profit_to_capital=True,
        )
        conditions = [
            AgricultureBusiness(120000),
            CreditLoan(500000, 0.05),
        ]
        predictor = PredictFutureEconomy(economic_situation, economic_strategy=economic_strategy, *conditions)
        predictor.predict_future_economy(24)
        assert predictor.economic_situation.private_capital == exp_income_after_tax
