import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

import matplotlib
matplotlib.rcParams['text.usetex'] = True

# Data for the bar plot
models = ['Pipeline 1', 'Pipeline 2']
accuracies = [89, 75]

# Set the font details
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# Standardizing the figure size
plt.figure(figsize=(3.5, 3.5))

# Create the bar plot with specified colors, full opacity, and modified bar width
#plt.bar(models, accuracies, color=[(18/255, 53/255, 36/255), (247/255, 252/255, 245/255)], edgecolor='black', alpha=1, width=0.6, zorder=3)
plt.bar(models, accuracies, color=[(195/255, 35/255, 25/255), (255/255, 239/255, 225/255)], edgecolor='black', alpha=1, width=0.6, zorder=3)

# Add gridlines with different styles for major and minor
plt.grid(True, which='major', linestyle='-', linewidth=0.7, color='grey', alpha=0.9)
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)  # Dotted minor lines

# Set up minor locator for y-axis
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.minorticks_on()  # Ensure that minor ticks are on
plt.xticks(range(len(models)), models)
plt.gca().xaxis.set_minor_locator(AutoMinorLocator(0))  # Disable minor ticks on x-axis


# Set the y-axis limits to include up to 100
plt.ylim(0, 100)

# Add labels
plt.xlabel('Approach')
plt.ylabel('Accuracy (\%)')

# Adjust layout to ensure all titles and labels are visible
plt.tight_layout()

# Save the plot as a PDF
plt.savefig('./plots/pipeline_accuracy.pdf', format='pdf')

plt.show()
