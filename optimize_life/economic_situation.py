from dataclasses import dataclass

from income_tax import IncomeTax

INF = 9999999999


class EconomicSituation:
    """used as a economic balance but also an economic result"""

    def __init__(self, private_capital, company_capital: int = 0, private_investment_loan: int = 0):
        self.private_capital = private_capital
        self.company_capital = company_capital
        self.private_investment_loan = private_investment_loan
        self.income_tax = IncomeTax()

    def __str__(self):
        return f"private_capital: {self.private_capital:,.0f}, " \
               f"company_capital: {self.company_capital:,.0f}"

    def __add__(self, other: "EconomicSituation"):
        private_capital = self.private_capital + other.private_capital
        company_capital = self.company_capital + other.company_capital
        private_investment_loan = self.private_investment_loan + other.private_investment_loan
        return EconomicSituation(private_capital, company_capital, private_investment_loan)

    def __sub__(self, other: "EconomicSituation"):
        private_capital = self.private_capital - other.private_capital
        company_capital = self.company_capital - other.company_capital
        private_investment_loan = self.private_investment_loan - other.private_investment_loan
        return EconomicSituation(private_capital, company_capital, private_investment_loan)

    def transfer_to_private(self, amount=INF):
        amount_transferred = self.pay_back_private_investment(amount)
        self.transfer_to_private_via_income_tax(amount - amount_transferred)

    def ensure_enough_money_on_private(self):
        while self.private_capital < 0:
            if self.company_capital < 0:
                raise Exception("You are out of money!!")
            self.transfer_to_private(1000)

    def transfer_to_private_via_income_tax(self, amount=INF):
        income_before_tax = min(self.company_capital, amount)
        # TODO convert to the actual model for income, this should not be here. move Income tax out
        income_after_tax_monthly = self.income_tax.calculate_simple_income_tax_monthly(income_before_tax)
        self.private_capital += income_after_tax_monthly
        self.company_capital -= income_before_tax

    def pay_back_private_investment(self, amount=INF):
        private_investment_payback = min(self.private_investment_loan, self.company_capital, amount)
        self.company_capital -= private_investment_payback
        self.private_capital += private_investment_payback
        return private_investment_payback

    def invest_private_money(self, amount: int = INF):
        investment = min(amount, self.private_capital)
        self.private_investment_loan += investment
        self.private_capital -= investment
        self.company_capital += investment


if __name__ == "__main__":
    EconomicSituation(3, 2) + EconomicSituation(4, 1)
