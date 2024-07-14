# Monitor the packet using:
# sudo tcpdump -i eth0 -vv -XX
# Try sending ARP Packet

import socket
# network byte order: Big Endian format
import struct

# 0x0800 -> Internet protocol packet
raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

raw_socket.bind(("eth0", socket.htons(0x0800)))

packet = struct.pack("!6s6s2s", "\xaa\xaa\xaa\xaa\xaa\xaa".encode(), "\xbb\xbb\xbb\xbb\xbb\xbb".encode(),
                     "\x08\x00".encode())
raw_socket.send(packet + "Yo world".encode())
