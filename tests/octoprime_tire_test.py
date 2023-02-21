import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):

    def test_needs_service_returns_true_when_sum_of_wear_values_is_greater_than_or_equal_to_3(self):
        # arrange
        tire = OctoprimeTire([0.9, 0.8, 0.7, 0.6])

        # act
        result = tire.needs_service()

        # assert
        self.assertTrue(result)

    def test_needs_service_returns_false_when_sum_of_wear_values_is_less_than_3(self):
        # arrange
        tire = OctoprimeTire([0.2, 0.3, 0.4, 0.5])

        # act
        result = tire.needs_service()

        # assert
        self.assertFalse(result)

    def test_needs_service_returns_true_when_sum_of_wear_values_is_exactly_3(self):
        # arrange
        tire = OctoprimeTire([0.9, 0.6, 0.5, 1.0])

        # act
        result = tire.needs_service()

        # assert
        self.assertTrue(result)

    def test_needs_service_returns_false_when_wear_values_are_all_zero(self):
        # arrange
        tire = OctoprimeTire([0, 0, 0, 0])

        # act
        result = tire.needs_service()

        # assert
        self.assertFalse(result)

    def test_needs_service_returns_true_when_wear_values_are_all_one(self):
        # arrange
        tire = OctoprimeTire([1, 1, 1, 1])

        # act
        result = tire.needs_service()

        # assert
        self.assertTrue(result)

    def test_needs_service_returns_false_when_wear_values_are_empty(self):
        # arrange
        tire = OctoprimeTire([])

        # act
        result = tire.needs_service()

        # assert
        self.assertFalse(result)
