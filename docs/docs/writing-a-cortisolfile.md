---
title: Writing a cortisolfile
sidebar_position: 3
---

## Writing a cortisolfile

Cortisol has been inspired by [Locust](https://docs.locust.io/en/stable/writing-a-locustfile.html) on defining the behaviour of users.

In fact, there is only one difference between a cortisol file and a locust file. The user defined class in the cortisol file must extend the `CortisolHttpUser`. The rest is exactly the same.

Let's look at a realistic example that is slightly modified from the original [Locust example](https://docs.locust.io/en/stable/writing-a-locustfile.html).

```python
    import time
    from cortisol.cortisollib.users import CortisolHttpUser
    from locust import task, between

    class QuickstartUser(CortisolHttpUser):
        wait_time = between(1, 5)

        @task
        def hello_world(self):
            self.client.get("/hello")
            self.client.get("/world")

        @task(3)
        def view_items(self):
            for item_id in range(10):
                self.client.get(f"/item?id={item_id}", name="/item")
                time.sleep(1)

        def on_start(self):
            self.client.post("/login", json={"username":"foo", "password":"bar"})
```

**Let's break it down**


```python
    import time
    from cortisol.cortisollib.users import CortisolHttpUser
    from locust import task, between
```

A cortisol file is just a normal Python module, it can import code from other files or packages.

```python
    class QuickstartUser(CortisolHttpUser):
```

Here we define a class for the users that we will be simulating. It inherits from
`CortisolHttpUser <cortisollib.users.CortisolHttpUser>` which gives each user a ``client`` attribute,
which is an instance of `HttpSession <locust.clients.HttpSession>` behind the scenes, that
can be used to make HTTP requests to the target system that we want to load test. When a test starts,
locust will create an instance of this class for every user that it simulates, and each of these
users will start running within their own green gevent thread.

For a file to be a valid cortisolfile it must contain at least one class inheriting from :py:class:`CortisolHttpUser <cortisollib.users.CortisolHttpUser>`.

Behind the scenes, the class `CortisolHttpUser <cortisollib.users.CortisolHttpUser>` has extended the `User <locust.User>` so that it can read and process the logs that are written during the load test that happen in the background.

```python
    wait_time = between(1, 5)
```

Our class defines a ``wait_time`` that will make the simulated users wait between 1 and 5 seconds after each task (see below)
is executed. For more info see [wait-time](https://docs.locust.io/en/stable/writing-a-locustfile.html#wait-time).

```python
    @task
    def hello_world(self):
        ...
```

Methods decorated with ``@task`` are the core of your cortisol file. For every running user,
Locust creates a greenlet (micro-thread), that will call those methods.

```python
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_items(self):
    ...
```

We've declared two tasks by decorating two methods with ``@task``, one of which has been given a higher weight (3).
When our ``QuickstartUser`` runs it'll pick one of the declared tasks - in this case either ``hello_world`` or
``view_items`` - and execute it. Tasks are picked at random, but you can give them different weighting. The above
configuration will make Locust three times more likely to pick ``view_items`` than ``hello_world``. When a task has
finished executing, the User will then sleep during its wait time (in this case between 1 and 5 seconds).
After its wait time it'll pick a new task and keep repeating that.

Note that only methods decorated with ``@task`` will be picked, so you can define your own internal helper methods any way you like.

```python
    self.client.get("/hello")
```

```python
    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)
```

In the ``view_items`` task we load 10 different URLs by using a variable query parameter.
