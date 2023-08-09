import unittest

from cortisol.cortisollib.estimators import linear_extrapolator


class TestLinearExtrapolator(unittest.TestCase):
    def test_extrapolation(self):
        value_to_extrapolate = 1000
        test_run_time = 3600  # 1 hour in seconds
        expected_extrapolated_value = (2592000.0 * value_to_extrapolate) / test_run_time

        extrapolated_value = linear_extrapolator(value_to_extrapolate, test_run_time)
        self.assertAlmostEqual(
            extrapolated_value,
            expected_extrapolated_value,
            places=10,
            msg="Extrapolation result is not as expected",
        )
