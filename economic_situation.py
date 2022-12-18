from dataclasses import dataclass

from income_tax import IncomeTax


@dataclass
class EconomicSituation:
    """used as a economic balance but also an economic result"""
    private_capital: int
    company_capital: int = 0

    def __str__(self):
        return f"private_capital: {self.private_capital:,.0f}, " \
               f"company_capital: {self.company_capital:,.0f}"

    def __add__(self, other: "EconomicSituation"):
        private_capital = self.private_capital + other.private_capital
        company_capital = self.company_capital + other.company_capital
        return EconomicSituation(private_capital, company_capital)

    def __sub__(self, other: "EconomicSituation"):
        private_capital = self.private_capital - other.private_capital
        company_capital = self.company_capital - other.company_capital
        return EconomicSituation(private_capital, company_capital)

    def transfer_to_private(self, keep: int = 0):
        self.private_capital += IncomeTax().calculate_income_tax_monthly(self.company_capital - keep)
        self.company_capital = keep


if __name__ == "__main__":
    EconomicSituation(3, 2) + EconomicSituation(4, 1)
