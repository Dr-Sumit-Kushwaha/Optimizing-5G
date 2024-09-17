import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('experimental_results.csv')

# Display the data
print(data)

# Plot the data
metrics = data['Metric']
EESF = data['EESF (%)']
FADT = data['FADT (%)']
ERS = data['ERS (%)']
EMUA = data['EMUA (%)']
MCM = data['MCM (%)']

# Plotting each metric
plt.figure(figsize=(10, 6))
plt.plot(metrics, EESF, label='EESF (%)', marker='o')
plt.plot(metrics, FADT, label='FADT (%)', marker='o')
plt.plot(metrics, ERS, label='ERS (%)', marker='o')
plt.plot(metrics, EMUA, label='EMUA (%)', marker='o')
plt.plot(metrics, MCM, label='MCM (%)', marker='o')

plt.xlabel('Metrics')
plt.ylabel('Performance (%)')
plt.title('Performance Comparison of Different Models')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


