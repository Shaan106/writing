import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, LogFormatterSciNotation


import matplotlib
matplotlib.rcParams['text.usetex'] = True

# Data for latency comparison
components = ['AVG', 'BBF', 'FFT', 'PWXC', 'SVM', 'THR', 'TKEO']
total_latency = [56852.48, 67584.0, 5132779.52, 75776.0, 14.32,  0.86, 63078.4]

# Latency data for Shiao and NEO models
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

# Sum of latencies for Shiao model for specific components
shiao_sum = shiao_components['FFT'] + shiao_components['SVM'] + shiao_components['THR']

# Sum of latencies for NEO model for all its components
neo_sum = sum(neo_components.values())

# Total latency for each model
latency = [x/(10**3) for x in [shiao_sum, neo_sum]] # convert to microseconds

# Define the models for labeling in the plot
models = ['Pipeline 1', 'Pipeline 2']

# Set the font details
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# Standardizing the figure size
plt.figure(figsize=(3.5, 3.5))

# Create the bar plot with specified colors and full opacity
plt.bar(models, latency, color=[(195/255, 35/255, 25/255), (255/255, 239/255, 225/255)], edgecolor='black', alpha=1, width=0.6, zorder=3)

# Add gridlines for major and explicitly for minor
plt.grid(True, which='major', linestyle='-', linewidth=0.7, color='grey', alpha=0.9)  # Darker major lines
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)  # Dotted minor lines

# Setting up the y-axis with log scale
plt.yscale('log')
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_major_formatter(LogFormatterSciNotation())
plt.gca().yaxis.set_minor_formatter(LogFormatterSciNotation(minor_thresholds=(2, 0.5)))

# Explicitly defining major and minor ticks on y-axis
plt.ylim(bottom=10**0, top=10**4)  # Setting the limits to explicitly include from 10^0 to 10^7
plt.gca().set_yticks([10**x for x in range(0, 5)])  # Major ticks from 10^0 to 10^7
minor_ticks = [x * 10**i for i in range(0, 4) for x in range(2, 10)]
plt.gca().set_yticks(minor_ticks, minor=True)  # Adding detailed minor ticks to ensure visibility
plt.xticks(range(len(models)), models)

# Adding axis labels
plt.xlabel('Approach')
plt.ylabel('Latency ($\mu$s)')

# Adjusting layout to ensure all labels and titles are visible
plt.tight_layout()

# Save the plot as a PDF
plt.savefig('./plots/pipeline_latency.pdf', format='pdf')

# Display the plot
plt.show()
