* scapy injection and forging

```bash
# L2 send
sendp(Ether()/IP(dst="google.com")/ICMP()/"XXX", iface="eth0", loop=1, inter=1) # loop sending packet, with interval 1 sec
```

```bash
# L3 send
send()
```

* send and receive

> l3
> * sr()  -> returns answers and unanswered packets
> * sr1() -> returns only answer or sent packets
>
> l2
> * srp()
> * srp1()

```bash
# L2
srp1=(Ether()/IP(dst="google.com", ttl=22)/ICMP()/"XXX")
r1(IP(dst="google.com"), timeout=3)
```

```bash
# L3
response, no_response = sr(IP(dst="google.com")/ICMP()/"XXX")
response, no_response = sr1(IP(dst="google.com")/ICMP()/"XXX")
```

* routing

```bash
conf.route # show route
conf.route.add(host="192.168.0.1", gw="192.168.0.2") # if host is 0.1, gateway should be 0.2
conf.route.resync() # reset
```