import numpy as np
import pandas as pd
from scapy.all import rdpcap
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt
import seaborn as sns


# Function to parse PCAP file and create a dataset
def parse_pcap(file_path):
    packets = rdpcap(file_path)
    data = []
    for packet in packets:
        if packet.haslayer('IP'):
            packet_size = len(packet)
            packet_rate = packet.time  
            duration = packet.time  
            is_ddos = 0  
            data.append([packet_size, packet_rate, duration, is_ddos])
    return pd.DataFrame(data, columns=['packet_size', 'packet_rate', 'duration', 'is_ddos'])

# Parse the PCAP file
df = parse_pcap(r"C:\Users\rohan\Downloads\Project\Project\data\pcap_files\traffic.pcap")

# Split the dataset into training and testing sets
X = df[['packet_size', 'packet_rate', 'duration']]
y = df['is_ddos']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))

# Example of detecting a new sample
new_sample = np.array([[500, 300, 50]])
prediction = clf.predict(new_sample)
print(f"Prediction for the new sample: {'DDoS' if prediction[0] == 1 else 'Normal'}")

# Distribution of Packet Sizes
plt.figure(figsize=(10, 6))
sns.histplot(df['packet_size'], bins=50, kde=True)
plt.title('Distribution of Packet Sizes')
plt.xlabel('Packet Size')
plt.ylabel('Frequency')
plt.show()

# Packet Rate Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df.index, y='packet_rate')
plt.title('Packet Rate Over Time')
plt.xlabel('Time')
plt.ylabel('Packet Rate')
plt.show()

# Duration of Packets
plt.figure(figsize=(10, 6))
sns.histplot(df['duration'], bins=50, kde=True)
plt.title('Distribution of Packet Durations')
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.show()


