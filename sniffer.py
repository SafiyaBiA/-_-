import scapy.all as scapy # type: ignore
def sniffer(interface):
    scapy.sniff(iface=interface,store=False, prn=process_packet)
def process_packet(packet):
    print(packet)
sniffer('Wi-Fi') 
