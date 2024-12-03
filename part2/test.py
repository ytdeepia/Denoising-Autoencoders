# %%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from scipy.ndimage import gaussian_filter
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Generate Original Data
np.random.seed(42)  # For reproducibility

# Parameters for two 2D Gaussians
mean1 = [-2, -2]
cov1 = [[1, 0], [0, 1]]  # Identity matrix

mean2 = [2, 2]
cov2 = [[1, 0], [0, 1]]

# Sample data from the two Gaussians
data1 = np.random.multivariate_normal(mean1, cov1, 5000)
data2 = np.random.multivariate_normal(mean2, cov2, 5000)

# Combine the data
original_data = np.vstack((data1, data2))

# Step 2: Add Gaussian Noise
# Noise parameters
noise_mean = [0, 0]
noise_cov = [[0.5, 0], [0, 0.5]]  # Smaller variance

# Generate Gaussian noise
noise = np.random.multivariate_normal(noise_mean, noise_cov, original_data.shape[0])

# Add noise to the original data
noised_data = original_data + noise

# Step 3: Estimate PDFs


# Function to estimate pdf using KDE
def estimate_pdf(data, grid_size=100):
    x_min, x_max = data[:, 0].min() - 3, data[:, 0].max() + 3
    y_min, y_max = data[:, 1].min() - 3, data[:, 1].max() + 3

    X, Y = np.mgrid[x_min : x_max : grid_size * 1j, y_min : y_max : grid_size * 1j]
    positions = np.vstack([X.ravel(), Y.ravel()])
    kernel = gaussian_kde(data.T)
    Z = np.reshape(kernel(positions).T, X.shape)
    return X, Y, Z


# Estimate pdf of the original data
X_orig, Y_orig, Z_orig = estimate_pdf(original_data)

# Estimate pdf of the noised data
X_noised, Y_noised, Z_noised = estimate_pdf(noised_data)

# Step 4: Convolve Original PDF with Gaussian Kernel
# Use a Gaussian filter to convolve the original pdf
sigma = 5  # Standard deviation for Gaussian kernel
Z_convolved = gaussian_filter(Z_orig, sigma=sigma)

# Visualization
fig = plt.figure(figsize=(18, 5))

# Original PDF
ax1 = fig.add_subplot(1, 3, 1, projection="3d")
ax1.plot_surface(X_orig, Y_orig, Z_orig, cmap="viridis")
ax1.set_title("Original PDF")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Probability Density")

# Noised Data PDF
ax2 = fig.add_subplot(1, 3, 2, projection="3d")
ax2.plot_surface(X_noised, Y_noised, Z_noised, cmap="viridis")
ax2.set_title("PDF of Noised Data")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Probability Density")

# Convolved PDF
ax3 = fig.add_subplot(1, 3, 3, projection="3d")
ax3.plot_surface(X_orig, Y_orig, Z_convolved, cmap="viridis")
ax3.set_title("Convolved PDF")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("Probability Density")

plt.tight_layout()
plt.show()
