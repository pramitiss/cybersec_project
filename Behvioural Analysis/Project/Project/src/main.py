from data_collection import read_pcap_file
from feature_extraction import extract_features
from signature_matching import match_signature
from alert_generation import generate_alert

if __name__ == '__main__':
      # Adjust interface and capture rate as needed
    pcap_file = 'data/pcap_files/traffic.pcap'
    read_pcap_file(pcap_file)
    features = extract_features(pcap_file)

    if match_signature(features, signatures='data/signatures.json') is False:
        generate_alert(features[0]['source_ip'], features[0]['destination_ip'])