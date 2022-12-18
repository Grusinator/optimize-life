from dataclasses import dataclass


@dataclass
class EconomicSituation:
    """used as a economic balance but also an economic result"""
    private_capital: int
    company_capital: int = 0

    def __add__(self, other: "EconomicSituation"):
        private_capital = self.private_capital + other.private_capital
        company_capital = self.company_capital + other.company_capital
        return EconomicSituation(private_capital, company_capital)

    def __sub__(self, other: "EconomicSituation"):
        private_capital = self.private_capital - other.private_capital
        company_capital = self.company_capital - other.company_capital
        return EconomicSituation(private_capital, company_capital)


if __name__ == "__main__":
    EconomicSituation(3, 2) + EconomicSituation(4, 1)