import matplotlib.pyplot as plt

# Data for the components and their total power
components = ['AVG', 'BBF', 'FFT', 'PWXC', 'SVM', 'THR', 'TKEO']
total_power = [0.0003219456, 0.030179328, 2.84672, 0.002269184, 0.003465, 2.8e-10, 0.03489792]

# Create a figure for linear scale
plt.figure(figsize=(7, 6))

# Plot with linear scale
plt.bar(components, total_power, color=['orange', 'lightskyblue', 'green', 'red', 'purple', 'brown', 'pink'], 
    edgecolor='black', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xlabel('Component')
plt.ylabel('Total Power (W)')
# plt.title('Total Power of Components (Linear Scale)')

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('plots/total_power_components_linear.png')

# Create a figure for logarithmic scale
plt.figure(figsize=(7, 6))

# Plot with logarithmic scale
plt.bar(components, total_power, color=['orange', 'lightskyblue', 'green', 'red', 'purple', 'brown', 'pink'], 
    edgecolor='black', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.yscale('log')
plt.xlabel('Component')
plt.ylabel('Total Power (W)')
# plt.title('Total Power of Components (Log Scale)')

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('plots/total_power_components_log.png')

# Show plots
# plt.show()
