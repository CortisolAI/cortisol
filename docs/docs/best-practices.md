---
title: Best practices
sidebar_position: 5
---

## Best practices

Here are three best practices to follow when using Cortisol:

1. Cortisol uses the volume of the logged data from the run to project and approximate
its value over a month using linear extrapolation. To obtain a precise estimation,
it's essential to set the `--run-time` to an adequate duration.
The `--spawn-rate` influences `--run-time`,
as a higher rate of user spawning results in a shorter `--run-time`.

2. Create scenarios that accurately replicate the user actions or API calls
that generate log entries. If certain actions trigger specific log types or levels,
ensure your cortisolfile defines those actions accordingly.
The goal is to generate log entries in a way that mirrors real-world usage.

3. Gradually vary the intensity of the load during testing to observe how the volume of logs changes.
Start with a lower load and increase it step by step. This will help you identify thresholds
where log volume might start to spike significantly or where certain log types become more frequent.