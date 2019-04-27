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
        self.http_server.serve_forever()

    def shutdown(self):
        self.http_server.shutdown()

class Handler(BaseHTTPRequestHandler):
    """Router for the HTTP server"""

    def do_GET(self):
        if self.path[:13] == '/status_code=':
            status = int(self.path[13:])
        else:
            status = 404
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
    # deactivate logs
    def log_message(self, *args, **kwargs):
        pass