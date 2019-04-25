import requests

def oget(*args, **kwargs):
    """Wraps the requests.get() method"""

    # TODO: add replay logic

    return requests.get(*args, **kwargs)
