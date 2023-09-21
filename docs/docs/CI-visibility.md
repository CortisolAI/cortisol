---
title: Continuous Integration Visibility
sidebar_position: 6
---

## Continuous Integration Visibility

Streamline your CI/CD pipelines with detailed visibility into your expected log costs.

There are examples below on how to enable Cortisol in your CI/CD pipeline.

## Cortisol as a Github Action

For more information about Github Action, please refer [here](https://github.com/features/actions).

Let's suppose that you want to run Cortisol as a step in a Github action for this FastAPI [repository](https://github.com/CortisolAI/getting-started-example).

It's very simple! 

1. Fork this [repository](https://github.com/CortisolAI/getting-started-example) 
2. Create a file named `cortisolfile.py` at the root of the repository with the following content:
```Python
from locust import task

from cortisol.cortisollib.users import CortisolHttpUser


class WebsiteUser(CortisolHttpUser):
    @task
    def my_task(self):
        self.client.get("/")
```
3. Create a file named `my_config.yaml` at the root of the repository with the following content:
```YAML
host: "http://127.0.0.1:8080"
log-file: "cortisol_app.log"
users: 10
spawn-rate: 5
run-time: "10s"
cortisol-file: "cortisolfile.py"
```
4. Create in this repository the following path `.github/workflows/`
5. Save under `.github/workflows/` a file named `main.yml` with the following content:

```YAML
name: Main Workflow

on:
  push:
    branches:
      - main  # Replace with the branch you want to trigger on

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2  

    - name: Set up Python  # Replace with your desired programming language.
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"  # Replace with your desired Python version.

    - name: Install Dependencies  # Replace with your desired dependency management tool.
      run: |
        pip install -r requirements.txt

    - name: Run FastAPI Server in the background
      run: |
        nohup python -m app.main &

    - name: Verify server is running
      run: |
        curl http://127.0.0.1:8080

    - name: Cortisol log costs pre-production
      run: |
        cortisol logs cost-estimate --config my_config.yaml
```
6. Push the code changes to your `main` branch.
7. You should see in the Actions tab of your forked repository this action being in progress. Click on it. Once it's finished you should something like that:

![GH-Action](/img/gh-action-cortisol.png)

Let's explain the steps in this Github Action workflow:

1. **Checkout Repository**: This step checks out the source code repository into the runner's workspace. It uses the `actions/checkout` action with version `v2`.
2. **Set up Python**: This step sets up the Python environment on the runner. It specifies the desired Python version, which is version `3.10` in this case.
3. **Install Dependencies**: This step installs Python dependencies from a `requirements.txt` file using the `pip` package manager. The `requirements.txt` file contains the `cortisol` library.
4. **Run FastAPI Server in the background**: This step starts a FastAPI server in the background. The nohup command allows the server to keep running after this step is completed and, more importantly, it doesn't block the entire Github Action.
5. **Verify server is running**: This step uses `curl` to make an HTTP request to the FastAPI server to verify that it is running and responsive.
6. **Cortisol log costs pre-production**: This step runs Cortisol with the arguments `logs cost-estimate --config my_config.yaml`. It estimates log costs pre-production.
