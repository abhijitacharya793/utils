# L2 packet sniffer in linux
# Sniff and parse packets on n/w
# filter port 80 packets
# sudo ifconfig eth0 promisc up


import socket
# network byte order: Big Endian format
import struct
import binascii

# 0x0800 -> Internet protocol packet
raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt = raw_socket.recvfrom(2048)

# PACKET FORMAT:
# L2 - ETHERNET
# L3 - IP
# L4 - TCP
# L5 - Application

print("############### L2 ###############")
# Ethernet header is 14 bytes
ethernet_header = pkt[0][:14]
eth_hdr = struct.unpack("!6s6s2s", ethernet_header)
# first 6 bytes - destination mac addr,
# next 6 bytes - source mac addr,
# last 2 - type
print(
    f"eth_hdr is source MAC: {binascii.hexlify(eth_hdr[1])};\n destination MAC: {binascii.hexlify(eth_hdr[0])};\n "
    f"ether type (IP: 0800): {binascii.hexlify(eth_hdr[2])}"
)

print("############### L3 ###############")
ip_header = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s", ip_header)
# first 12 bytes - other headers like version, total length, identification, TTL, Protocol, Checksum;
# next 4 bytes - source ip addr; last 4 - destination ip addr
print(f"ip_hdr is source IP: {socket.inet_ntoa(ip_hdr[1])};\n destination IP: {socket.inet_ntoa(ip_hdr[2])}")

print("############### L4 ###############")
tcp_header = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s", tcp_header)
# first 2 bytes - source port;
# next 2 bytes - destination port;
print(f"tcp_hdr is source port: {tcp_hdr[0]};\n destination port: {tcp_hdr[1]}")
