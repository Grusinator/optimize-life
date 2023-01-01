import pandas as pd
import panel as pn
import param
from panel.template import BootstrapTemplate
from panel.widgets import Button
from param import Dynamic, Parameter

from app.widgets.economic_situation_widget import EconomicSituationWidget
from app.widgets.economic_strategy_widget import EconomicStrategyWidget
from app.widgets.personal_expenses_widget import PersonalExpensesWidget
from optimize_life.income_tax import IncomeTax
from optimize_life.predict_future_economy import PredictFutureEconomy
from optimize_life.script import plot_investment_prediction, predict_and_plot

pn.extension()


class OptimizeLifeApp(BootstrapTemplate):
    data = param.DataFrame()

    def __init__(self):
        self.widgets = [PersonalExpensesWidget()]
        self.economic_situation_widget = EconomicSituationWidget()
        self.economic_strategy_widget = EconomicStrategyWidget()
        self.economy_predictor = PredictFutureEconomy(
            economic_situation=self.economic_situation_widget.create_economic_situation(),
            economic_strategy=self.economic_strategy_widget.create_economic_strategy()
        )

        self.refresh_button = Button()

        # allocation = pn.widgets.IntSlider(name='allocation', value=1500, start=1, end=2000)
        # agro_land_ha = pn.widgets.FloatSlider(name='agro land', value=16, start=0, end=32)
        # loan_interest = pn.widgets.FloatSlider(name='interest', value=0.05, start=0.0, end=0.1, step=0.01)
        # cost_of_living = pn.widgets.IntSlider(name='cost of living', value=15000, start=0, end=30000)
        #
        # cost_pr_ha = 130000
        # house_cost = 1000000

        # interactive = pn.bind(plot_investment_prediction,
        #                       agro_land_ha=agro_land_ha,
        #                       consultancy_allocation=allocation,
        #                       cost_pr_ha=cost_pr_ha,
        #                       house_cost=house_cost, loan_interest=loan_interest,
        #                       cost_of_living=cost_of_living)
        # plot_and_other = [allocation, agro_land_ha, loan_interest, cost_of_living, interactive]
        main = pn.GridSpec()
        main[0, 0:1] = pn.Column(*self.widgets)
        main[0, 1:2] = lambda: self.update_economy_prediction_conditions()
        sidebar = pn.Column(self.economic_situation_widget)
        self.watch_all_widgets()
        super().__init__(title="Optimize Life", main=main, sidebar=sidebar)

    def plot_predictions(self):
        def plot():
            return "test"
            # self.update_economy_prediction_conditions()
            # return predict_and_plot(self.economy_predictor)

        return plot

    def watch_all_widgets(self):
        for widget in self.widgets:
            widget_param_names = list(set(widget.param.params().keys()) - {"name"})
            widget.param.watch(self.update_data, widget_param_names)

    def update_data(self, *events):
        self.data = pd.DataFrame()

    def create_economic_iterators_from_widgets(self):
        return [widget.get_economic_iterator() for widget in self.widgets]

    def update_economy_prediction_conditions(self):
        personal_tax = IncomeTax()
        conditions = self.create_economic_iterators_from_widgets()
        economic_situation = self.economic_situation_widget.create_economic_situation()
        self.economy_predictor = PredictFutureEconomy(economic_situation, *conditions, tax_model=personal_tax)
        return predict_and_plot(self.economy_predictor)
