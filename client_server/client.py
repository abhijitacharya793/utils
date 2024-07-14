import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect(("172.18.0.1", 8000))

    # Send data to the server
    message = "hello"
    client_socket.sendall(message.encode())

    # Receive data from the server
    received_data = client_socket.recv(1024)
    print(f"Received from server: {received_data.decode()}")

except ConnectionRefusedError:
    print("Connection was refused, make sure the server is running")
finally:
    # Close the socket connection
    client_socket.close()
