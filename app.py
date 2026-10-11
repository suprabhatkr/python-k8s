from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Kubernetes & Docker!</h1><p>This is a simple Python HTTP server.</p>")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
    print("Serving on port 8080...")
    server.serve_forever()