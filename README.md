![Cortisol](docs/cortisol_h_large.png#gh-light-mode-only)
![Cortisol](docs/cortisol_h_large_w.png#gh-dark-mode-only)

<p align="center">
    <em>Cortisol, accurately forecast log costs pre-production.</em>
</p>

# cortisol

A command-line tool that provides cost estimation and forecasting for main observability tools like [Datadog](https://www.datadoghq.com/), [New Relic](https://newrelic.com/), and [Grafana](https://grafana.com/), helping users plan and optimize their log, metric and trace costs pre-production.

For detailed reference to Cortisol commands please go to: [Read the Docs](TODO)

## Installation

### Prerequisites

cortisol requires the following one of the following Python versions: 3.8, 3.9, 3.10 or 3.11

### Install cortisol

At the command line:

    pip install cortisol

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

Here's a YAML example:

```YAML
host: "http://10.20.31.32:8000"
log-file: "/path/to/logfile"
users: 100
spawn-rate: 30
run-time: "20m"
cortisol-file: "some_cortisol_file.py"
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
  "container_id": "80f1bc1e7feb"
}
```
