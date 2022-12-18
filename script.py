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
        amount=5000000, interest=0.05, kurs=100, payment=100000
    )

    job = Job(
        salary=53000
    )

    consultancy = ConsultancyBusiness(hourly_rate=750, internal_expenses=3000, allocation=1800 / 12)

    # agriculture_business = AgricultureBusiness()
    #
    cost_of_living = CostOfLiving(
        200
    )
    economic_situation = EconomicSituation(
        private_capital=500000
    )

    economy = PredictFutureEconomy(economic_situation, consultancy, cost_of_living, mortgage_loan)
    future_economy = economy.predict_future_economy(stop=2)
    print(future_economy)
