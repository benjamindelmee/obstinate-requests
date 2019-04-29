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
        """It should returns the server's respons when everthing works
        fine"""

        url = 'http://localhost:7654/status_code=200'
        
        res = obstinate.oget(url)

        self.assertEqual(res.status_code, 200)

    def test_status_forcelist(self):
        """It should return the server's respons after several queries
        with status code 500"""
        
        url = 'http://localhost:7654/status_code=500'
        
        res = obstinate.oget(url, o_status_forcelist=['5xx'])
        
        self.assertEqual(res.status_code, 500)

    def test_behavior_consistance(self):
        """It should raise the same error as the requests library"""

        def f():
            url = 'htp:/url-with-wrong-format.error'
            res = obstinate.oget(url)
        
        self.assertRaises(requests.exceptions.InvalidSchema, f)
    
if __name__ == '__main__':
    unittest.main()
