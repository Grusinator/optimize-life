import logging

from shapely.geometry import Point

logger = logging.getLogger(__name__)


class Job:
    def __init__(self, location: Point, monthly_salary: int, weeks_of_vacation: int = 6):
        self.location = location
        self.monthly_salary = monthly_salary
        self.weeks_of_vacation = weeks_of_vacation
        self.average_work_days_pr_month = 20

    def monthly_commute_time(self, home_location: Point, commute_days_pr_week=5):
        #  https://cloud.google.com/maps-platform/pricing?hl=da
        distance = self.location.distance(home_location)
        time_spent_pr_day = distance / 60 * 2  # 60 km/h back and forth
        monthly_commute_time = time_spent_pr_day * self.average_work_days_pr_month * commute_days_pr_week / 5
        logger.info(f"monthly commute time: {monthly_commute_time:.1f}")
        return monthly_commute_time

    def monthly_commute_income_loss(self, home_location: Point):
        monthly_commute_time = self.monthly_commute_time(home_location)
        monthly_commute_income_loss = monthly_commute_time * self.hourly_rate()
        logger.info(f"monthly commute income loss: {monthly_commute_income_loss:.0f}")
        return monthly_commute_income_loss

    def salary_after_tax(self):
        salary_after_tax = self.monthly_salary * 0.6
        logger.info(f"salary after tax: {salary_after_tax:.0f}")
        return salary_after_tax

    def hourly_rate(self):
        return self.salary_after_tax() / 160
