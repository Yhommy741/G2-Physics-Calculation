import matplotlib.pyplot as plt

# Sample data
voltage = [48.21, 48.23, 48.22, 48.21, 48.16, 48.12, 47.96, 47.97, 47.86, 47.76, 47.71, 47.56, 47.49, 47.40, 47.25, 47.17, 47.04]
torque = [0.057, 0.076, 0.114, 0.182, 0.288, 0.447, 0.671, 0.938, 1.274, 1.648, 2.019, 2.421, 2.827, 3.302, 3.804, 4.312, 4.785]
rpm = [3218.00, 3218.00, 3215.00, 3210.00, 3203.00, 3191.00, 3175.00, 3156.00, 3133.00, 3106.00, 3080.00, 3051.00, 3022.00, 2989.00, 2953.00, 2917.00, 2883.00]
current = [1.56, 1.68, 1.97, 2.44, 3.15, 4.23, 5.72, 7.70, 10.06, 12.71, 15.42, 18.30, 20.97, 24.38, 28.40, 31.89, 35.48]
InPower = [75.38, 81.22, 95.12, 117.4, 151.6, 203.3, 274.2, 369.5, 481.4, 607.1, 735.8, 870.5, 995.6, 1156, 1342, 1504, 1669]
OutPower = [19.21, 25.61, 38.38, 61.18, 96.59, 149.4, 223.1, 310.1, 417.9, 536.1, 651.2, 773.6, 894.8, 1033, 1176, 1317, 1445]
efficiency = [25.48, 31.53, 40.35, 52.10, 63.72, 73.48, 81.37, 83.92, 86.81, 88.30, 88.50, 88.87, 89.87, 89.42, 87.65, 87.56, 86.57]

# Create the plot
fig, axRPM = plt.subplots(figsize=(12, 8))

# RPM (Primary Y-axis)
axRPM.plot(torque, rpm, 'firebrick', label='RPM')
axRPM.set_xlabel('Torque (N.m)')
axRPM.set_ylabel('RPM', color='firebrick')
axRPM.tick_params(axis='y', labelcolor='firebrick')
axRPM.set_ylim(2800, 3300)
axRPM.set_xlim(0, 5.0)
axRPM.grid(True, linestyle='--', alpha=0.6)

# Voltage (Secondary Y-axis)
axV = axRPM.twinx()
axV.plot(torque, voltage, 'goldenrod', label='Voltage (V)')
axV.set_ylabel('Voltage (V)', color='goldenrod')
axV.tick_params(axis='y', labelcolor='goldenrod')
axV.set_ylim(0, 60)

# Current (Secondary Y-axis)
axA = axRPM.twinx()
axA.plot(torque, current, 'g', label='Current (A)')
axA.set_ylabel('Current (A)', color='g')
axA.tick_params(axis='y', labelcolor='g')
axA.set_ylim(0, 40)
axA.spines['right'].set_position(('outward', 60))

# # Input Power (Secondary Y-axis)
# axInPower = axRPM.twinx()
# axInPower.plot(torque, InPower, 'goldenrod', label='Input Power (W)')
# axInPower.set_ylabel('Input Power (W)', color='goldenrod')
# axInPower.tick_params(axis='y', labelcolor='goldenrod')
# axInPower.set_ylim(0, 1500)
# axInPower.spines['right'].set_position(('outward', 120))

# # Output Power (Secondary Y-axis)
# axOutPower = axRPM.twinx()
# axOutPower.plot(torque, OutPower, 'goldenrod', label='Output Power (W)')
# axOutPower.set_ylabel('Output Power (W)', color='goldenrod')
# axOutPower.tick_params(axis='y', labelcolor='goldenrod')
# axOutPower.set_ylim(0, 1500)
# axOutPower.spines['right'].set_position(('outward', 180))

# Efficiency (Secondary Y-axis)
axEff = axRPM.twinx()
axEff.plot(torque, efficiency, 'royalblue', label='Efficiency (%)')
axEff.set_ylabel('Efficiency (%)', color='royalblue')
axEff.tick_params(axis='y', labelcolor='royalblue')
axEff.set_ylim(0, 100)
axEff.spines['right'].set_position(('outward', 120))

# Combine legends
lines, labels = axRPM.get_legend_handles_labels()
lines2, labels2 = axV.get_legend_handles_labels()
lines3, labels3 = axA.get_legend_handles_labels()
lines4, labels4 = axEff.get_legend_handles_labels()
axRPM.legend(lines + lines2 + lines3 + lines4 , labels + labels2 + labels3 + labels4 , loc='lower right', bbox_to_anchor=(1.0, 0))

# Add title and adjust layout
plt.title('Ningbo Volcano Electric Co ., Ltd | Motor M099 Performance Characteristics', pad=20)
fig.tight_layout()
plt.show()