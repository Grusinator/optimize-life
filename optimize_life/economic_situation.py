class EconomicSituation:
    """used as an economic balance but also an economic result"""

    def __init__(self, private_capital, company_capital: int = 0, private_investment_loan: int = 0, company_profit=0):
        self.private_capital = private_capital
        self.company_profit = company_profit
        self.company_capital = company_capital
        self.private_investment_loan = private_investment_loan

    def __str__(self):
        return f"private_capital: {self.private_capital:,.0f}, " \
               f"company_capital: {self.company_capital:,.0f}"

    def __add__(self, other: "EconomicSituation"):
        private_capital = self.private_capital + other.private_capital
        company_capital = self.company_capital + other.company_capital
        company_profit = self.company_profit + other.company_profit
        private_investment_loan = self.private_investment_loan + other.private_investment_loan
        return EconomicSituation(private_capital, company_capital, private_investment_loan, company_profit)

    def __sub__(self, other: "EconomicSituation"):
        private_capital = self.private_capital - other.private_capital
        company_capital = self.company_capital - other.company_capital
        company_profit = self.company_profit - other.company_profit
        private_investment_loan = self.private_investment_loan - other.private_investment_loan
        return EconomicSituation(private_capital, company_capital, private_investment_loan, company_profit)


if __name__ == "__main__":
    EconomicSituation(3, 2) + EconomicSituation(4, 1)
