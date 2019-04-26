import requests
import time

def oget(*args, o_max_attempts=2, **kwargs):
    """Wraps the requests.get() method"""

    # keep track of the number of request sent
    attempts = 0

    # send the request at least once
    # if it fails, retry at most o_max_attempts times
    while attempts < o_max_attempts + 1:

        # send the request and keep track if an error occurs
        try:
            res = requests.get(*args, **kwargs)
        except Exception as e:
            exception = e
        else:
            exception = None

        # increase the counter of request sent
        attempts += 1

        # choose what to do according to the response received
        if exception is not None:
            url = args[0]
            print('An error occured while trying to reach {}'.format(url))
        else:
            # everything is OK
            return res

        # wait, hoping it won't fail the next time
        time.sleep(1)

    url = args[0]
    raise Exception('Impossible to reach {}'.format(url))
