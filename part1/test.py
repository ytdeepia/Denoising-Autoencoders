# %%
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

# Define parameters for the two Gaussian components
mu1 = np.array([1, 1])  # Mean of the first Gaussian
sigma1 = np.array([[0.5, 0], [0, 0.5]])  # Covariance of the first Gaussian
pi1 = 0.5  # Weight of the first Gaussian

mu2 = np.array([-1, -1])  # Mean of the second Gaussian
sigma2 = np.array([[0.5, 0], [0, 0.5]])  # Covariance of the second Gaussian
pi2 = 0.5  # Weight of the second Gaussian


# Multivariate Gaussian PDF
def gaussian_pdf(x, mu, sigma):
    d = x.shape[0]
    det_sigma = np.linalg.det(sigma)
    inv_sigma = np.linalg.inv(sigma)
    norm_const = 1 / (np.sqrt((2 * np.pi) ** d * det_sigma))
    diff = x - mu
    return norm_const * np.exp(-0.5 * diff.T @ inv_sigma @ diff)


# Gradient of the log PDF of a single Gaussian
def gradient_log_gaussian(x, mu, sigma):
    inv_sigma = np.linalg.inv(sigma)
    return -inv_sigma @ (x - mu)


# Mixture PDF
def mixture_pdf(x):
    return pi1 * gaussian_pdf(x, mu1, sigma1) + pi2 * gaussian_pdf(x, mu2, sigma2)


# Gradient of the log PDF of the mixture
def gradient_log_mixture(x):
    p1 = gaussian_pdf(x, mu1, sigma1)
    p2 = gaussian_pdf(x, mu2, sigma2)
    p = pi1 * p1 + pi2 * p2
    grad1 = gradient_log_gaussian(x, mu1, sigma1)
    grad2 = gradient_log_gaussian(x, mu2, sigma2)
    return (pi1 * p1 * grad1 + pi2 * p2 * grad2) / p


# Generate a grid of points for the vector field
x_range = np.linspace(-3, 3, 20)
y_range = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x_range, y_range)
points = np.stack([X.ravel(), Y.ravel()], axis=-1)

# Compute the gradient at each point
gradients = np.array([gradient_log_mixture(point) for point in points])
U = gradients[:, 0].reshape(X.shape)
V = gradients[:, 1].reshape(X.shape)

print(gradients)
# Plot the vector field
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, color="blue")
plt.title("Gradient of Log Probability (Score Function)")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
plt.show()


# %%
# Load the image
image_path = "./img/original_2.png"
image = Image.open(image_path)

# Convert the image to a tensor
transform = transforms.Compose([transforms.ToTensor(), transforms.Grayscale()])
image_tensor = transform(image)

# Add Gaussian noise
mean = 0
std = 30 / 255
noise = torch.randn_like(image_tensor) * std + mean
noisy_image_tensor = image_tensor + noise

# Clip the values to be between 0 and 1
noisy_image_tensor = torch.clamp(noisy_image_tensor, 0, 1)

# Convert the tensor back to an image
transform_to_pil = transforms.ToPILImage()
noisy_image = transform_to_pil(noisy_image_tensor)

# Display the original and noisy images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Noisy Image")
plt.imshow(noisy_image, cmap="gray")
plt.axis("off")

plt.show()

noisy_image.save("./img/noisy_2.png")

# %%
# Load the image again
image = Image.open(image_path)

# Convert the image to a tensor
image_tensor = transform(image)

# Add Poisson noise
lam = 0.5  # Lambda parameter for Poisson distribution
poisson_noise = torch.poisson(image_tensor * lam) / lam
noisy_image_tensor_poisson = image_tensor + poisson_noise

# Clip the values to be between 0 and 1
noisy_image_tensor_poisson = torch.clamp(noisy_image_tensor_poisson, 0, 1)

# Convert the tensor back to an image
noisy_image_poisson = transform_to_pil(noisy_image_tensor_poisson)

# Display the original and noisy images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Noisy Image with Poisson Noise")
plt.imshow(noisy_image_poisson, cmap="gray")
plt.axis("off")

plt.show()

noisy_image_poisson.save("./img/cameraman_poisson.jpg")

# %%
# Load the image again
image = Image.open(image_path)

# Convert the image to a tensor
image_tensor = transform(image)

# Add Inverse Gamma noise
alpha = 0.2  # Shape parameter for Inverse Gamma distribution
beta = 2.0  # Scale parameter for Inverse Gamma distribution
inverse_gamma_noise = torch.from_numpy(
    np.random.standard_gamma(alpha, size=image_tensor.shape) / beta
).float()
noisy_image_tensor_inverse_gamma = image_tensor + inverse_gamma_noise

# Clip the values to be between 0 and 1
noisy_image_tensor_inverse_gamma = torch.clamp(noisy_image_tensor_inverse_gamma, 0, 1)

# Convert the tensor back to an image
noisy_image_inverse_gamma = transform_to_pil(noisy_image_tensor_inverse_gamma)

# Display the original and noisy images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Noisy Image with Inverse Gamma Noise")
plt.imshow(noisy_image_inverse_gamma, cmap="gray")
plt.axis("off")

plt.show()

noisy_image_inverse_gamma.save("./img/cameraman_inverse_gamma.jpg")

""

# %%
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Generate random 28x28 grayscale images
num_images = 5
image_size = (28, 28)

random_images = []
for _ in range(num_images):
    random_image = np.random.rand(*image_size)
    random_images.append(random_image)

# Display the random images
plt.figure(figsize=(12, 6))
for i, random_image in enumerate(random_images):
    plt.subplot(1, num_images, i + 1)
    plt.title(f"Random Image {i+1}")
    plt.imshow(random_image, cmap="gray")
    plt.axis("off")

plt.show()

# Save the random images
for i, random_image in enumerate(random_images):
    image_path = f"./img/random_image_{i+1}.png"
    plt.imsave(image_path, random_image, cmap="gray")


# %%
def create_shape_image(shape, image_size=(28, 28)):
    image = np.zeros(image_size, dtype=np.uint8)
    if shape == "square":
        top_left = (7, 7)
        bottom_right = (21, 21)
        cv2.rectangle(image, top_left, bottom_right, 255, -1)
    elif shape == "circle":
        center = (14, 14)
        radius = 7
        cv2.circle(image, center, radius, 255, -1)
    return image


shapes = ["square", "circle"]
shape_images = []

for shape in shapes:
    shape_image = create_shape_image(shape)
    shape_images.append(shape_image)

# Display the shape images
plt.figure(figsize=(12, 6))
for i, shape_image in enumerate(shape_images):
    plt.subplot(1, len(shape_images), i + 1)
    plt.title(f"{shapes[i].capitalize()}")
    plt.imshow(shape_image, cmap="gray")
    plt.axis("off")

plt.show()

# %%
# Save the shape images
for i, shape_image in enumerate(shape_images):
    shape_name = shapes[i]
    image_path = f"./img/{shape_name}.png"
    cv2.imwrite(image_path, shape_image)

# %%
import numpy as np
import matplotlib.pyplot as plt


# Define the parametric 1D curve: y = 0.5*sin(x) + 0.2*x
def curve(x):
    return 0.5 * np.sin(x) + 0.2 * x


# Derivative of the curve (gradient of the manifold)
def curve_gradient(x):
    return 0.5 * np.cos(x) + 0.2


# Project a point onto the curve
def project_onto_curve(x, y):
    y_curve = curve(x)
    return x, y_curve


# Compute the "score" (direction toward the curve)
def score(x, y):
    _, y_proj = project_onto_curve(x, y)
    grad = curve_gradient(x)
    dx = 1 / (1 + grad**2)
    dy = grad / (1 + grad**2)
    # Direction pointing toward the curve
    delta_x = dx * (x - x)
    delta_y = dy * (y_proj - y)
    return delta_x, delta_y


# Generate points around the curve
np.random.seed(42)
x_points = np.random.uniform(-np.pi, np.pi, 20)
y_points = curve(x_points) + np.random.uniform(-0.5, 0.5, 20)

# Generate curve points for plotting
x_curve = np.linspace(-np.pi, np.pi, 500)
y_curve = curve(x_curve)

# Plot the curve
plt.figure(figsize=(10, 6))
plt.plot(x_curve, y_curve, label="1D Curve: $y=0.5\\sin(x)+0.2x$", color="blue", lw=2)

# Plot the points and their scores
for x, y in zip(x_points, y_points):
    dx, dy = score(x, y)
    plt.arrow(x, y, dx, dy, head_width=0.05, head_length=0.1, color="red")
    plt.scatter(
        x,
        y,
        color="yellow",
        label=(
            "Noisy Points"
            if "Noisy Points" not in plt.gca().get_legend_handles_labels()[1]
            else None
        ),
    )

# Decorations
plt.scatter(
    x_points, [curve(x) for x in x_points], color="green", label="Projected Points"
)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Score Vectors Pointing Toward the Curve")
plt.grid(True)
plt.show()
