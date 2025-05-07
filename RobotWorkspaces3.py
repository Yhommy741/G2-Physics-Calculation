import numpy as np
import matplotlib.pyplot as plt

# Link lengths
L1 = 425  # mm
L2 = 275  # mm

# Angle ranges
theta1_range = np.radians(np.linspace(-132, 132, 300))
theta2_range = np.radians(np.linspace(-145, 145, 300))

# Generate grid of angles
theta1, theta2 = np.meshgrid(theta1_range, theta2_range)

# Forward kinematics (planar)
x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)

# Specific pose (e.g., θ₁=45°, θ₂=45°)
theta1_deg = 132
theta2_deg = 0
θ1 = np.radians(theta1_deg)
θ2 = np.radians(theta2_deg)

# Joint positions
x0, y0 = 0, 0  # base
x1 = x0 + L1 * np.cos(θ1)
y1 = y0 + L1 * np.sin(θ1)
x2 = x1 + L2 * np.cos(θ1 + θ2)
y2 = y1 + L2 * np.sin(θ1 + θ2)

# Plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, '.', markersize=0.5, alpha=0.4)

# Plot links and joints
plt.plot([x0, x1], [y0, y1], 'r-', linewidth=4, label='Link 1')
plt.plot([x1, x2], [y1, y2], 'b-', linewidth=4, label='Link 2')
plt.plot(x0, y0, 'ko', markersize=8, label='Base Joint')
plt.plot(x1, y1, 'ko', markersize=8, label='Joint 2')
plt.plot(x2, y2, 'go', markersize=10, label='End Effector')

# Decorations
plt.title(f"SCARA Robot KR6 R700 Z200 ")
plt.xlabel("X position (mm)")
plt.ylabel("Y position (mm)")
plt.axis("equal")
plt.grid(True)
plt.show()