import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("new.csv")

# Filter data for sensor a1
sensor_a1_data = data[data['Sensor'] == 'a1']

# Extract water content and capacitance values
water_content = sensor_a1_data['water content']
capacitance_2kHz = sensor_a1_data['2kHz(pF)']
capacitance_20kHz = sensor_a1_data['20kHz(pF)']
capacitance_200kHz = sensor_a1_data['200kHz(pF)']
capacitance_1M = sensor_a1_data['1M(pF)']

# Plot the graph
plt.figure(figsize=(10, 6))

plt.plot(water_content, capacitance_2kHz, label='2kHz')
plt.plot(water_content, capacitance_20kHz, label='20kHz')
plt.plot(water_content, capacitance_200kHz, label='200kHz')
plt.plot(water_content, capacitance_1M, label='1M')

plt.xlabel('Water Content')
plt.ylabel('Capacitance (pF)')
plt.title('Capacitance vs Water Content for Sensor a1')
plt.legend()
plt.grid(True)

plt.show()

