import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire1 = CarriganTire([0.8, 0.9, 0.95])
        self.assertTrue(tire1.needs_service())

        tire2 = CarriganTire([0.9, 0.9, 0.9])
        self.assertTrue(tire2.needs_service())

    def test_needs_service_false(self):
        tire1 = CarriganTire([0.7, 0.8, 0.85])
        self.assertFalse(tire1.needs_service())

        tire2 = CarriganTire([0.7, 0.8, 0.9])
        self.assertTrue(tire2.needs_service())


if __name__ == '__main__':
    unittest.main()
