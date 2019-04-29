import unittest
import obstinate
import requests
import Server
import time

class Test(unittest.TestCase):

    http_server = None

    @classmethod
    def setUpClass(cls):
        """Method executed only once before running the tests
        
        Runs a local http server to perform tests on it
        """
        cls.http_server = Server.Server()
        cls.http_server.start()

        # wait a bit to be sure the server is running while test are run
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        """Method executed only once at the end of the tests
        
        Shuts down the local http server
        """
        cls.http_server.shutdown()
    
    def test_code_200(self):
        """It should returns the server's response when everthing works
        fine"""

        url = 'http://localhost:7654/status_code=200'
        
        res = obstinate.oget(url)

        self.assertEqual(res.status_code, 200)

    def test_status_forcelist_1(self):
        """It should make several attemps when the status code received
        isn't the one expected"""

        url = 'http://localhost:7654/status_code=500'
        
        # start counting the number of requests received
        self.http_server.reset_counter()

        res = obstinate.oget(url, o_status_forcelist=['500'],
            o_max_attempts=2)

        self.assertEqual(3, self.http_server.counter())

    def test_status_forcelist_2(self):
        """It should not make several attemps when the status code
        received wasn't listed in `o_status_forcelist`"""

        url = 'http://localhost:7654/status_code=500'
        
        # start counting the number of requests received
        self.http_server.reset_counter()

        res = obstinate.oget(url, o_status_forcelist=['501'],
            o_max_attempts=2)

        self.assertEqual(1, self.http_server.counter())

    def test_behavior_consistency_1(self):
        """It should return the server's response after several queries
        with status code 500, as the requests library would do"""
        
        url = 'http://localhost:7654/status_code=500'
        
        res = obstinate.oget(url, o_status_forcelist=['5xx'])
        
        self.assertEqual(res.status_code, 500)

    def test_behavior_consistency_2(self):
        """It should raise the same error as the requests library"""

        def f():
            url = 'htp:/url-with-wrong-format.error'
            res = obstinate.oget(url)
        
        self.assertRaises(requests.exceptions.InvalidSchema, f)
    
if __name__ == '__main__':
    unittest.main()
