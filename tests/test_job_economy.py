from economic_iterators.job import Job
from economic_situation import EconomicSituation
from predict_future_economy import PredictFutureEconomy


def test_job_economy():
    job = Job(salary=50000)
    future_economy = PredictFutureEconomy(EconomicSituation(0), job).predict_future_economy()
    assert future_economy.private_capital == 346800
