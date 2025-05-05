import numpy as np
import matplotlib.pyplot as plt

# Link lengths
L1 = 70
L2 = 50

# Joint angle ranges (degrees to radians)
theta1_range = np.radians(np.linspace(0, 180, 300))
theta2_range = np.radians(np.linspace(-90, 270, 300))

# Meshgrid for all joint configurations
theta1, theta2 = np.meshgrid(theta1_range, theta2_range)

# Workspace calculation
x_ws = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
y_ws = 50 + L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)

# --- Start Pose: θ1 = 0, θ2 = 0 ---
theta1_start = np.radians(0)
theta2_start = np.radians(0)

x0, y0 = 0, 50  # Base joint
x1 = x0 + L1 * np.cos(theta1_start)
y1 = y0 + L1 * np.sin(theta1_start)

x2 = x1 + L2 * np.cos(theta1_start + theta2_start)
y2 = y1 + L2 * np.sin(theta1_start + theta2_start)

# --- Plot ---
plt.figure(figsize=(8, 8))

# Workspace dots
plt.plot(x_ws, y_ws, '.', markersize=0.5, alpha=0.4)

# Robot arm in start pose
plt.plot([x0, x1], [y0, y1], 'r-', linewidth=4, label="Link 1")
plt.plot([x1, x2], [y1, y2], 'b-', linewidth=4, label="Link 2")
plt.plot(x0, y0, 'ko', markersize=8)  # Joint 1
plt.plot(x1, y1, 'ko', markersize=8)  # Joint 2

# Decorations
plt.title("2 Links Robot Arm")
plt.xlabel("X Position (mm)")
plt.ylabel("Y Position (mm)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()