import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
import unittest

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2025, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2023, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_same_date(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2024, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_one_day_before(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2024, 12, 31)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_by_today(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_one_year_before(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2023, 12, 31)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
