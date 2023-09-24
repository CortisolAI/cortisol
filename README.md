![Cortisol](docs/cortisol_h_large.png#gh-light-mode-only)
![Cortisol](docs/cortisol_h_large_w.png#gh-dark-mode-only)

<p align="center">
    <em>Cortisol, accurately forecast log costs pre-production.</em>
</p>
<p align="center">
<a href="https://github.com/cortisolai/cortisol/actions?query=workflow%3ACI" target="_blank">
    <img src="https://github.com/cortisolai/cortisol/workflows/CI/badge.svg" alt="Test">
</a>
</p>

# cortisol

Cortisol is an open-source command-line tool designed specifically for web services. It offers easy-to-use cost estimation and forecasting capabilities tailored to main observability tools like [Datadog](https://www.datadoghq.com/), [New Relic](https://newrelic.com/), [Grafana](https://grafana.com/) and [GCP Cloud Logging](https://cloud.google.com/logging). Cortisol assists users in planning and optimizing their log costs before deploying their web services. It operates on a foundation inspired by [Locust](https://locust.io/), allowing users to define user behavior using a regular Python script 💰📉.

For detailed reference to Cortisol commands please go to: [Read the Docs](https://cortisolai.github.io/cortisol/)

## Installation

### Prerequisites

Cortisol requires one of the following Python versions: 3.8, 3.9, 3.10 or 3.11

### Install cortisol

At the command line:

    pip install cortisol

If you have an Apple M1 CPU, we suggest installing using Poetry as a dependency management. Otherwise, the underline gevent library may not work.

## Getting started

First things first! We need a RESTful service and so you'll need to do the following steps:

1. Clone this example repo https://github.com/CortisolAI/getting-started-example
2. `cd getting-started-example`
3. `mkvirtualenv getting-started-cortisol`
4. `python -m app.main` which will make the service available at `http://127.0.0.1:8080/`

And, now, it's time to create your first cortisol file. Copy and paste the following in a file named `cortisolfile.py`:

```python
from locust import task

from cortisol.cortisollib.users import CortisolHttpUser


class WebsiteUser(CortisolHttpUser):
    @task
    def my_task(self):
        self.client.get("/")

```

Go to the virtualenv where the cortisol library is installed and run the following command in the terminal. Make sure to change the base path for the `--log-file` argument:

```terminal
cortisol logs cost-estimate --host http://127.0.0.1:8080 --users 10 --spawn-rate 5 --run-time 10s --cortisol-file cortisolfile.py --log-file /some/path/getting-started-example/cortisol_app.log
```

## Commands

### Log Cost Estimate

#### Name

Forecast log costs

#### Synopsis

    cortisol logs cost-estimate --host HOST --log-file LOG_FILE --users NUM_USERS --spawn-rate SPAWN_RATE --run-time RUN_TIME -cortisol-file CORTISOL_PYTHON_FILE

#### Description

Forecast log costs pre-production with Cortisol for Datadog, New Relic, and Grafana

### Example

    cortisol logs cost-estimate --host http://10.20.31.32:8000 --users 10 --spawn-rate 5 --run-time 10s --cortisol-file ./examples/cortisolfile.py --log-file /app/playground_app.log

#### Required Flags - Option 1

`-f, --cortisol-file PATH`      Path to the CORTISOL_FILE

`-h, --host TEXT`               Host in the following format: http://10.20.31.32 or http://10.20.31.32:8000

`-l, --log-file PATH`           Path to log file

`-u, --users INTEGER`           Peak number of concurrent users

`-r, --spawn-rate INTEGER`      Rate to spawn users at (users per second)

`-t, --run-time TEXT`           Stop after the specified amount of time, e.g. (50, 30s, 200m, 5h, 2h30m, etc.). Default unit in seconds.

#### Required Flags - Option 2

All the latter options plus the following in case your application run in a Docker container:

`-c, --container-id TEXT`      Optional docker container id where your application runs

##### Example
    cortisol logs cost-estimate --host http://127.0.0.1:8080 --users 100 --spawn-rate 5 --run-time 10s --cortisol-file ./examples/cortisolfile.py --log-file /app/playground_app.log --container-id 1212aa67e530af75b3310e1e5b30261b36844a6748df1d321088c4d48a20ebd0


#### Required Flags - Option 3

`--config PATH`                 Path to config file (YAML or JSON) containing the long version of flags from option 1

#### Optional Flags

`--stats-file PATH`             Path where to store the cortisol statistics output as a csv

Here's a YAML example:

```YAML
host: "http://10.20.31.32:8000"
log-file: "/path/to/logfile"
users: 100
spawn-rate: 30
run-time: "20m"
cortisol-file: "some_cortisol_file.py"
stats-file: "cortisol_stats.csv"
```

Here's a YAML example with docker container id:

```YAML
host: "http://10.20.31.32:8000"
log-file: "/path/to/logfile"
users: 100
spawn-rate: 30
run-time: "20m"
cortisol-file: "some_cortisol_file.py"
container-id: "80f1bc1e7feb"
stats-file: "cortisol_stats.csv"
```

and a JSON example:

```JSON
{
  "host": "http://10.20.31.32:8000",
  "log_file": "/path/to/logfile",
  "users": 100,
  "spawn_rate": 30,
  "run_time": "20m",
  "cortisol_file": "some_cortisol_file.py",
  "container_id": "80f1bc1e7feb",
  "stats-file": "cortisol_stats.csv"
}
```
