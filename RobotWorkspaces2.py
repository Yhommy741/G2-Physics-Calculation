import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
L1 = 40  # Link 1 length (cm)
L2 = 30  # Link 2 length (cm)
base_height = 15  # cm

# Angle ranges in radians
theta1_range = np.radians(np.linspace(0, 180, 300))
theta2_range = np.radians(np.linspace(0, 180, 300))

# Generate grid of angles
theta1, theta2 = np.meshgrid(theta1_range, theta2_range)

# Forward kinematics for workspace
x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
y = base_height + L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)

# Pose to draw robot structure
theta1_deg = 30
theta2_deg = 30
θ1 = np.radians(theta1_deg)
θ2 = np.radians(theta2_deg)

# Joint positions
x0, y0 = 0, base_height  # base
x1 = x0 + L1 * np.cos(θ1)
y1 = y0 + L1 * np.sin(θ1)
x2 = x1 + L2 * np.cos(θ1 + θ2)
y2 = y1 + L2 * np.sin(θ1 + θ2)

# --- Plot ---
plt.figure(figsize=(8, 8))

# Plot workspace
plt.plot(x, y, '.', markersize=0.5, alpha=0.4)

# Plot robot in pose (θ1=45°, θ2=45°)
plt.plot([x0, x1], [y0, y1], 'r-', linewidth=4, label='Link 1')
plt.plot([x1, x2], [y1, y2], 'b-', linewidth=4, label='Link 2')
plt.plot(x0, y0, 'ko', markersize=8, label='Joint 1')
plt.plot(x1, y1, 'ko', markersize=8, label='Joint 2')

# Decorate
plt.title(f"2 Links Robot Workspace")
plt.xlabel("X position (cm)")
plt.ylabel("Y position (cm)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()