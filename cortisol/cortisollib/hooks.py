from time import time
from prettytable import PrettyTable

from cortisol.cortisollib.readers import log_file_size_reader
from cortisol.cortisollib.calculators import (
    datadog_log_cost_calculator,
    grafana_log_cost_calculator,
    format_bytes,
)


def colorize(value, key):
    colors = {
        "log-volume": "#FFFFFF",
        "datadog-cost": "#774aa4",
        "grafana-cost": "#ffa500",
    }
    hex_color = colors[key]
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:8], 16)
    color = f"38;2;{r};{g};{b}"
    return f"\033[{color}m{value}\033[0m"


def add_symbol(key, value):
    symbols = {
        "log-volume": f"{round(value, 2)} GiB",
        "datadog-cost": f"${round(value, 2)}",
        "grafana-cost": f"${round(value, 2)}",
    }
    symbol = symbols[key]
    return symbol


def create_results_table(obs_stats):
    table = PrettyTable()
    table.field_names = ["Name", "Value"]
    # Add data to the table with color
    for key, value in obs_stats[list(obs_stats.keys())[0]].items():
        table.add_row([colorize(key, key), colorize(add_symbol(key, value), key)])

    # Set the formatting options
    table.align = "l"  # Left-align columns
    table.border = True  # Add borders to the table
    table._min_width = {"Name": 50, "Value": 25}
    return table


def on_quit(environment, **kwargs):
    print("Observability Statistics")
    obs_stats = environment.runner.stats.custom_stats
    print(f"*----{list(obs_stats.keys())[0].upper()}----*")
    # Create a PrettyTable instance
    table = create_results_table(obs_stats)
    print(table)


stats = {}


def on_init(environment, **kwargs):
    environment.runner.stats.custom_stats = stats


def on_request(
    request_type, name, response_time, response_length, exception, context, **kwargs
):
    """
    Event handler that get triggered on every request
    """
    stats.setdefault("logs", {"log-volume": 0, "datadog-cost": 0, "grafana-cost": 0})

    log_file = context["log_file"]
    container_id = context["container_id"]
    start_time = context["start_time"]
    initial_log_volume = context["initial_log_volume"]
    file_size = log_file_size_reader(log_file, container_id) - initial_log_volume
    formatted_file_size = format_bytes(file_size)
    current_time = time()
    elapsed_time_in_seconds = (current_time - start_time) / 1000
    extrapolated_size = (2592000.0 * formatted_file_size) / elapsed_time_in_seconds
    datadog_cost = datadog_log_cost_calculator(extrapolated_size)
    grafana_cost = grafana_log_cost_calculator(extrapolated_size)

    stats["logs"]["log-volume"] = extrapolated_size
    stats["logs"]["datadog-cost"] = datadog_cost
    stats["logs"]["grafana-cost"] = grafana_cost
