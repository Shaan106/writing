import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

# Data
x_labels = ["Pipeline 1", "Pipeline 2"]
pipeline1_labels = ['PWXC', 'BBF', 'SVM', 'THR', 'FFT']
pipeline2_labels = ['TKEO', 'AVG', 'SVM', 'THR']

pipeline1_power = [2.269184, 30.179328, 3.465, 0.00028, 2846.72]  # Converted to mW
pipeline2_power = [34.89792, 0.3219456, 3.465, 0.00028]

# Define colors from a spectrum between specified RGB values
# Ensuring SVM and THR have the same colors across both pipelines
color_map = {
    'PWXC': (18/255, 53/255, 36/255),  # Dark green
    'BBF': (82/255, 149/255, 118/255),
    'SVM': (146/255, 245/255, 200/255),  # Same color for SVM in both pipelines
    'THR': (217/255, 253/255, 239/255),  # Same color for THR in both pipelines
    'FFT': (247/255, 252/255, 245/255),  # Light green
    'TKEO': (50/255, 101/255, 77/255),
    'AVG': (114/255, 197/255, 159/255)
}

plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# Create the figure and subplots
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(5, 5),
                              gridspec_kw={'height_ratios': [1, 2]})

fig.subplots_adjust(hspace=0.5, top=0.85, left=0.18)

# Increase the size of the diagonal ticks to make the break appear wider
d = 0.03  # Increase this value for wider breaks

# Adjust the plot to render the break marks
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# Adjust spacing between subplots if necessary for aesthetics
fig.subplots_adjust(hspace=0.1)  # Increase if more space is needed

# Plotting data with color gradients for both pipelines
bar_handles = []  # Store handles for the legend
for axx in [ax, ax2]:
    pipeline1_bottom = 0
    pipeline2_bottom = 0

    for i, (label, power) in enumerate(zip(pipeline1_labels, pipeline1_power)):
        bar = axx.bar('Pipeline 1', power, bottom=pipeline1_bottom, color=color_map[label], edgecolor='black', alpha=1, width=0.6, zorder=3)
        if label not in [l for _, l in bar_handles]:  # Add handle only if not already added
            bar_handles.append((bar[0], label))
        pipeline1_bottom += power

    for i, (label, power) in enumerate(zip(pipeline2_labels, pipeline2_power)):
        bar = axx.bar('Pipeline 2', power, bottom=pipeline2_bottom, color=color_map[label], edgecolor='black', alpha=1, width=0.6, zorder=3)
        if label not in [l for _, l in bar_handles]:  # Add handle only if not already added
            bar_handles.append((bar[0], label))
        pipeline2_bottom += power
    
    # Enable major grid lines
    axx.grid(which='major', linestyle='-', linewidth=0.7, color='grey', alpha=0.9)  # Darker line for major grid
    
    # Enable minor grid lines
    axx.minorticks_on()  # Enable minor ticks which are necessary for minor grid lines
    axx.grid(which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)  # Dotted line for minor grid

    axx.xaxis.set_minor_locator(NullLocator())


# Adjust the split in the y-axis
ax.set_ylim(2860, 2885)  # upper plot
ax2.set_ylim(0, 40)  # lower plot

# Labels and legend
ax2.set_xlabel("Approach")

# Shared Y-axis label centered vertically
fig.text(0.01, 0.5, 'Power (mW)', va='center', rotation='vertical')

ax.legend(handles=[h for h, _ in bar_handles], labels=[l for _, l in bar_handles], ncol=4, loc='upper center', bbox_to_anchor=(0.45, 1.6))

plt.savefig('./plots/power_aggregate.pdf', format='pdf')

plt.show()
