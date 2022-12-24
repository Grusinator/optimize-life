from bokeh.plotting import figure, show

from economic_iterators.agriculture_business import AgricultureBusiness
from economic_iterators.consultancy_business import ConsultancyBusiness
from economic_iterators.cost_of_living import CostOfLiving
from economic_iterators.credit_loan import CreditLoan
from economic_situation import EconomicSituation
from predict_future_economy import PredictFutureEconomy


def main():
    # try to run for different cases, to see what the outcome will be, fx. try to see if it makes the
    #  most sense to buy a farm as a private thing, vs as a business. How tight will my economy be etc.
    allocation = 1800
    interest = 0.05
    consultancy = ConsultancyBusiness(hourly_rate=750, internal_expenses=50000, allocation=allocation)
    credit_loan = CreditLoan(3000000, interest)
    agriculture_business = AgricultureBusiness((32.16 * 4000) - 250000)
    cost_of_living = CostOfLiving(20000)
    economic_situation = EconomicSituation(private_capital=450000, company_capital=0)
    economic_situation.invest_private_money(450000)
    economy_predictor = PredictFutureEconomy(
        economic_situation,
        cost_of_living,
        consultancy,
        agriculture_business,
        credit_loan
    )
    economy_predictor.predict_future_economy(10 * 12)
    month, private_capital, company_capital, debt, total_payed_interest = list(zip(*economy_predictor.history))
    month = [m / 12 for m in month]
    title = f"prediction interest:{interest}, allocation: {allocation}"
    p = figure(width=1500, height=800, title=title)
    p.line(month, private_capital, line_width=2, legend_label="private")
    # p.line(month, company_capital, line_width=2, color="green", legend_label="company")
    p.line(month, debt, line_width=2, color="black", legend_label="debt")
    p.line(month, total_payed_interest, line_width=2, color="red", legend_label="interest payed")
    show(p)


if __name__ == "__main__":
    main()
