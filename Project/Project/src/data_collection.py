import dpkt
import socket

def read_pcap_file(pcap_file):
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                continue
            ip = eth.data
            if ip.p == dpkt.ip.IP_PROTO_TCP:
                tcp = ip.data
                # Extract features for analysis
                source_ip = socket.inet_ntoa(ip.src)
                destination_ip = socket.inet_ntoa(ip.dst)
                source_port = tcp.sport
                destination_port = tcp.dport
                # Perform feature-based analysis and signature matching
                # ...
                yield {
                    'source_ip': source_ip,
                    'destination_ip': destination_ip,
                    'source_port': source_port,
                    'destination_port': destination_port,
                    # Add other extracted features as needed
                }

# Example usage:
pcap_file = 'data/pcap_files/traffic.pcap'
for flow_data in read_pcap_file(pcap_file):
    read_pcap_file(pcap_file)
    # Process flow data and perform signature matching  