import panel as pn
from panel.template import BootstrapTemplate
from panel.widgets import Button
from param import Dynamic, Parameter

from app.widgets.economic_situation_widget import EconomicSituationWidget
from app.widgets.personal_expenses_widget import PersonalExpensesWidget
from optimize_life.income_tax import IncomeTax
from optimize_life.predict_future_economy import PredictFutureEconomy
from optimize_life.script import plot_investment_prediction, predict_and_plot

pn.extension()


class OptimizeLifeApp(BootstrapTemplate):
    def __init__(self):
        self.widgets = [PersonalExpensesWidget()]
        self.economic_situation_widget = EconomicSituationWidget()
        self.economy_predictor = PredictFutureEconomy(self.economic_situation_widget.create_economic_situation())

        self.refresh_button = Button()

        allocation = pn.widgets.IntSlider(name='allocation', value=1500, start=1, end=2000)
        agro_land_ha = pn.widgets.FloatSlider(name='agro land', value=16, start=0, end=32)
        loan_interest = pn.widgets.FloatSlider(name='interest', value=0.05, start=0.0, end=0.1, step=0.01)
        cost_of_living = pn.widgets.IntSlider(name='cost of living', value=15000, start=0, end=30000)

        cost_pr_ha = 130000
        house_cost = 1000000

        interactive = pn.bind(plot_investment_prediction,
                              agro_land_ha=agro_land_ha,
                              consultancy_allocation=allocation,
                              cost_pr_ha=cost_pr_ha,
                              house_cost=house_cost, loan_interest=loan_interest,
                              cost_of_living=cost_of_living)
        plot_and_other = [allocation, agro_land_ha, loan_interest, cost_of_living, interactive]
        main = pn.GridSpec()
        main[0, 0:1] = pn.Column(*self.widgets)
        main[0, 1:2] = pn.Column(*plot_and_other)
        sidebar = pn.Column(self.economic_situation_widget)
        self.watch_all_widgets()
        super().__init__(title="Optimize Life", main=main, sidebar=sidebar)

    def watch_all_widgets(self):
        for widget in self.widgets:
            param_names = [widget_param for widget_param in widget.__dict__ if
                           isinstance(widget_param, (Dynamic, Parameter))]
            widget.param.watch(self.create_plot, param_names)

    def create_plot(self, *events):
        return predict_and_plot(self.economy_predictor)

    def create_economic_iterators_from_widgets(self):
        return [widget.get_economic_iterator() for widget in self.widgets]

    def update_economy_prediction_conditions(self):
        personal_tax = IncomeTax()
        conditions = self.create_economic_iterators_from_widgets()
        economic_situation = self.economic_situation_widget.create_economic_situation()
        self.economy_predictor = PredictFutureEconomy(economic_situation, *conditions, tax_model=personal_tax)
