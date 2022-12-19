from economic_iterators.agriculture_business import AgricultureBusiness
from economic_iterators.company_investment_loan import CompanyInvestmentLoan
from economic_iterators.consultancy_business import ConsultancyBusiness
from economic_iterators.cost_of_living import CostOfLiving
from economic_situation import EconomicSituation
from economic_iterators.job import Job
from economic_iterators.mortgage_loan import MortgageLoan
from predict_future_economy import PredictFutureEconomy

if __name__ == "__main__":
    # try to run for different cases, to see what the outcome will be, fx. try to see if it makes the
    #  most sense to buy a farm as a private thing, vs as a business. How tight will my economy be etc.
    mortgage_loan = MortgageLoan(
        amount=5000000, interest_rate=0.05, kurs=100, payment=1000000
    )

    job = Job(
        salary=53000
    )
    job2 = Job(
        salary=43000
    )

    consultancy = ConsultancyBusiness(hourly_rate=750, internal_expenses=4000, allocation=1500 / 12)

    company_investment = CompanyInvestmentLoan(amount=4500000, interest_rate=0.0647, kurs=100, payment=1500000)

    agriculture_business = AgricultureBusiness(30*3500)
    #
    cost_of_living = CostOfLiving(
        15000
    )
    economic_situation = EconomicSituation(
        private_capital=500000,
        company_capital=1000000,
    )



    economy_predictor = PredictFutureEconomy(economic_situation, cost_of_living, consultancy, agriculture_business, company_investment)
    economy_predictor.prioritize_private = False
    economy_predictor.predict_future_economy()
    print(company_investment.debt)
