import matplotlib.pyplot as plt

# Data for the bar plot
models = ['Shiao et al.', 'NEO']
accuracies = [89, 75]

plt.figure(figsize=(7, 6))
# Create the bar plot with transparent colors and thin boundary lines
plt.bar(models, accuracies, color=['orange', 'lightskyblue'], edgecolor='black', alpha=0.7)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Add labels and title
plt.xlabel('Model')
plt.ylabel('Accuracy (%)')
# plt.title('Accuracy of Seizure Detection Models')

# Save the plot
plt.savefig('plots/model_accuracy.png')
