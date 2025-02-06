import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches


# Data
memory_types = ['STT', 'PCM', 'FeFET', 'RRAM']
areas = [0.352215178, 0.249885986, 0.150765438, 0.358045268]
powers = [0.037975518144, 0.006268435152, 0.007346379504, 0.025138752816]
life_expectancies = [476833520.2520733, 95366.70405041466, 47683.35202520733, 476.8335202520733]

colors = []  # To hold color values

# Define custom colors using named colors from matplotlib
dark_green = np.array((18/255, 53/255, 36/255))
light_green = np.array((247/255, 252/255, 245/255))

num_types = len(memory_types)

for i in range(len(memory_types)):
    # Create a gradient of colors 
    blend_ratio = i / (num_types - 1)  # Calculate blending ratio based on index
    blended_color = (1 - blend_ratio) * dark_green + blend_ratio * light_green
    colors.append(blended_color)

plt.rc('font', family='Serif', size=12)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
fig.subplots_adjust(left=0.02)

# Set the width and depth of the bars as specified
bar_width = 0.8
bar_depth = 0.03

# Plotting data
sorted_indices = np.argsort(life_expectancies)  # Sort by life expectancy for plotting
for i in sorted_indices:
    ax.bar3d(np.log10(life_expectancies[i]), areas[i], 0, bar_width, bar_depth, powers[i], color=colors[i], zorder=3, hatch='//', edgecolor='black')

# Setting labels and applying log scale on the life expectancy axis
ax.set_xlabel('Life Expectancy (s)', labelpad=15)
ax.set_ylabel('Area ($mm^2$)', labelpad=15)
ax.set_zlabel('Power (mW)', labelpad=15)

# Adjusting x-axis ticks for log scale to display up to 10^10
max_power = 10  # The maximum power of 10 you want displayed
tick_vals = np.arange(np.floor(np.log10(min(life_expectancies))), max_power + 1)

ax.set_xticks(tick_vals)
ax.set_xticklabels([f"$10^{{{int(x)}}}$" for x in tick_vals])  # Display in scientific notation

# Adjusting z-axis ticks to show increments from 0 to 0.04 by 0.01
z_ticks = np.arange(0, 0.041, 0.01)
ax.set_zticks(z_ticks)
ax.set_zticklabels([f"{z:.2f}" for z in z_ticks])

ax.set_xlim(1.5, 10.5)
ax.set_ylim(0.125, 0.425)
ax.set_zlim(0, 0.04)

# Create a custom legend for cell types
legend_handles = [mpatches.Patch(facecolor=color, label=memory, edgecolor='black') for color, memory in zip(colors, memory_types)]
legend = ax.legend(legend_handles, memory_types, ncol=4, loc='upper center', bbox_to_anchor=(0.55, 1.05))

plt.tight_layout()

# Save the plot as a PDF
plt.savefig('./plots/storage.pdf', format='pdf')

plt.show()