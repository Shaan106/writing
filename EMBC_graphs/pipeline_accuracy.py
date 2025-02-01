import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# Data for the bar plot
models = ['Shiao et al.', 'NEO']
accuracies = [89, 75]

# Set the font details
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# Standardizing the figure size
plt.figure(figsize=(3.5, 3.5))

# Create the bar plot with specified colors and full opacity
plt.bar(models, accuracies, color=['#8fbc8f', '#ccffcc'], edgecolor='black', alpha=1, zorder=3)

# Add gridlines with different styles for major and minor
plt.grid(True, which='major', linestyle='-', color='grey', alpha=0.8, zorder=0)  # Stronger alpha for major lines
plt.grid(True, which='minor', linestyle=':', color='grey', alpha=0.5, zorder=0)  # Dotted and lighter for minor lines

# Set up minor locator for y-axis
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.minorticks_on()  # Ensure that minor ticks are on

# Set the y-axis limits to include up to 100
plt.ylim(0, 100)

# Add labels
plt.xlabel('Pipeline')
plt.ylabel('Accuracy (%)')

# Adjust layout to ensure all titles and labels are visible
plt.tight_layout()

# Save the plot as a PDF
plt.savefig('./plots/pipeline_accuracy.pdf', format='pdf')

plt.show()
