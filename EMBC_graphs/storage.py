import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

print(plt.__file__)

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
fig.subplots_adjust(left=0.02, right=0.849)

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
minor_ticks = []
for val in tick_vals:
    base = 10**val
    minor_ticks.extend([3*base, 5*base, 7*base, 9*base])

# # Filter minor ticks to be within the range of data
# filtered_minor_ticks = [tick for tick in minor_ticks if min(life_expectancies) <= tick <= 10**max_power]

# Convert minor ticks to log scale for setting on log-scaled axis
minor_tick_positions = np.log10(minor_ticks)

# Add the minor ticks to the plot
ax.set_xticks(minor_tick_positions, minor=True)

ax.set_yticks(np.arange(0.1, 0.41, 0.1))
ax.set_yticks(np.arange(0.1, 0.41, 0.05), minor=True)

# Adjusting z-axis ticks to show increments from 0 to 0.04 by 0.01
ax.set_zticks(np.arange(0, 0.041, 0.01))
ax.set_zticks(np.arange(0, 0.041, 0.005), minor=True)
# ax.set_zticklabels([f"{z:.2f}" for z in z_ticks])

# y_ticks = np.arange(0, 0.041, 0.01)
# y_ticks_minor = np.arange(0, 0.041, 0.002)
# ax.set_yticks(y_ticks_minor, minor=True)
# ax.set_yticks(y_ticks)

ax.set_xlim(2, 10)
ax.set_ylim(0.1, 0.4)
ax.set_zlim(0, 0.04)

black = (175/255, 176/255, 176/255, 1)

ax.zaxis.set_gridline_color((0, black))
ax.xaxis.set_gridline_color((0, black))
ax.yaxis.set_gridline_color((6, black))


ax.zaxis._axinfo["grid"]["linestyle"] = ":"
ax.yaxis._axinfo["grid"]["linestyle"] = ":"
ax.xaxis._axinfo["grid"]["linestyle"] = ":"

ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='z', labelsize=10)


# Create a custom legend for cell types
legend_handles = [mpatches.Patch(facecolor=color, label=memory, edgecolor='black') for color, memory in zip(colors, memory_types)]
legend = ax.legend(legend_handles, memory_types, ncol=4, loc='upper center', bbox_to_anchor=(0.58, 1.05))

plt.tight_layout()

# Save the plot as a PDF
plt.savefig('./plots/storage.pdf', format='pdf')

plt.show()



# def three_dim():
#     """
#     Creates 3D plot for Spike Sorting and Seizure Detection

#     x-axis is input data rate (Mbps)
#     y-axis is power (mW)
#     z-axis is throughput (Mbps)
#     """
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1, projection="3d")

#     read_input()

#     x1, y1 = np.meshgrid(sensor_rate_range(), maxpower_range())
#     zss = np.zeros((len(x1), len(x1[0])))
#     zsz = np.zeros((len(x1), len(x1[0])))

#     for i, maxpower in enumerate(maxpower_range()):
#         sz = seizure[i] * CHAN_RATE
#         ss = spike[i] * CHAN_RATE

#         for j, rate in enumerate(sensor_rate_range()):

#             if rate <= sz:
#                 zsz[i][j] = rate
#             else:
#                 zsz[i][j] = sz

#             if rate <= ss:
#                 zss[i][j] = rate
#             else:
#                 zss[i][j] = ss

#     ax.plot_surface(
#         x1,
#         y1,
#         zss,
#         color=color_group["red"],
#         alpha=0.3
#     )
#     ax.plot_surface(
#         x1,
#         y1,
#         zsz,
#         color=color_group["blue"],
#         alpha=0.3
#     )
#     ax.plot_wireframe(
#         x1,
#         y1,
#         zss,
#         label="Spike Sorting",
#         color=color_group["red"]
#     )
#     ax.plot_wireframe(
#         x1,
#         y1,
#         zsz,
#         label="Seizure Detection",
#         color=color_group["blue"]
#     )
#     ax.set_zlabel("Throughput (Mbps)")
#     ax.set_ylabel("Power (mW)")
#     ax.set_xlabel("Sensor Data Rate (Mbps)")

#     ax.set_xticks([0, 50, 100, 150])
#     ax.set_xticks(ticks=sensor_rate_range(), minor=True)

#     ax.set_yticks([6, 9, 12, 15])
#     ax.set_yticks(ticks=maxpower_range(), minor=True)

#     ax.set_zticks([0, 25, 50, 75, 100, 125])
#     ax.set_zticks(ticks=[x for x in range(0, 125, 5)], minor=True)

#     black = (0, 0, 0, 1)
#     """
#     ax.zaxis.set_gridline_color((0, black))
#     ax.xaxis.set_gridline_color((0, black))
#     ax.yaxis.set_gridline_color((6, black))
#     """

#     ax.zaxis._axinfo["grid"]["linestyle"] = ":"
#     ax.yaxis._axinfo["grid"]["linestyle"] = ":"
#     ax.xaxis._axinfo["grid"]["linestyle"] = ":"

#     plt.legend(loc="upper right", bbox_to_anchor=(1.05, 1))
#     plt.tight_layout()

#     ax.view_init(elev=25, azim=315)
#     plt.savefig("ss_sz_throughput_3d.pdf")

#     print("finished 3d plot")