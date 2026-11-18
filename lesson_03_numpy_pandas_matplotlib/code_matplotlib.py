import numpy as np
import matplotlib.pyplot as plt



# 1. The simplest line plot
x = np.linspace(0, 5, 6)
y = x**2
plt.figure()
plt.plot(x, y, 'o-')
plt.title("Quadratic function")
plt.xlabel("Temperature (C)")
plt.ylabel("$ Resistance (\Omega) $")
plt.grid()
plt.show()


# 2. Comparing multiple curves
x = np.linspace(0, 2 * np.pi, 200)
plt.figure()
plt.plot(x, np.sin(x), label="sine", color="blue")
plt.plot(x, np.cos(x), label="cosine", linestyle="--", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.legend()
plt.grid(True)
plt.show()


# 3. Basic customizations
plt.figure(figsize=(8, 3))
plt.plot(x, np.sin(x), marker="^", markersize=3, linewidth=1.5)
plt.title("Sinusoidal signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid(True, linestyle="dashdot")
plt.show()



# 4. Other plot types: bars
categories = ["A", "B", "C", "D"]
values = [4, 7, 5, 8]
plt.figure()
plt.bar(categories, values)
plt.title("Comparison by category")
plt.xlabel("categories")
plt.ylabel("values")
plt.show()
 

# 5. Other plot types: scatter
x_measured = np.array([1, 2, 3, 4, 5, 6, 7])
y_measured = np.array([2.0, 2.5, 3.7, 3.9, 5.1, 5.5, 6.8])
plt.figure()
plt.scatter(x_measured, y_measured)
plt.title("Scatter between measurements")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# 6. Other plot types: histogram
samples = np.array([4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 9, 10, 10, 11])
plt.figure()
plt.hist(samples, bins=8, edgecolor="black")
plt.title("Distribution of the samples")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()