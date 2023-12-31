---
title: Configuration
sidebar_position: 4
---

## Configuration

### Log Cost Estimate

#### Name

Forecast log costs

#### Synopsis

    cortisol logs cost-estimate --host HOST --log-file LOG_FILE --users NUM_USERS --spawn-rate SPAWN_RATE --run-time RUN_TIME -cortisol-file CORTISOL_PYTHON_FILE

#### Description

Forecast log costs pre-production with Cortisol for [Datadog](https://www.datadoghq.com/), [New Relic](https://newrelic.com/), [Grafana](https://grafana.com/) and [GCP Cloud Logging](https://cloud.google.com/logging)

### Example

    cortisol logs cost-estimate --host http://10.20.31.32:8000 --users 100 --spawn-rate 30 --run-time 20m -cortisol-file some_cortisol_file.py

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
