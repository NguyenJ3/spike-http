from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        print("Received message: ", body)
        self.send_response(200)
        self.end_headers()
server_address = ('localhost', 8000)
httpd = HTTPServer(server_address, RequestHandler)
httpd.serve_forever()