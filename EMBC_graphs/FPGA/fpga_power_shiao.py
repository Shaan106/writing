import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
import numpy as np

import matplotlib

plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})
matplotlib.rcParams['text.usetex'] = True

# Data
x_labels = ["Pipeline 1", "Pipeline 2"]
pipeline1_labels = ['PWXC', 'BBF', 'SVM', 'THR', 'FFT']
pipeline2_labels = ['PWXC', 'BBF', 'SVM', 'THR', 'FFT']

pipeline1_power = [2.269184, 30.179328, 3.465, 0.00028, 2846.72]  # Converted to mW
pipeline2_power = [0.003,    0.003,     0.057,   0.002,  1.334] # this is in watts

# Normalize power values to 100%
pipeline1_total_power = sum(pipeline1_power)
pipeline2_total_power = sum(pipeline2_power)

pipeline1_power_normalized = [p / pipeline1_total_power * 100 for p in pipeline1_power]
pipeline2_power_normalized = [p / pipeline2_total_power * 100 for p in pipeline2_power]

# Define colors from a spectrum between specified RGB values
color_map = {
    'PWXC': np.array([195, 35, 25])/255,    # Darker version of #D92D20
    'BBF': np.array([207, 75, 45])/255,     # Further darkened version of original BBF
    'SVM': np.array([215, 120, 90])/255,    # Deeper and darker than the previous adjustment
    'THR': np.array([225, 160, 120])/255,   # Darkened to maintain the gradient with previous colors
    'FFT': np.array([249, 200, 160])/255,   # Unchanged as it's already towards the lighter end
    'TKEO': np.array([255, 224, 204])/255,  # Unchanged from your previous code
    'AVG': np.array([255, 250, 245])/255    # Whiter version of the original AVG color
}

# Create the figure and subplot
fig, ax = plt.subplots(figsize=(5, 5))

# Plotting data with color gradients for both pipelines
bar_handles = []  # Store handles for the legend
pipeline1_bottom = 0
pipeline2_bottom = 0

for i, (label, power) in enumerate(zip(pipeline1_labels, pipeline1_power_normalized)):
    hatch = '//' if label in ['TKEO', 'AVG'] else ''
    bar = ax.bar('Forsee', power, bottom=pipeline1_bottom, color=color_map[label], edgecolor='black', alpha=1, width=0.6, zorder=3, hatch=hatch)
    if label not in [l for _, l in bar_handles]:  # Add handle only if not already added
        bar_handles.append((bar[0], label))
    pipeline1_bottom += power

for i, (label, power) in enumerate(zip(pipeline2_labels, pipeline2_power_normalized)):
    hatch = '//' if label in ['TKEO', 'AVG'] else ''
    bar = ax.bar('FPGA', power, bottom=pipeline2_bottom, color=color_map[label], edgecolor='black', alpha=1, width=0.6, zorder=3, hatch=hatch)
    if label not in [l for _, l in bar_handles]:  # Add handle only if not already added
        bar_handles.append((bar[0], label))
    pipeline2_bottom += power

# Enable major grid lines
ax.grid(which='major', linestyle='-', linewidth=0.7, color='grey', alpha=0.9)  # Darker line for major grid

# Enable minor grid lines
ax.minorticks_on()  # Enable minor ticks which are necessary for minor grid lines
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)  # Dotted line for minor grid

ax.xaxis.set_minor_locator(NullLocator())

# Set y-axis limit
ax.set_ylim(0, 105)

# Labels and legend
ax.set_xlabel("Power Model")
ax.set_ylabel("Power (\%)")

ax.legend(handles=[h for h, _ in bar_handles], labels=[l for _, l in bar_handles], loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('../plots/fpga_power_validation.pdf', format='pdf', bbox_inches='tight')
plt.savefig('../plots/fpga_power_validation.png', format='png', bbox_inches='tight')

plt.show()
