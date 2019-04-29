import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(threading.Thread):
    """Basic HTTP server

    The server is run into a separated thread to avoid blocking the main
    script.
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.host_name = 'localhost'
        self.port_number = 7654

    def run(self):
        self.http_server = HTTPServer((self.host_name, self.port_number), Handler)
        # add a counter to track the number of requests received
        self.http_server.obst_counter = 0
        self.http_server.serve_forever()

    def shutdown(self):
        self.http_server.shutdown()
    
    def counter(self):
        """Return the number of queries received since the last call to
        the method `reset_counter`"""

        return self.http_server.obst_counter

    def reset_counter(self):
        self.http_server.obst_counter = 0

class Handler(BaseHTTPRequestHandler):
    """Router for the HTTP server"""

    def do_GET(self):
        # increment the counter each time a request is received
        self.server.obst_counter += 1

        # handle the routes
        if self.path[:13] == '/status_code=':
            status = int(self.path[13:])
        else:
            status = 404
        
        # send the response
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    # deactivate logs
    def log_message(self, *args, **kwargs):
        pass