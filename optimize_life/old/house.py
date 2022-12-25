import logging

from shapely.geometry import Point

logger = logging.getLogger(__name__)


class House:
    def __init__(self, price: int, location: Point):
        self.price = price
        self.location = location

    def monthly_expences(self):
        monthly_expences = self.price / 1000000 * 5000  # 5k pr million
        logger.info(f"monthly expenses: {monthly_expences:.0f}")
        return monthly_expences
