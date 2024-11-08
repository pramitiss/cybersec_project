import dpkt
import socket

def extract_features(pcap_file):
    features = []
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                continue
            ip = eth.data
            if ip.p == dpkt.ip.IP_PROTO_TCP:
                tcp = ip.data
                features.append({
                    'source_ip': socket.inet_ntoa(ip.src),
                    'destination_ip': socket.inet_ntoa(ip.dst),
                    'source_port': tcp.sport,
                    'destination_port': tcp.dport,
                    # Add other relevant features as needed
                })
    return features