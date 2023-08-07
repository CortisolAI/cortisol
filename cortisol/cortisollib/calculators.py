def datadog_log_cost_calculator(
    size, n_retained_logs
):  # TODO: Cost estimator is a placeholder
    """
    Calculates the datadog log cost

    :param size: Log file size in GB
    :type size: Float
    :return: Log cost in dollars
    :rtype: Float
    """

    return size * 0.1


def grafana_log_cost_calculator(size):  # TODO: Cost estimator is a placeholder
    """
    Calculates the grafana log cost

    :param size: Log file size in GB
    :type size: Float
    :return: Log cost in dollars
    :rtype: Float
    """

    return size * 0.01


def new_relic_log_cost_calculator(logs_in_gb):
    """
    Calculate the estimated cost of logs in USD currency based on the given amount of logs in gigabytes,
    assuming the New Relic Pro Plan is chosen and ignoring the free tier.
    Args:
        logs_in_gb (float): The amount of logs in gigabytes.
    Returns:
        float: The estimated cost of the logs in USD currency for the New Relic Pro Plan.
    Example:
        >>> new_relic_log_cost(120)
        36.0
    Note:
        The return value is calculated based on the pricing of the New Relic Pro Plan and does not consider the free tier.
    """
    return logs_in_gb * 0.3


def format_bytes(file_size):
    """
    Converts file size from Bytes to GB

    :param file_size: file size in bytes
    :type file_size: Float
    :return: File size in GB
    :rtype: Float
    """
    k = 1024
    file_size_in_gb = file_size / k**3  # Directly convert to GB (1024^3)
    return file_size_in_gb
