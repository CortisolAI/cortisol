def datadog_log_cost_calculator(size):  # TODO: Cost estimator is a placeholder
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
