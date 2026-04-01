from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Teresia apps - version 2!!")

server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
print("Server running on port 8080...")
server.serve_forever()