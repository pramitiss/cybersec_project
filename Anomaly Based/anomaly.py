import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:/VIT- STUDY MATERIAL/project_cybersec/network_traffic.csv')

index = pd.Index(range(2,len(df)+2))
df.index = index

features = ['Flow_IAT_Min', 'Tot_Fwd_Pkts', 'Init_Bwd_Win_Bytes', 'Src_port']
X = df[features].copy()

X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.dropna(inplace=True)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

isoforest = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
isoforest.fit(X_scaled)

predictions = isoforest.predict(X_scaled)
df['anomaly'] = np.nan
df.loc[X.index, 'anomaly'] = predictions

anomalies_df = df[df['Label'] == 1]

print(anomalies_df)

normal_data = df[df['Label'] == 0]
anomalies_data = df[df['Label'] == 1]

plt.figure(figsize=(12, 6))
plt.scatter(anomalies_data.index, anomalies_data['Flow_IAT_Min'], color='red', label='Anomaly', alpha=0.6)

plt.title('Anomalies in Network Traffic')
plt.xlabel('Time (index)')
plt.ylabel('Flow IAT Min')
plt.legend()
plt.show()
