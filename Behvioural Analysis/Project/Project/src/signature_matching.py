import json

def match_signature(features, signatures):
    with open('data/signatures.json', 'r') as f:
        signatures = json.load(f)

    for feature in features:
        for signature in signatures:
            if (
                feature['source_ip'] == signature['source_ip'] and
                feature['destination_ip'] == signature['destination_ip']):
                return True
    return False