from time import time
from prettytable import PrettyTable

from cortisol.cortisollib.readers import log_file_size_reader, count_log_entries
from cortisol.cortisollib.estimators import linear_extrapolator
from cortisol.cortisollib.calculators import (
    datadog_log_cost_calculator,
    grafana_log_cost_calculator,
    new_relic_log_cost_calculator,
    gcp_cloud_logging_log_cost_calculator,
    format_bytes,
)


def colorize(value, key):
    """
    Apply color formatting to a value based on a specified key.

    This function takes a value and a key as input, and applies color formatting
    to the value based on the provided key. The colors dictionary contains hex color
    codes for different keys. The value is formatted using ANSI escape codes for
    terminal color output.

    Args:
        value (str): The value to be colorized.
        key (str): The key associated with a specific color in the colors dictionary.

    Returns:
        str: The colorized value with ANSI escape codes for color.

    Example:
        formatted_value = colorize("Some Text", "log-volume")
        print(formatted_value)
    """
    colors = {
        "log-volume": "#FFFFFF",
        "datadog-cost": "#774aa4",
        "grafana-cost": "#ffa500",
        "new-relic-cost": "#1CE783",
        "gcp-cloud-logging-cost": "#4285F4",
    }
    hex_color = colors[key]
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:8], 16)
    color = f"38;2;{r};{g};{b}"
    return f"\033[{color}m{value}\033[0m"


def add_symbol(key, value):
    """
    Add a symbol or unit to a numeric value based on a specified key.

    This function takes a key and a numeric value as input and adds a corresponding
    symbol or unit to the value based on the provided key. The symbols dictionary
    contains symbols or units for different keys.

    Args:
        key (str): The key associated with a specific symbol or unit in the symbols dictionary.
        value (float): The numeric value to which the symbol or unit should be added.

    Returns:
        str: The value with the symbol or unit added.

    Example:
        formatted_value = add_symbol("log-volume", 150)
        print(formatted_value)
    """
    symbols = {
        "log-volume": f"{round(value, 2)} GiB",
        "datadog-cost": f"${round(value, 2)}",
        "grafana-cost": f"${round(value, 2)}",
        "new-relic-cost": f"${round(value, 2)}",
        "gcp-cloud-logging-cost": f"${round(value, 2)}",
    }
    symbol = symbols[key]
    return symbol


def create_results_table(obs_stats):
    """
    Create a formatted results table with colored and symbolized data.

    This function generates a PrettyTable object and populates it with data from
    the 'obs_stats' dictionary. The table displays the data with colored names and
    symbolized values based on the keys in the dictionary.

    Args:
        obs_stats (dict): A dictionary containing observed statistics.

    Returns:
        PrettyTable: A formatted table displaying the observed statistics.

    Example:
        observed_stats = {
            "log-volume": {"Average": 150.5, "Max": 200},
            "datadog-cost": {"Total": 350.25},
            "grafana-cost": {"Total": 80},
        }
        result_table = create_results_table(observed_stats)
        print(result_table)
    """
    table = PrettyTable()
    table.field_names = ["Name", "Value"]
    # Add data to the table with color
    for key, value in obs_stats["logs"].items():
        table.add_row([colorize(key, key), colorize(add_symbol(key, value), key)])

    # Set the formatting options
    table.align = "l"  # Left-align columns
    table.border = True  # Add borders to the table
    table._min_width = {"Name": 50, "Value": 25}
    return table


def on_quit(environment, **kwargs):
    """
    Display observability statistics using a formatted PrettyTable.

    This function is called when the Locust test is completed or interrupted.
    It prints the observability statistics in a formatted table using PrettyTable.

    Args:
        environment (Environment): The Locust environment object.
        **kwargs: Additional keyword arguments.

    Example:
        from locust import Environment, HttpUser, task, events
        from my_locust_file import on_quit

        env = Environment(user_classes=[HttpUser])
        env.events.quitting += on_quit
        env.create_user(HttpUser, "http://example.com")
        env.runner.start(1, hatch_rate=1)
    """
    obs_stats = environment.runner.stats.custom_stats
    print(f"Cortisol sent {obs_stats['n_requests']} requests to your service")
    print("\n")
    print("Observability Statistics")
    print(f"*----LOGS----*")
    # Create a PrettyTable instance
    table = create_results_table(obs_stats)
    print(table)
    return table


stats = {}


def on_init(environment, **kwargs):
    """
    Initialize custom statistics for the Locust environment.

    This function is called during the initialization of the Locust environment.
    It sets up custom statistics for the environment's runner.

    Args:
        environment (Environment): The Locust environment object.
        **kwargs: Additional keyword arguments.

    Example:
        from locust import Environment, HttpUser, task, events
        from my_locust_file import on_init

        env = Environment(user_classes=[HttpUser])
        env.events.init += on_init
        env.create_user(HttpUser, "http://example.com")
        env.runner.start(1, hatch_rate=1)
    """
    environment.runner.stats.custom_stats = stats


def on_request(
    request_type, name, response_time, response_length, exception, context, **kwargs
):
    """
    Calculate and update custom observability statistics during a request.

    This function is called for each request made during a Locust load test. It calculates
    and updates custom observability statistics related to log volume, Datadog cost, and Grafana cost.

    Args:
        request_type (str): Type of the HTTP request (GET, POST, etc.).
        name (str): Name of the request.
        response_time (float): Response time of the request in milliseconds.
        response_length (int): Length of the response in bytes.
        exception (Exception or None): Exception raised during the request, if any.
        context (dict): Contextual information related to the request.
        **kwargs: Additional keyword arguments.

    Example:
        from locust import task, events
        from my_locust_file import on_request

    @task
    def my_task(self):
        with self.client.get("/endpoint", catch_response=True) as response:
            if response.status_code == 200:
                events.request_success.fire(
                    request_type="GET",
                    name="my_task",
                    response_time=response.elapsed.total_seconds() * 1000,
                    response_length=len(response.content),
                    exception=None,
                    context={
                        "log_file": "path/to/log_file.log",
                        "container_id": "my-container",
                        "start_time": time(),
                        "initial_log_volume": 0,
                    },
                )
            else:
                events.request_failure.fire(
                    request_type="GET",
                    name="my_task",
                    response_time=response.elapsed.total_seconds() * 1000,
                    exception=None,
                    context={
                        "log_file": "path/to/log_file.log",
                        "container_id": "my-container",
                        "start_time": time(),
                        "initial_log_volume": 0,
                    },
                )

    self.environment.events.request.fire = on_request
    """
    stats.setdefault(
        "logs",
        {
            "log-volume": 0,
            "datadog-cost": 0,
            "grafana-cost": 0,
            "new-relic-cost": 0,
            "gcp-cloud-logging-cost": 0,
        },
    )
    stats.setdefault("n_requests", 0)

    log_file = context["log_file"]
    container_id = context["container_id"]
    start_time = context["start_time"]
    initial_log_volume = context["initial_log_volume"]
    initial_log_entries = context["initial_log_entries"]
    file_size = log_file_size_reader(log_file, container_id) - initial_log_volume
    num_log_entries = count_log_entries(log_file, container_id) - initial_log_entries
    formatted_file_size = format_bytes(file_size)
    current_time = time()
    elapsed_time_in_seconds = (current_time - start_time) / 1000
    extrapolated_size = linear_extrapolator(
        formatted_file_size, elapsed_time_in_seconds
    )
    extrapolated_num_log_entries = (
        linear_extrapolator(num_log_entries, elapsed_time_in_seconds) / 30
    )
    datadog_cost = datadog_log_cost_calculator(
        extrapolated_size, extrapolated_num_log_entries
    )
    grafana_cost = grafana_log_cost_calculator(extrapolated_size)
    new_relic_cost = new_relic_log_cost_calculator(extrapolated_size)
    gcp_cost = gcp_cloud_logging_log_cost_calculator(extrapolated_size)

    stats["logs"]["log-volume"] = extrapolated_size
    stats["logs"]["datadog-cost"] = datadog_cost
    stats["logs"]["grafana-cost"] = grafana_cost
    stats["logs"]["new-relic-cost"] = new_relic_cost
    stats["logs"]["gcp-cloud-logging-cost"] = gcp_cost
    stats["n_requests"] += 1

    return stats
