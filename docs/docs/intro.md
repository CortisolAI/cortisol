---
slug: /
title: What is Cortisol?
sidebar_position: 1
---

# Cortisol

![Cortisol](/img/cortisol_h_large.png)

Let's discover **Cortisol in less than 5 minutes**.

## What is Cortisol?

Cortisol is an open-source command-line tool designed specifically for web services. It offers easy-to-use cost estimation and forecasting capabilities tailored to main observability tools like [Datadog](https://www.datadoghq.com/), [New Relic](https://newrelic.com/), [Grafana](https://grafana.com/) and [GCP Cloud Logging](https://cloud.google.com/logging). Cortisol assists users in planning and optimizing their log costs before deploying their web services. It operates on a foundation inspired by [Locust](https://locust.io/), allowing users to define user behavior using a regular Python script 💰📉.

### How does it work?

Cortisol seamlessly harnesses the power of [Locust](https://locust.io/) for load testing. Users simply provide a standard Python script that outlines the anticipated user behavior on their web service. Cortisol, in turn, processes the load test's log file to project monthly log costs. It achieves this by referencing the public pricing figures of [Datadog](https://www.datadoghq.com/), [New Relic](https://newrelic.com/), [Grafana](https://grafana.com/) and [GCP Cloud Logging](https://cloud.google.com/logging).

### Name & Background

Picture this: the world of observability is brimming with fantastic tools like Grafana, Datadog, and New Relic. But here's the catch – costs can sneak up on you, catching you off guard or, worse, too late. And don't get us started on those log costs; they can go from "too little" to "what?!" in no time, even for the simplest web services. We wanted a tool that's right there in the thick of your software development workflow, because programming should always be a joyful ride.

In Cortisol, you define the behaviour of your users using Python code, much like you would in load testing scenarios. Various load testing scenarios result in logs of different sizes, leading to differing costs. Having this information beforehand can assist you in more effective budgeting and, potentially, in eliminating unnecessary log statements from your code.

Cortisol takes its name from the steroid hormone that helps our bodies respond to stress by increasing alertness, boosting energy, and regulating metabolism. It also plays a role in controlling blood sugar levels, reducing inflammation, and supporting the immune system. 

### Authors

- Dionysis Varelas ([@dvarelas](https://github.com/dvarelas) on Github)
- Pavlos Mitsoulis ([@pm330](https://github.com/pm3310) on Github)
- Narek Verdian ([@narek](https://www.linkedin.com/in/narek/) on LinkedIn)
