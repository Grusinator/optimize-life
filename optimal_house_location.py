import logging

from house import House
from job import Job
from shapely.geometry import Point

from life import Life

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
for not_interested in ("azure", "uamqp", " urllib3"):
    logging.getLogger(not_interested).setLevel(logging.WARN)
# create console handler with a higher log level
log_stream = logging.StreamHandler()
log_stream.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(message)s')
log_stream.setFormatter(formatter)
logger.addHandler(log_stream)


def calculate_total_cost(house: House, job: Job):
    commute_loss = job.monthly_commute_income_loss(house.location)

    monthly_expenses = house.monthly_expences()
    salary = job.salary_after_tax()
    return salary - monthly_expenses - commute_loss


if __name__ == "__main__":
    job = Job(Point(0, 0), 40000)
    house1 = House(4000000, Point(0, 30))
    house2 = House(2000000, Point(0, 60))

    Life(house1, job).life_monthly_value()
    Life(house2, job).life_monthly_value()
