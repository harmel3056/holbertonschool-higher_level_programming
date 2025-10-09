#!/usr/bin/python3
"""
Introduction to HTTP using http.server
"""
import http.server
import json

PORT = 8000
Handler = http.server.BaseHTTPRequestHandler


class MyHandler(Handler):
    def do_GET(self):
        """
        Custom class identifying response protocol when someone runs GET
        """
        if self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_error(404, "Endpoint not found")


with http.server.HTTPServer(("", PORT), MyHandler) as httpd:
    print(f"serving at port {PORT}")
    httpd.serve_forever()
