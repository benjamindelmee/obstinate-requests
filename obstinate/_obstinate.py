import requests
import time

def oget(*args, o_max_attempts=2, o_status_forcelist=['5xx'], **kwargs):
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
    
    o_status_forcelist : :obj:`list` of :obj:`str`, optional
        A set of HTTP status codes and classes of status codes that we
        should force a retry on.        
        Exemple: ['404', '5xx'] force retry on status code 404 and
        on status codes 5xx (500, 501, 502, etc.)
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
            # an exception was raised during the query
            url = args[0]
            print('An error occured while trying to reach {}'.format(url))
        elif _code_in_list(res.status_code, o_status_forcelist):
            # status code received is not acceptable
            url = args[0]
            print('An error occured while trying to reach {}'.format(url))
        else:
            # everything is OK
            return res

        # wait, hoping it won't fail the next time
        time.sleep(1)

    if exception is not None:
        # after several attemps, an error is still raised
        # forward this error as the requests library would do
        raise exception
    else:
        # after several attemps, unexpected status code is still received
        # return the server's respons as the requests library would do
        return res

def _code_in_list(code, codelist):
    """Tells if `code` is contained in `codelist`

    Examples:
        - 401 is not contained in ['3xx', '404', '5xx']
        - 404 is contained in ['3xx', '404', '5xx']
        - 503 is contained in ['3xx', '404', '5xx']
    """

    # status codes to exclude
    exact_codes = [code for code in codelist if 'x' not in code]
    
    if str(code) in exact_codes:
        return True

    # classes of status code to exclude
    class_codes = [code[0] for code in codelist if 'x' in code]

    if str(code)[0] in class_codes:
        return True

    return False