import unittest
from engine.capulet_engine import CapuletEngine
from datetime import datetime


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_mileage = 100000
        current_mileage = 130001
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        last_service_mileage = 100000
        current_mileage = 120000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_same_mileage(self):
        last_service_mileage = 100000
        current_mileage = 100000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_one_mileage_before(self):
        last_service_mileage = 100000
        current_mileage = 129999
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_by_today(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_one_mileage_before(self):
        last_service_mileage = 100000
        current_mileage = 129999
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    if __name__ == '__main__':
        unittest.main()
