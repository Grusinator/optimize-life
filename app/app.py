import panel as pn
from panel.template import BootstrapTemplate

from app.widgets.agriculture_business_widget import AgricultureBusinessWidget
from app.widgets.consultancy_business_widget import ConsultancyBusinessWidget
from app.widgets.credit_loan_widget import CreditLoanWidget
from app.widgets.economic_situation_widget import EconomicSituationWidget
from app.widgets.economic_strategy_widget import EconomicStrategyWidget
from app.widgets.job_widget import JobWidget
from app.widgets.cost_of_living_widget import CostOfLivingWidget
from app.widgets.mortgage_loan_widget import MortgageLoanWidget
from optimize_life.income_tax import IncomeTax
from optimize_life.predict_future_economy import PredictFutureEconomy
from optimize_life.script import predict_and_plot

pn.extension(notifications=True)


class OptimizeLifeApp(BootstrapTemplate):

    def __init__(self):
        self.widgets: list = [
            CostOfLivingWidget(monthly_expenses=15000),
            JobWidget(enabled=False),
            CreditLoanWidget(amount=5000000),
            ConsultancyBusinessWidget(hourly_rate=750, allocation=1800),
            AgricultureBusinessWidget(yearly_income=30 * 4000),
            MortgageLoanWidget()
        ]
        self.economic_situation_widget = EconomicSituationWidget(private_capital=500000)
        self.economic_strategy_widget = EconomicStrategyWidget()
        self.economy_predictor = PredictFutureEconomy(
            self.economic_situation_widget.create_economic_situation(),
            *self.create_economic_iterators_from_widgets(),
            economic_strategy=self.economic_strategy_widget.create_economic_strategy(),
        )
        self.economy_predictor.predict_future_economy()

        self.bokeh_pane = pn.pane.Bokeh(predict_and_plot(self.economy_predictor), sizing_mode='stretch_width')
        main = pn.GridSpec(sizing_mode='stretch_both')
        main[0, 0:1] = pn.Column(*self.widgets)
        main[0, 1:2] = self.bokeh_pane
        sidebar = pn.Column(self.economic_situation_widget, self.economic_strategy_widget)
        self.watch_all_widgets()
        super().__init__(title="Optimize Life", main=main, sidebar=sidebar)

    def watch_all_widgets(self):
        sidebar_widgets = [self.economic_strategy_widget, self.economic_situation_widget]
        for widget in self.widgets + sidebar_widgets:
            widget_param_names = list(set(widget.param.params().keys()) - {"name"})
            widget.param.watch(self.update_data, widget_param_names)

    def update_data(self, *events):
        try:
            self.bokeh_pane.object = self.update_economy_prediction_conditions()
        except Exception as e:
            pn.state.notifications.error(f'This is an error notification. {e}', duration=5000)

    def create_economic_iterators_from_widgets(self):
        return [widget.get_economic_iterator() for widget in self.widgets if widget.enabled]

    def update_economy_prediction_conditions(self):
        personal_tax = IncomeTax()
        conditions = self.create_economic_iterators_from_widgets()
        economic_situation = self.economic_situation_widget.create_economic_situation()
        economic_strategy = self.economic_strategy_widget.create_economic_strategy()
        self.economy_predictor = PredictFutureEconomy(economic_situation, *conditions,
                                                      economic_strategy=economic_strategy, tax_model=personal_tax)
        return predict_and_plot(self.economy_predictor)
