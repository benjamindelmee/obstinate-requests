# ![Obstinate Requests](misc/obstinate_requests.png)

Obstinate is a python 3 snippet wrapping the [requests](https://github.com/kennethreitz/requests) library.

Obstinate automaticaly replays a request when a connection error occurs, or when the status code returned by the server is not the expected one. Obstinate is meant to be used with minimum code modification, working in the exact same way as requests.

**Why / when to use Obstinate?**

When you want to send a request through Internet but you have an instable connexion, or when the server you query is busy, you sometimes need to replay multiple times the request before it works. For instance, this happens a lot to data scientists willing to grab data from a publicly accessible database. 

However, if the connection between your application and the remote server is critical, you'd better to implement a tailor-made solution in order to handle edge scenarios.

## Getting Started

### Installation

First, install obstinate into your python environment:

```bash
git clone https://github.com/benjamindelmee/obstinate-requests

cd obstinate-requests

python -m pip install .
```

### Usage

Obstinate adds the `obstinate.oget()` method to the *requests* library.

```python
import obstinate as requests

url = 'https://www.google.com'

# make the request with oget() instead of get()
res = requests.oget(url)

# no more than 5 retries will be made, only for the status code 418, 500,
# 501, 502, etc.
res = requests.oget(url, o_max_attempts=5, o_status_forcelist=['418', '5xx'])

# if needed, you still have access to the original and unmodified get()
# method of requests
res = requests.get(url)
```
