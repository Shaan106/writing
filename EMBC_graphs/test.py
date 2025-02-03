import matplotlib.pyplot as plt
import numpy as np

# Data for the components and their total power
components = ['AVG', 'BBF', 'FFT', 'PWXC', 'SVM', 'THR', 'TKEO']
total_power = [0.0003219456, 0.030179328, 2.84672, 0.002269184, 0.003465, 2.8e-10, 0.03489792]

# Define figure and axes with two y-axis scales
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(7, 6), gridspec_kw={'height_ratios': [1, 4]})

# Define the break point
break_point = 0.04  # Adjust as needed to fit your data well

# Plot lower portion
ax1.bar(components, total_power, color=['orange', 'lightskyblue', 'green', 'red', 'purple', 'brown', 'pink'], 
        edgecolor='black', alpha=0.7)
ax1.set_ylim(2, 3)  # Adjust to show the tallest bar
ax1.spines['bottom'].set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)  

# Plot upper portion
ax2.bar(components, total_power, color=['orange', 'lightskyblue', 'green', 'red', 'purple', 'brown', 'pink'], 
        edgecolor='black', alpha=0.7)
ax2.set_ylim(0, break_point)
ax2.spines['top'].set_visible(False)

# Add diagonal break markers
d = .015  # Size of the diagonal lines
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False, linewidth=1.5)
# ax1.plot((-d, +d), (-d, +d), **kwargs)
# ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)

kwargs.update(transform=ax2.transAxes)
# ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
# ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

# Labels and grid
ax2.set_ylabel('Total Power (W)')
ax2.grid(axis='y', linestyle='--', alpha=0.6)
ax1.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('plots/test.png')
plt.show()
