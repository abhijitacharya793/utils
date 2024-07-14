import socketserver
import http.server

port = 8000

# acts as a file server
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
