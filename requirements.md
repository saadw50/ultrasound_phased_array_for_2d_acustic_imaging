# 🧰 Project Requirements

This file outlines all the necessary components, software tools, and libraries needed to build and run the **Ultrasonic Sensor Array-Based Shape Detection Rudder** project (ESP32 + Python, No Servo, No ML).

---

## 🧩 Hardware Requirements

| Component                    | Quantity | Notes                          |
|-----------------------------|----------|--------------------------------|
| ESP32 Dev Board             | 1        | Any ESP32 (e.g., DOIT V1)      |
| HC-SR04 Ultrasonic Sensors  | 5–8      | Use fixed angular placement    |
| Breadboard or PCB           | 1        | For sensor connections         |
| Jumper Wires (Male–Male)    | ~40      | For GPIO connections           |
| 5V USB Power Source / Cable | 1        | Power ESP32 and sensors        |
| Optional: OLED (SSD1306/I2C)| 1        | Display distance/angle live   |

---

## 🖥️ Software Requirements

### 1. 🧠 Arduino IDE / PlatformIO
For uploading the main microcontroller code to ESP32.

- Install from: [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)

#### Arduino Board Manager Setup:
- Install `ESP32` board support from Espressif

#### Arduino Libraries:
Install the following via **Library Manager**:
- `NewPing` (for managing HC-SR04 easily)
- `Adafruit SSD1306` *(if using OLED)*
- `Adafruit GFX` *(for OLED graphics)*
- `Wire.h` *(already included)*

---

### 2. 🐍 Python 3.x (on your PC)

Required to visualize the sensor data in real-time.

> You can use Anaconda or plain Python

#### Python Libraries (Install with pip):

```bash
pip install pyserial matplotlib numpy
