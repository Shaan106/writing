import matplotlib.pyplot as plt
import numpy as np

components = ['AVG', 'BBF', 'FFT', 'PWXC', 'SVM', 'THR', 'TKEO']
total_latency = [56852.48, 67584.0, 5132779.52, 75776.0, 14.32,  0.86, 63078.4]

# Data for the components and their total latency
shiao_components = {
    'THR': 0.86,
    'PWXC': 75776.0,
    'SVM': 14.32,
    'BBF': 67584.0,
    'FFT': 5132779.52,
}

neo_components = {
    'THR': 0.86,
    'AVG': 56852.48,
    'SVM': 14.32,
    'TKEO': 63078.4,
}

# Data for the bar plot
models = ['Shiao et al.', 'NEO']

shiao_sum = shiao_components['FFT'] + shiao_components['SVM'] + shiao_components['THR']
neo_sum = neo_components['TKEO'] + neo_components['AVG'] + neo_components['SVM'] + neo_components['THR'] 

latency = [shiao_sum, neo_sum]

plt.figure(figsize=(7, 6))
# Create the bar plot with transparent colors and thin boundary lines
plt.bar(models, latency, color=['orange', 'lightskyblue'], edgecolor='black', alpha=0.7)

# Set y-axis to log scale
plt.yscale('log')

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Add labels and title
plt.xlabel('Model')
plt.ylabel('Latency (s)')
# plt.title('Latency of Seizure Detection Models')

# Save the plot
plt.savefig('plots/pipeline_latency.png')
