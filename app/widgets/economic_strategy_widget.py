import param

from optimize_life.predict_future_economy import EconomicStrategy


class EconomicStrategyWidget(param.Parameterized):
    ensure_enough_money_on_private = param.Boolean(default=True)
    loan_private_to_company = param.Boolean(default=True)
    pay_off_loans = param.Boolean(default=True)
    transfer_income_to_private = param.Boolean(default=True)

    def create_economic_strategy(self):
        return EconomicStrategy(
            self.ensure_enough_money_on_private,
            self.loan_private_to_company,
            self.pay_off_loans,
            self.transfer_income_to_private,
        )
