# Only good for 1 connection at a time. Implement multi threaded version for serving multiple clients
import socket
import socketserver

server_addr = ("0.0.0.0", 8000)


class EchoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Connection recv from: {self.client_address}")
        data = "dummy"
        while len(data):
            data = self.request.recv(1024)
            print(f"Client sent data: {data}")
            self.request.send(f"you sent {data.decode()}".encode())
        print("Client left")


server = socketserver.TCPServer(server_addr, EchoHandler)

server.serve_forever()
