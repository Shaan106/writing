import matplotlib.pyplot as plt

# Data for the components and their total latency
components = ['AVG', 'BBF', 'FFT', 'PWXC', 'SVM', 'THR', 'TKEO']
total_latency = [56852.48, 67584.0, 5132779.52, 75776.0, 14.32,  0.86, 63078.4]

# Plot with linear scale
plt.figure(figsize=(7, 6))
plt.bar(components, total_latency, color=['orange', 'lightskyblue', 'green', 'red', 'purple', 'brown', 'pink'], 
    edgecolor='black', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xlabel('Component')
plt.ylabel('Total Latency (ns)')
# plt.title('Total Latency of Components (Linear Scale)')
plt.tight_layout()
plt.savefig('plots/total_latency_components_linear.png')
plt.close()

# Plot with logarithmic scale
plt.figure(figsize=(7, 6))
plt.bar(components, total_latency, color=['orange', 'lightskyblue', 'green', 'red', 'purple', 'brown', 'pink'], 
    edgecolor='black', alpha=0.7)
plt.yscale('log')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xlabel('Component')
plt.ylabel('Total Latency (ns)')
# plt.title('Total Latency of Components (Logarithmic Scale)')
plt.tight_layout()
plt.savefig('plots/total_latency_components_log.png')
plt.close()
