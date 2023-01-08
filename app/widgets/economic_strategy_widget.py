import param

from optimize_life.economic_strategy import EconomicStrategy


class EconomicStrategyWidget(param.Parameterized):
    ensure_enough_money_on_private = param.Boolean(default=False)
    loan_private_to_company = param.Boolean(default=True)
    pay_off_loans = param.Boolean(default=True)
    transfer_income_to_private = param.Boolean(default=True)
    transfer_business_profit_to_capital = param.Boolean(default=False)

    def create_economic_strategy(self):
        return EconomicStrategy(
            self.ensure_enough_money_on_private,
            self.loan_private_to_company,
            self.pay_off_loans,
            self.transfer_income_to_private,
            self.transfer_business_profit_to_capital,
        )
