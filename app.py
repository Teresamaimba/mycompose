from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Teresia Maimba - DevOps Support Project!!")

server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
print("Server running on port 8080...")
server.serve_forever()
