# 🛰️ Ultrasonic Sensor Array-Based Shape Detection System (Servo-Free)

This project is a real-time 2D shape detection system built using a static array of ultrasonic sensors (HC-SR04) connected to an ESP32 microcontroller. The system detects object profiles (walls, curves, people, corners) by analyzing the distance readings from multiple fixed-angle sensors, creating a rudder-style scan without any servo motors.

---

## 🧠 Features

- ✅ Multi-directional object detection using 5–8 ultrasonic sensors
- ✅ No moving parts — fixed sensor array for better speed & durability
- ✅ Real-time shape approximation (curved, flat, corner detection)
- ✅ Data visualization in Python (radar/point plot)
- ✅ Expandable design — add more sensors easily
- ✅ Optional OLED/LCD display support

---

## 🛠️ Hardware Requirements

| Component           | Quantity | Description                         |
|---------------------|----------|-------------------------------------|
| ESP32 Dev Board     | 1        | Core microcontroller (e.g., DOIT ESP32 DEVKIT V1) |
| HC-SR04 Ultrasonic Sensors | 5–8    | For directional distance sensing    |
| Jumper Wires        | Many     | For all GPIO connections            |
| Breadboard          | 1        | Or custom PCB setup                 |
| 5V Power Source     | 1        | USB power or battery pack           |
| (Optional) OLED/LCD | 1        | For local display output            |

---

## 🔌 Wiring (Example with 6 Sensors)

| Sensor | TRIG Pin | ECHO Pin |
|--------|----------|----------|
| S1     | GPIO12   | GPIO13   |
| S2     | GPIO14   | GPIO27   |
| S3     | GPIO26   | GPIO25   |
| S4     | GPIO33   | GPIO32   |
| S5     | GPIO22   | GPIO21   |
| S6     | GPIO19   | GPIO18   |

> **Note**: Adjust pins in the code to match your layout.

---

## 🧩 How It Works

1. Each sensor measures distance in a specific fixed direction.
2. Data is collected in real-time from all sensors.
3. Output is sent over serial (USB) to PC.
4. A Python script reads the data and plots the shape as a 2D radar/contour map.
5. Optional: The ESP32 can also send distance/shape type to an OLED screen.

---

## 📦 Folder Structure

```bash
├── Arduino_Code/
│   └── ultrasonic_array_shape.ino
├── Python_Visualizer/
│   └── shape_plotter.py
├── docs/
│   ├── schematic_diagram.png
│   └── wiring_diagram.pdf
├── images/
│   ├── demo_output_plot.png
│   └── hardware_setup_photo.jpg
└── README.md
