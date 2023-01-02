from optimize_life.economic_situation import EconomicSituation
from optimize_life.income_tax import IncomeTax

INF = 9999999999


class EconomicConversion:
    def __init__(self, tax_model: IncomeTax, economic_situation: EconomicSituation):
        self.tax_model = tax_model
        self.economic_situation = economic_situation

    def transfer_to_private(self, amount=INF):
        amount_transferred = self.pay_back_private_investment(amount)
        self.transfer_to_private_via_income_tax(amount - amount_transferred)

    def ensure_enough_money_on_private(self):
        while self.economic_situation.private_capital < 0:
            if self.economic_situation.company_capital <= 0:
                raise Exception("You are out of money!!")
            self.transfer_to_private(1000)

    def transfer_to_private_via_income_tax(self, amount=INF):
        income_before_tax = min(self.economic_situation.company_capital, amount)
        # TODO convert to the actual model for income, this should not be here. move Income tax out
        income_after_tax_monthly = self.tax_model.calculate_simple_income_tax_monthly(income_before_tax)
        self.economic_situation.private_capital += income_after_tax_monthly
        self.economic_situation.company_capital -= income_before_tax

    def pay_back_private_investment(self, amount=INF):
        private_investment_payback = min(self.economic_situation.private_investment_loan,
                                         self.economic_situation.company_capital, amount)
        self.economic_situation.company_capital -= private_investment_payback
        self.economic_situation.private_capital += private_investment_payback
        return private_investment_payback

    def invest_private_money(self, amount: int = INF):
        investment = min(amount, self.economic_situation.private_capital)
        self.economic_situation.private_investment_loan += investment
        self.economic_situation.private_capital -= investment
        self.economic_situation.company_capital += investment
