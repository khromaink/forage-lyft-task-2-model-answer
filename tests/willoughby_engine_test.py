import unittest
from engine.willoughby_engine import WilloughbyEngine
from datetime import datetime


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_mileage = 100000
        current_mileage = 160001
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_service_mileage = 100000
        current_mileage = 150000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_same_mileage(self):
        last_service_mileage = 130000
        current_mileage = 130000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_one_mileage_before(self):
        last_service_mileage = 100000
        current_mileage = 159999
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_by_today(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_one_mileage_before(self):
        last_service_mileage = 100000
        current_mileage = 159999
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    if __name__ == '__main__':
        unittest.main()
