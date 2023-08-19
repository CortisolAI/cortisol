def datadog_log_cost_calculator(logs_in_gb, log_events_in_million):
    """
    Calculate the estimated annual cost of logging using Datadog, including any free tier.

    This function calculates the estimated annual cost of logging using the Datadog platform,
    considering the amount of data logs in gigabytes and the number of log events in millions.

    Args:
        logs_in_gb (float): Amount of data logs in gigabytes.
        log_events_in_million (int): Number of log events in millions.

    Returns:
        float: Estimated annual cost of logging in USD for log ingestion plus log retention/storage.

    Note:
        The estimated cost is returned based on the assumption that the Datadog Pro Plan is chosen, billed annually and a 30 day retention is chosen.
    """
    cost_per_gb = logs_in_gb * 0.1
    cost_per_event_million = log_events_in_million * 2.5
    return cost_per_gb + cost_per_event_million


def grafana_log_cost_calculator(logs_in_gb):
    """
    Calculate the estimated cost of logs in USD currency based on the given amount of logs in gigabytes,
    assuming the Grafana Cloud Pro Plan is chosen and including the free tier.

    Args:
        logs_in_gb (float): The amount of logs in gigabytes.

    Returns:
        float: The estimated cost of the logs in USD currency for the Grafana Cloud Pro Plan.

    Example:
        >>> grafana_log_cost_calculator(100)
        50.0

    Note:
        The return value is calculated based on the pricing of the Grafana Cloud Pro Plan and does consider the free tier.
    """
    if logs_in_gb <= 100:
        return 0.0

    return (logs_in_gb - 100.0) * 0.5


def new_relic_log_cost_calculator(logs_in_gb):
    """
    Calculate the estimated cost of logs in USD currency based on the given amount of logs in gigabytes,
    assuming the New Relic Pro Plan is chosen and including the free tier.
    Args:
        logs_in_gb (float): The amount of logs in gigabytes.
    Returns:
        float: The estimated cost of the logs in USD currency for the New Relic Pro Plan.
    Example:
        >>> new_relic_log_cost_calculator(120)
        36.0
    Note:
        The return value is calculated based on the pricing of the New Relic Pro Plan and does consider the free tier.
    """
    if logs_in_gb <= 100:
        return 0.0
    return (logs_in_gb - 100.0) * 0.3


def format_bytes(file_size):
    """
    Converts file size from Bytes to GB

    Args:
        file_size (float): file size in bytes
    Returns:
        float: File size in GB
    """
    k = 1024
    file_size_in_gb = file_size / k**3  # Directly convert to GB (1024^3)
    return file_size_in_gb


def gcp_cloud_logging_log_cost_calculator(logs_in_gb):
    """
    Calculate the estimated annual cost of logging using GCP Cloud Logging, including the free tier.
    This function calculates the estimated annual cost of logging using the Cloud Logging platform,
    considering the amount of data logs in gigabytes.
    Args:
        logs_in_gb (float): Amount of data logs in gigabytes.
    Returns:
        float: Estimated annual cost of logging in USD for log ingestion plus log retention/storage.
    Note:
        The estimated cost is returned based on the assumption that logs are going to be retainted more than 30 days.
        No cost is incurred with default retention period https://cloud.google.com/logging/quotas#logs_retention_periods.
        Google Commitment Agreement is not taken into account.
    """
    if logs_in_gb <= 50:
        return logs_in_gb * 0.01

    return (logs_in_gb - 50.0) * 0.5 + logs_in_gb * 0.01
