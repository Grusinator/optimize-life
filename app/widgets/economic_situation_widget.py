import param

from optimize_life.economic_situation import EconomicSituation


class EconomicSituationWidget(param.Parameterized):
    private_capital = param.Integer()
    company_capital = param.Integer()

    def create_economic_situation(self):
        return EconomicSituation(self.private_capital, self.company_capital)
