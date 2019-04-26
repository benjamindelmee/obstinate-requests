import requests
import time

def oget(*args, o_max_attempts=2, **kwargs):
    """Same as requests.get() but with a replay mecanism included
    
    This function is an encapsulation of the requests.get() function, so
    it can be used in place of it without the need to rewrite all your
    code.

    All the parameters given to this function will be forwarded to the
    requests.get() function (except the parameters starting with o_
    because they are specific to obstinate).

    The main difference with requests.get() is that this function adds a
    replay mecanism. If the initial query to the url didn't return the
    expected response (because of a network error, a server error, or
    something else), this method will try to query again the url.

    Parameters
    ----------
    o_max_attempts : int, optional
        If the initial query fails, set the maximum number of
        new attempts. If the value is zero, no new attempt will be made
        after the initial query.
    """

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
