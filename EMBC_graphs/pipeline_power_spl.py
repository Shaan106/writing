import matplotlib.pyplot as plt
import numpy as np

# Data for the components and their total power
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

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(9, 6))

# Colors for each bar
colors1 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Blue, Orange, Green, Red, Purple
colors2 = ['#9467bd', '#8c564b', '#e377c2', '#7f7f7f']  # Purple, Brown, Pink, Gray

# First bar
bottom = 0
for component, value in shiao_components.items():
    ax.bar('Bar 1', value, bottom=bottom, label=component, color=colors1.pop(0))
    bottom += value

# Second bar
bottom = 0
for component, value in neo_components.items():
    ax.bar('Bar 2', value, bottom=bottom, label=component, color=colors2.pop(0))
    bottom += value

# Set y-axis to log scale
ax.set_yscale('log')

# Customize the plot
ax.set_ylabel('Watts')
ax.set_title('Power Consumption Breakdown\nTwo Bars Comparison')
ax.legend(title='Components', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
