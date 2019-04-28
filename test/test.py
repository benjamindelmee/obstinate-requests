import unittest
import obstinate
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
        """It should raise an error when receiving status code 500
        several times"""
        
        def f():
            url = 'http://localhost:7654/status_code=500'
            res = obstinate.oget(url, status_forcelist=['5xx'])
        
        self.assertRaises(Exception, f)
        
if __name__ == '__main__':
    unittest.main()
