from economic_iterators.job import Job
from predict_future_economy import predict_future_economy


def test_job_economy():
    job = Job(
        salary=50000
    )
    future_economy = predict_future_economy(job, stop=2)
    assert future_economy == 100000
