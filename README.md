# 🤖 ROS2-Based Control System for Differential Drive Rover

This repository documents the development of a differential drive rover control system for the **BRACU Mongol Tori** Mars Rover. The project evolved from a simple Arduino-based implementation using PySerial to a robust ROS2–Pixhawk architecture using MAVLink and long-range telemetry.

---

## 📁 Repository Structure

### `mt_main_10.0_ros2_diff_drive_v1`
> **Stage 1: Arduino + BTS7960 + ROS2 (PySerial)**

- Implemented differential drive control using **Arduino UNO**.
- **BTS7960** H-bridge motor driver used for brushed motor control.
- Communication between **Arduino** and **ROS2 (Humble)** via **PySerial**.
- ROS2 nodes handled velocity commands and encoder feedback.
- Suitable for early prototyping and basic testing.

### `mt_rover_wheel`
> **Stage 2: Pixhawk + pymavlink + ROS2**

- Shifted to **Pixhawk** for robust control, safety, and telemetry.
- Used **`pymavlink`** to interface ROS2 with Pixhawk via MAVLink protocol.
- MAVLink communication scripts follow [ArduSub Developer Guide](https://www.ardusub.com/developers/pymavlink.html).
- Motor control signals routed through **Cytron MDDS60** brushed motor driver.
- Full MAVLink message handling for motor commands, feedback, and telemetry.

---

## ⚙️ Hardware Components

### ✅ **BTS7960 Motor Driver** (Initial Phase)
- Dual-channel H-bridge brushed motor driver.
- Controlled via PWM and DIR pins from Arduino.
- Used for the Arduino-based system in early development.

### ✅ **Cytron MDDS60 Motor Driver** (Final Phase)
- Dual-channel 60A brushed motor driver.
- Supports Serial, PWM, RC, and Analog control.
- Used with Pixhawk + ROS2 system for robust and reliable motor control.
- Product page: [Cytron MDDS60 (SmartDrive 60A, 2-Channel)](https://www.cytron.io/p-60amp-7v-45v-smartdrive-dc-motor-driver-2-channels)

### ✅ **Pixhawk Flight Controller**
- Acts as the central control and telemetry hub.
- Runs ArduRover firmware.
- Communicates with ROS2 nodes via MAVLink and serial interfaces.
- Enables mode switching, sensor integration, and failsafe features.

### ✅ **Telemetry Modules**

#### • **SiK Telemetry V3** (Early Testing)
- 900 MHz telemetry radio.
- Enabled wireless MAVLink communication for short-range development and testing.

#### • **P900** (Final Deployment)
- High-power, long-range telemetry module.
- Replaced SiK for robust field testing.
- Ensured reliable MAVLink communication across large distances.

### ✅ **Companion Computer**
- Runs **ROS2 Humble**.
- Hosts custom ROS2 nodes, including:
  - `pymavlink` integration
  - Differential drive logic
  - Sensor interfacing (IMU, encoder)
- Communicates with Pixhawk via serial or USB.

---

## 🧠 Why the Shift from Arduino to Pixhawk?

While the Arduino solution was fast and flexible, it lacked:

- Long-range wireless telemetry
- Built-in failsafe and mode switching
- Real-time sensor integration at scale

Switching to **Pixhawk + pymavlink** allowed us to take advantage of the MAVLink protocol, Mission Planner, and robust field-tested firmware — all while staying within the ROS2 framework.

---

## 🧑‍💻 Developer Notes

> Special thanks to the **BRACU Duburi Team** for providing internal MAVLink documentation and guidance that accelerated the Pixhawk–pymavlink integration process.

---

## 📚 References

- [ArduSub pymavlink Documentation](https://www.ardusub.com/developers/pymavlink.html)  
- [Cytron MDDS60 – SmartDrive 60A, 2-Channels](https://www.cytron.io/p-60amp-7v-45v-smartdrive-dc-motor-driver-2-channels)  
- [ROS2 Humble Documentation](https://docs.ros.org/en/humble/index.html)

---

## 🚀 Project Context

- Built for the **University Rover Challenge (URC)**
- Team: **BRACU Mongol Tori**
- Role: Main Driver & Control System Developer
- Focus: Field-ready, modular, and robust rover control architecture

---

## 👤 Maintainer

**Md Jesan**  
GitHub: [@mdJesan-08](https://github.com/mdJesan-08)  
Main control system developer and rover driver  
BRAC University | BRACU Mongol Tori

---
