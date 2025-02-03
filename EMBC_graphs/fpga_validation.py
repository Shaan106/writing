import matplotlib.pyplot as plt

# Data for the components and their total power
components = ['AVG', 'SVM', 'THR', 'TKEO']
total_power = [0.001 * 16, 0.012, 0.0005, 0.003 * 16]

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
plt.savefig('plots/fpga_validation.png')

# ---- comparision ------

components = ['AVG', 'SVM', 'THR', 'TKEO']
total_power = [0.0003219456, 0.003465, 2.8e-10, 0.03489792]

# Create a figure for logarithmic scale
plt.figure(figsize=(7, 6))

# Plot with logarithmic scale
plt.bar(components, total_power, color=['orange', 'lightskyblue', 'green', 'red'], 
    edgecolor='black', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.yscale('log')
plt.xlabel('Component')
plt.ylabel('Total Power (W)')
# plt.title('Total Power of Components (Log Scale)')

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('plots/fpga_compare_log.png')