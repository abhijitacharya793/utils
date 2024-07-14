# Web server
# Usage:
# curl -X POST http://localhost:8000 -d "param1=value1"
# curl http://localhost:8000

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "<h1>Web server</h1><br/><p>Hello GET!!</p>"
        self.wfile.write(bytes(message, "utf-8"))
        return

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(post_data.decode("utf-8"))
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = f"<h1>Web server</h1><br/><p>Hello POST!!</p><br/><i>{parsed_data}</i>"
        self.wfile.write(bytes(message, "utf-8"))
        return


server_addr = ("", 8000)
httpd = HTTPServer(server_addr, RequestHandler)
print("Starting server at port 8000")
httpd.serve_forever()
