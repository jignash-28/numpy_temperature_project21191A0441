
import numpy as np
import matplotlib.pyplot as plt

# Simulate 30 days of temperature data using NumPy (in °C)
np.random.seed(42)  # for consistent results
days = np.arange(1, 31)
temperatures = np.random.normal(loc=32, scale=3, size=30)  # avg 32°C ± 3°C

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='teal')
plt.title('Simulated Daily Temperature - 30 Days')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()

# Save the image
plt.savefig('numpy_temperature_plot.png')
plt.show()
