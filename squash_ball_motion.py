import numpy as np
import matplotlib.pyplot as plt
import math

# Constant variables
g = 9.81  # m/s^2
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
v_y =  math.sqrt((v_x/math.cos(math.radians(thetaV)))**2 - v_x**2)

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

# Find relation between S_x and thetaB
X = np.linspace(0, 90, 1000)  # Angle in degrees
X_rad = np.radians(X)  # Convert to radians for calculations

term1 = (A * w_i - B * u_y * np.cos(X_rad)) / C
term2 = abs(u_y) * np.sin(X_rad)

v_x_expr = term1 * np.sin(X_rad) + term2 * np.cos(X_rad)
v_y_expr = term1 * np.cos(X_rad) - term2 * np.sin(X_rad)

time_expr = (v_y_expr + np.sqrt(v_y_expr**2 + 2 * g * h_hit)) / g
S_x = v_x_expr * time_expr 

# Plot results
fig, ax = plt.subplots()
ax.plot(X, S_x)
ax.set_xlabel("Degree of Racket (Degree)")
ax.set_ylabel("Distance the ball falls (m)")
plt.grid()
plt.show()