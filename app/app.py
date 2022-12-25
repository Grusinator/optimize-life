import panel as pn

from optimize_life.script import plot_investment_prediction

pn.extension()

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

app = pn.Column(allocation, agro_land_ha, loan_interest, cost_of_living, interactive)
