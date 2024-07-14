# simple tcp server and client

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    tcp_socket.bind(("0.0.0.0", 8000))

    tcp_socket.listen(2)

    print("Waiting for client")
    (client, (ip, port)) = tcp_socket.accept()

    print(f"Rx connection from {ip}")

    # client.send("Welcome")
    data = "dummy"
    while len(data):
        data = client.recv(2048)
        print(f"client sent {data}")
        client.send(f"you sent {data.decode()}".encode())
except Exception as ex:
    print(f"Error spinning up server, make sure the error is resolved: \n{ex}")
finally:
    client.close()
    tcp_socket.close()

# After this, use the following on WSL/ubuntu/any client with nc
# nc <ip> 8000
# hello
