import matplotlib.pyplot as plt
import numpy as np

# Data for components with two bars
shiao_components = {
    'THR': 2.8e-10,
    'PWXC': 0.002269184,
    'SVM': 0.003465,
    'BBF': 0.030179328,
    'FFT': 2.84672,
}

neo_components = {
    'THR': 2.8e-10,
    'AVG': 0.0003219456,
    'SVM': 0.003465,
    'TKEO': 0.03489792, 
}

# Data for the bar plot
models = ['Shiao et al.', 'NEO']

shiao_sum = sum(shiao_components.values())
neo_sum = sum(neo_components.values())

power_consumption = [shiao_sum, neo_sum]

plt.figure(figsize=(7, 6))
# Create the bar plot with transparent colors and thin boundary lines
plt.bar(models, power_consumption, color=['orange', 'lightskyblue'], edgecolor='black', alpha=0.7)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Add labels and title
plt.xlabel('Model')
plt.ylabel('Power Consumption (W)')
# plt.title('Power Consumption of Seizure Detection Models')

# Save the plot
plt.savefig('plots/model_power_consumption.png')
