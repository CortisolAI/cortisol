def linear_extrapolator(value: float, run_time: float):
    """
    Linearly extrapolate a value over a specific run time.

    This function extrapolates a given value over a specified run time of one month (30 days).
    The extrapolated value is calculated by dividing the given value by the run time in seconds,
    and then multiplying it by the total number of seconds in 30 days (2592000 seconds).

    Args:
        value (float): The value to be extrapolated.
        run_time (float): The duration of the run time in seconds.

    Returns:
        float: The extrapolated value over the specified run time.

    Example:
        value_to_extrapolate = 1000
        test_run_time = 3600  # 1 hour in seconds
        extrapolated_value = linear_extrapolator(value_to_extrapolate, test_run_time)
    """
    extrapolated_value = (2592000.0 * value) / run_time
    return extrapolated_value
