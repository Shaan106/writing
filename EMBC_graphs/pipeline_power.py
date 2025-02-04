import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, LogFormatterSciNotation

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
models = ['Pipeline 1', 'Pipeline 2']

shiao_sum = sum(shiao_components.values())
neo_sum = sum(neo_components.values())

power = [x * 10**3 for x in [shiao_sum, neo_sum]] # convert to mW

# Set the font details
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# Standardizing the figure size
plt.figure(figsize=(3.5, 3.5))

# Create the bar plot with specified colors and full opacity
plt.bar(models, power, color=[(18/255, 53/255, 36/255), (247/255, 252/255, 245/255)], edgecolor='black', alpha=1, width=0.6, zorder=3)

# Add gridlines for major and explicitly for minor
plt.grid(True, which='major', linestyle='-', linewidth=0.7, color='grey', alpha=0.9)  # Darker major lines
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)  # Dotted minor lines

# Setting up the y-axis with log scale
plt.yscale('log')
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_major_formatter(LogFormatterSciNotation())
plt.gca().yaxis.set_minor_formatter(LogFormatterSciNotation(minor_thresholds=(2, 0.5)))

# Explicitly defining major and minor ticks on y-axis
plt.ylim(bottom=10**0, top=10**4)  # Setting the limits to explicitly include from 10^-2 to 10^1
plt.gca().set_yticks([10**x for x in range(0, 5)])  # Major ticks from 10^-2 to 10^1
minor_ticks = [x * 10**i for i in range(0, 4) for x in range(2, 10)]
plt.gca().set_yticks(minor_ticks, minor=True)  # Adding detailed minor ticks to ensure visibility
plt.xticks(range(len(models)), models)

# Adding axis labels
plt.xlabel('Approach')
plt.ylabel('Power (mW)')

# Adjusting layout to ensure all labels and titles are visible
plt.tight_layout()

# Save the plot as a PDF
plt.savefig('./plots/pipeline_power.pdf', format='pdf')

# Display the plot
plt.show()
