import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# === CONFIGURATION ===
PORT = 'COM3'  # Replace with your serial port (e.g., /dev/ttyUSB0 on Linux)
BAUD_RATE = 115200
NUM_SENSORS = 6
ANGLE_START = 0
ANGLE_INCREMENT = 30  # Adjust based on physical sensor angle spacing

# === INIT SERIAL ===
try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"Connected to {PORT} at {BAUD_RATE} baud.")
except:
    print(f"⚠️ ERROR: Could not connect to {PORT}")
    exit()

# === INIT PLOT ===
plt.ion()
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-100, 100)
ax.set_ylim(0, 150)
ax.set_title("Ultrasonic Array Shape Detection (Top View)")
sc = ax.scatter([], [], c='red', s=60)

def polar_to_cartesian(angle_deg, distance_cm):
    rad = np.deg2rad(angle_deg)
    x = distance_cm * np.cos(rad)
    y = distance_cm * np.sin(rad)
    return x, y

def update_plot(angles, distances):
    xs, ys = [], []
    for a, d in zip(angles, distances):
        x, y = polar_to_cartesian(a, d)
        xs.append(x)
        ys.append(y)
    sc.set_offsets(np.c_[xs, ys])
    fig.canvas.draw()
    fig.canvas.flush_events()

# === MAIN LOOP ===
angles = []
distances = []

print("🛰️ Reading data from ESP32...")
while True:
    try:
        line = ser.readline().decode().strip()
        if line == '':
            continue
        if line.startswith('---'):  # New scan starts
            if len(angles) == NUM_SENSORS:
                update_plot(angles, distances)
            angles, distances = [], []
        else:
            parts = line.split(',')
            if len(parts) == 2:
                angle = int(parts[0].strip())
                distance = int(parts[1].strip())
                angles.append(angle)
                distances.append(distance)
    except KeyboardInterrupt:
        print("\n🔌 Exiting...")
        break
    except Exception as e:
        print(f"Error: {e}")
