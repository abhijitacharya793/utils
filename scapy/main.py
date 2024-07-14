# TODO:
#   how to get local subnet automatically
#   dns poisoning tool - like dnsspoof
#   ARP mitm tool
#   TCP SYN scanner
#   dns fuzzer


# subnet scanner
from scapy.all import *

for lsb in range(1, 256):
    ip = f"192.168.1.{lsb}"
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    arp_response = srp1(arp_request, timeout=1, verbose=0)
    if arp_response:
        print(f"IP: {arp_response.psrc} MAC: {arp_response.hwsrc}")
