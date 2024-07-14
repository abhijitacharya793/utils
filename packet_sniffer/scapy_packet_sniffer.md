> can be used to create packet sniffer
> WiFi sniffer to print SSID

* finding protocols and details

```bash
ls()
```

```bash
ls(IP)
```

```bash
IP().show()
```

* sniffing packets

```bash
pkts = sniff(iface="eth0", count=3)
hexdump()
```

* simulating sniffing with a offline pcap capture

```bash
pkts = sniff(offline="offline.pcap")
```

* adding filters

```bash
pkts = sniff(iface="eth0", filter="arp", count=3)
```

* print packets live

```bash
pkts = sniff(iface="eth0", filter="icmp", count=20, prn=lambda x:x.summary())
```

* write packets to pcap file

```bash
wrpcap("demo.pcap", pkts)
```

* read from pcap

```bash
rdpcap("demo.pcap")
```

* export packet as base64 encoded

```bash
export_object(str(pkts[0]))
```

* import packet from base64 encoded

```bash
new_pkt = import_object()
```

* export packet as string

```bash
str(pkts[0])
```

* import packet as string

```bash
FirstHeader e.g. Ether(pkt_string)
```