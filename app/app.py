import panel as pn
from bokeh.plotting import figure
from panel.pane import Bokeh
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

pn.extension(notifications=True, sizing_mode="stretch_both")


class OptimizeLifeApp(BootstrapTemplate):
    widget_types = [CostOfLivingWidget, JobWidget, CreditLoanWidget, ConsultancyBusinessWidget,
                    AgricultureBusinessWidget, MortgageLoanWidget]

    def __init__(self):
        self.widgets: list = [
            CostOfLivingWidget(monthly_expenses=15000),
            # JobWidget(),
            CreditLoanWidget(amount=4500000),
            ConsultancyBusinessWidget(hourly_rate=750, internal_expenses=4000, allocation=1800),
            AgricultureBusinessWidget(yearly_income=32 * 4000),
            # MortgageLoanWidget()
        ]
        self.economic_situation_widget = EconomicSituationWidget(private_capital=500000)
        self.economic_strategy_widget = EconomicStrategyWidget()

        self.bokeh_plot = pn.pane.Bokeh(figure(), sizing_mode='stretch_both', max_height=500)

        self.try_calculate_prediction_and_built_plot()
        clear_all_button = self.create_clear_all_widgets()
        self.column_with_widgets = pn.Column(*self.widgets, scroll=True, max_height=500)
        self.gs_layout = self.create_main_layout()
        add_widget_button = self.create_widget_selector()
        sidebar = pn.Column(self.economic_situation_widget, self.economic_strategy_widget, clear_all_button,
                            add_widget_button)
        self.watch_all_widgets()
        super().__init__(title="Optimize Life", main=self.gs_layout, sidebar=sidebar)
        self.calculate_prediction_and_update_plot(None)

    def reset_widgets(self, event):
        self.widgets = []
        self.column_with_widgets.objects = []
        self.calculate_prediction_and_update_plot()

    def create_clear_all_widgets(self):
        button = pn.widgets.Button(name="clear", height=60, type="warning")
        button.on_click(self.reset_widgets)
        return button

    def create_widget_selector(self):
        items = [(widget.name, widget.__name__) for widget in self.widget_types]
        button = pn.widgets.MenuButton(name="Add condition", items=items, height=60)
        button.on_click(self.add_widget_on_click)
        return button

    def add_widget_on_click(self, event):
        widget_name = event.new
        widget = [widget() for widget in self.widget_types if widget.__name__ == widget_name][0]
        self.widgets.append(widget)
        self.column_with_widgets.append(widget)
        self.watch_widget(widget)
        self.calculate_prediction_and_update_plot()

    def create_main_layout(self):
        gs = pn.GridSpec(sizing_mode='stretch_both', max_height=500)
        gs[0, 0:1] = self.column_with_widgets
        gs[0, 1:4] = self.bokeh_plot
        return gs

    def watch_all_widgets(self):
        sidebar_widgets = [self.economic_strategy_widget, self.economic_situation_widget]
        for widget in self.widgets + sidebar_widgets:
            self.watch_widget(widget)

    def watch_widget(self, widget):
        widget_param_names = list(set(widget.param.params().keys()) - {"name"})
        widget.param.watch(self.calculate_prediction_and_update_plot, widget_param_names)

    def calculate_prediction_and_update_plot(self, *events):
        self.bokeh_plot.object = self.try_calculate_prediction_and_built_plot()

    def try_calculate_prediction_and_built_plot(self):
        try:
            return self.update_economy_prediction_conditions()
        except Exception as e:
            pn.state.notifications.error(f'This is an error notification. {e}', duration=5000)

    def create_economic_iterators_from_widgets(self):
        return [widget.get_economic_iterator() for widget in self.widgets if widget.enabled]

    def update_economy_prediction_conditions(self):
        personal_tax = IncomeTax()
        conditions = self.create_economic_iterators_from_widgets()
        economic_situation = self.economic_situation_widget.create_economic_situation()
        economic_strategy = self.economic_strategy_widget.create_economic_strategy()
        economy_predictor = PredictFutureEconomy(economic_situation, *conditions,
                                                 economic_strategy=economic_strategy, tax_model=personal_tax)
        return predict_and_plot(economy_predictor)
