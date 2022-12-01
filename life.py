import logging

from house import House
from job_location import Job

logger = logging.getLogger(__name__)


class Life:
    def __init__(self, house: House, job: Job):
        self.house = house
        self.job = job

    def life_monthly_value(self):
        logger.info(f"calculating life for house: {self.house.price:.0f}")
        commute_loss = self.job.monthly_commute_income_loss(self.house.location)
        monthly_expenses = self.house.monthly_expences()
        salary = self.job.salary_after_tax()
        life_monthly_value = salary - monthly_expenses - commute_loss
        logger.info(f"life monthly value: {life_monthly_value}")
