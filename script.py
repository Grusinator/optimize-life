from consultancy_business import ConsultancyBusiness
from cost_of_living import CostOfLiving
from economic_situation import EconomicSituation
from job import Job
from mortgage_loan import MortgageLoan
from predict_future_economy import PredictFutureEconomy

if __name__ == "__main__":
    # try to run for different cases, to see what the outcome will be, fx. try to see if it makes the
    #  most sense to buy a farm as a private thing, vs as a business. How tight will my economy be etc.
    morgage_loan = MortgageLoan(

    )

    job = Job(
        salary=53000
    )

    consultancy = ConsultancyBusiness(hourly_rate=750, internal_expenses=3000, allocation=1800 / 12)

    # agriculture_business = AgricultureBusiness()
    #
    expenses = CostOfLiving(
        20000
    )
    economic_situation = EconomicSituation(
        private_capital=50000
    )

    economy = PredictFutureEconomy(economic_situation, consultancy, expenses, morgage_loan)
    future_economy = economy.predict_future_economy(stop=2)
    print(future_economy)
