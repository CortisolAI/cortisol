---
title: How-to guides
sidebar_position: 7
---

## Estimating log costs from stdout and stderr streams

Often, we find ourselves using software like [fluent-bit](https://fluentbit.io/) to capture the stdout and stderr of
our applications and forward them directly to our chosen observability provider.
Many cloud providers offer this functionality as part of their managed Kubernetes offerings.
When you use such a setup, you might not specify a file to store your logs within your logger.
But fear not, with cortisol, you can still easily estimate the cost of these logs. Here's how you can do it!

### Local service

Assuming that you're already familiar with our [Your first log cost estimation guide](./getting-started.md/#your-first-log-cost-estimation),
 the only change you need to make is to redirect the stdout and stderr streams to a file of your choice.

You can do this with a simple command:
```
python -m app.main >> /path/to/my_redirected_logs.log
```

Once you've done this, you can use cortisol just as you normally would:

```terminal
cortisol logs cost-estimate --host http://127.0.0.1:8080 --users 10 --spawn-rate 5 --run-time 10s --cortisol-file cortisolfile.py --cortisol-file ./examples/cortisolfile.py --log-file /path/to/my_redirected_logs.log
```

### Local service with docker

If you're already familiar with our [Your first log cost estimation with docker guide](./getting-started.md/#your-first-log-cost-estimation-with-docker),
the only change you need to make is to redirect the stdout and stderr streams from your Docker container to a file outside of it.

Here's how you can do it:
1. First, make sure you have the Docker CLI installed.

2. Open a new terminal and run the following command, replacing the `container-id` with your own:
```terminal
docker logs -f {container-id} >> /path/to/my_redirected_logs.log
```
2. Now, run cortisol as usual:
```terminal
cortisol logs cost-estimate --host http://127.0.0.1:8080 --users 10 --spawn-rate 5 --run-time 10s --cortisol-file cortisolfile.py --cortisol-file ./examples/cortisolfile.py --log-file /path/to/my_redirected_logs.log
```
There's no need to specify a `container-id` in the `cost-estimate` command because the log file is outside of the container. Enjoy easy log cost estimation with cortisol!