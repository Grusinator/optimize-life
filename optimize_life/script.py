from bokeh.plotting import figure, show

from optimize_life.economic_conversions import EconomicConversion
from optimize_life.economic_iterators.agriculture_business import AgricultureBusiness
from optimize_life.economic_iterators.consultancy_business import ConsultancyBusiness
from optimize_life.economic_iterators.cost_of_living import CostOfLiving
from optimize_life.economic_iterators.company_credit_loan import CompanyCreditLoan
from optimize_life.economic_situation import EconomicSituation
from optimize_life.income_tax import IncomeTax
from optimize_life.predict_future_economy import PredictFutureEconomy


def main():
    # try to run for different cases, to see what the outcome will be, fx. try to see if it makes the
    #  most sense to buy a farm as a private thing, vs as a business. How tight will my economy be etc.
    loan_interest = 0.04
    agro_land_ha = 32.16
    cost_pr_ha = 130000
    house = 1000000
    consultancy_allocation = 1500
    cost_of_living = 15000
    p = plot_investment_prediction(agro_land_ha, consultancy_allocation, cost_pr_ha, house, loan_interest,
                                   cost_of_living)
    show(p)


def plot_investment_prediction(agro_land_ha, consultancy_allocation, cost_pr_ha, house_cost, loan_interest,
                               cost_of_living):
    land_cost = agro_land_ha * cost_pr_ha
    total_farm_cost = house_cost + land_cost
    print(f"total farm cost: {total_farm_cost}")
    consultancy = ConsultancyBusiness(hourly_rate=750, internal_expenses=50000, allocation=consultancy_allocation)
    credit_loan = CompanyCreditLoan(total_farm_cost, loan_interest)
    agriculture_business = AgricultureBusiness((agro_land_ha * 4000) - 100000)
    cost_of_living = CostOfLiving(cost_of_living)
    personal_tax = IncomeTax()
    economic_situation = EconomicSituation(private_capital=450000, company_capital=0)
    conversion = EconomicConversion(personal_tax, economic_situation)
    conversion.invest_private_money(450000)
    economy_predictor = PredictFutureEconomy(
        economic_situation,
        cost_of_living,
        consultancy,
        agriculture_business,
        credit_loan,
        tax_model=personal_tax
    )
    p = predict_and_plot(economy_predictor)
    return p


def predict_and_plot(economy_predictor: PredictFutureEconomy, years=10):
    economy_predictor.predict_future_economy(years * 12)
    month, private_capital, company_capital, company_profit, debt, total_payed_interest = list(
        zip(*economy_predictor.history))
    month = [m / 12 for m in month]
    title = f"prediction"
    p = figure(width=1500, height=600, title=title)
    p.line(month, private_capital, line_width=2, legend_label="private")
    p.line(month, company_capital, line_width=2, color="green", legend_label="company capital")
    p.line(month, company_profit, line_width=2, color="brown", legend_label="company profit")
    p.line(month, debt, line_width=2, color="black", legend_label="debt")
    p.line(month, total_payed_interest, line_width=2, color="red", legend_label="interest payed")
    return p


if __name__ == "__main__":
    main()
