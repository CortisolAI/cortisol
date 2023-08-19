import unittest
from cortisol.cortisollib.calculators import (
    datadog_log_cost_calculator,
    grafana_log_cost_calculator,
    new_relic_log_cost_calculator,
    gcp_cloud_logging_log_cost_calculator,
    format_bytes,
)


class TestLogCostCalculators(unittest.TestCase):
    def test_datadog_log_cost_calculator(self):
        size_gb = 5.0
        expected_cost = size_gb * 0.1
        n_retained_logs = 0.0
        self.assertEqual(
            datadog_log_cost_calculator(size_gb, n_retained_logs), expected_cost
        )

    def test_grafana_log_cost_calculator(self):
        size_gb = 103.0
        expected_cost = (size_gb - 100.0) * 0.5
        self.assertEqual(grafana_log_cost_calculator(size_gb), expected_cost)

    def test_new_log_log_cost_calculator(self):
        size_gb = 103.0
        expected_cost = (size_gb - 100.0) * 0.3
        self.assertEqual(new_relic_log_cost_calculator(size_gb), expected_cost)

    def test_gcp_cloud_logging_log_cost_calculator(self):
        size_gb = 103.0
        expected_cost = (size_gb - 50.0) * 0.5 + size_gb * 0.01
        self.assertEqual(gcp_cloud_logging_log_cost_calculator(size_gb), expected_cost)

    def test_format_bytes(self):
        file_size_bytes = 2147483648  # 2 GB in bytes
        expected_size_gb = 2.0
        result = format_bytes(file_size_bytes)
        self.assertEqual(expected_size_gb, result)

    def test_datadog_log_cost_calculator_zero_size(self):
        size_gb = 0.0
        n_retained_logs = 0.0
        expected_cost = 0.0
        self.assertEqual(
            datadog_log_cost_calculator(size_gb, n_retained_logs), expected_cost
        )

    def test_format_bytes_large_size(self):
        file_size_bytes = 128 * 1024**5  # 128 TB in bytes
        expected_size_gb = 128 * 1024**2
        result = format_bytes(file_size_bytes)
        print(result)
        print(expected_size_gb)
        self.assertEqual(expected_size_gb, result)
