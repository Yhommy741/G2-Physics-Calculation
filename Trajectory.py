import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

# Constants
g = 9.81  # Gravity (m/s^2)
S_x_max = 2.65  # m
h_drop = 2  # m
h_hit = 0.4  # m
m_ball = 0.024
e = 0.378
I_bat = 0.024
r = 0.4

# Free Falling of Squash ball
u_y = -math.sqrt(2 * g * (h_drop - h_hit))  # m/s

# Assume Suitable Projectile motion for longest Range
thetaV = 40.71  # deg
float_time = math.sqrt((2 * (S_x_max * math.tan(math.radians(thetaV)) + h_hit)) / g)
v_x = S_x_max / float_time
v_y = math.sqrt((v_x / math.cos(math.radians(thetaV)))**2 - v_x**2)

# Find ThetaB for suitable Projectile motion for longest Range
thetaB = math.atan(v_x / (v_y + abs(u_y)))  # Radians
u_per = u_y * math.cos(thetaB)
u_par = u_y * math.sin(thetaB)

v_per = (v_x - abs(u_par) * math.cos(thetaB)) / math.sin(thetaB)

# Find angular velocity (w) of the bat during collision
A = I_bat * (1 + e)
B = e * I_bat / r - m_ball * r
C = I_bat / r - m_ball * r

w_i = (B * u_per + C * v_per) / A

# Function to calculate S_x given thetaB
def calculate_S_x(thetaB_deg):
    thetaB_rad = math.radians(thetaB_deg)
    term1 = (A * w_i - B * u_y * math.cos(thetaB_rad)) / C
    term2 = abs(u_y) * math.sin(thetaB_rad)
    
    v_x_expr = term1 * math.sin(thetaB_rad) + term2 * math.cos(thetaB_rad)
    v_y_expr = term1 * math.cos(thetaB_rad) - term2 * math.sin(thetaB_rad)
    
    time_expr = (v_y_expr + math.sqrt(v_y_expr**2 + 2 * g * h_hit)) / g
    S_x = v_x_expr * time_expr
    return S_x

# Function to find thetaB that gives a specific S_x
def find_thetaB(S_x_target):
    def equation(thetaB_deg):
        return calculate_S_x(thetaB_deg) - S_x_target
    return fsolve(equation, x0=30)  # Initial guess for thetaB

# Desired S_x values
S_x_values = [0.94, 1.32, 1.7, 2.08, 2.46]

# Find corresponding thetaB values
thetaB_values = [find_thetaB(S_x_target)[0] for S_x_target in S_x_values]

# Function to calculate projectile motion
def projectile_path(thetaB, v_x, v_y):
    t_flight = (v_y + math.sqrt(v_y**2 + 2 * g * h_hit)) / g
    t = np.linspace(0, t_flight, num=100)
    x = v_x * t
    y = h_hit + v_y * t - 0.5 * g * t**2
    return x, y

# Compute and plot trajectories
plt.figure(figsize=(10, 6))  # Wider figure for better spacing
colors = ['#6495ED', '#27ae60', '#f4d03f', '#f39c12', '#e74c3c']  # Light blue, Green, Yellow, Orange, Red

for i, S_x in enumerate(S_x_values):
    thetaB = thetaB_values[i]
    thetaB_rad = math.radians(thetaB)
    
    # Calculate v_x and v_y using the derived expressions
    term1 = (A * w_i - B * u_y * math.cos(thetaB_rad)) / C
    term2 = abs(u_y) * math.sin(thetaB_rad)
    
    v_x = term1 * math.sin(thetaB_rad) + term2 * math.cos(thetaB_rad)
    v_y = term1 * math.cos(thetaB_rad) - term2 * math.sin(thetaB_rad)
    
    # Calculate trajectory
    x, y = projectile_path(thetaB_rad, v_x, v_y)
    plt.plot(x, y, label=f'ThetaB = {thetaB:.2f}°', color=colors[i], linewidth=2)

# Graph Labels
plt.xlabel("Horizontal Distance (m)", fontsize=12, fontweight='bold')
plt.ylabel("Vertical Distance (m)", fontsize=12, fontweight='bold')
plt.title("Projectile Trajectory for Different Goals", fontsize=14, fontweight='bold')

# Legend
plt.legend(loc='upper right', fontsize=10, frameon=True, shadow=True, bbox_to_anchor=(1.25, 1))  # Move legend outside

# Grid
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Background color
plt.gca().set_facecolor('#f7f7f7')  # Light gray background

# Add padding
plt.tight_layout()

# Show plot
plt.show()