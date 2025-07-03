# 🤖 ROS2-Based Control System for Differential Drive Rover

This repository documents the development of a custom control system for a Mars Rover built by **BRACU Mongol Tori**. It includes two major stages of implementation: starting with an Arduino–ROS2-based system using PySerial, and transitioning to a MAVLink-based control architecture using Pixhawk and `pymavlink`.

---

## 📁 Repository Structure

### `ros2_diff_drive_V1`
> **Stage 1: Arduino + ROS2 + PySerial**

- Implemented basic differential drive system.
- Communication between **Arduino** and **ROS2 (Humble)** via `pyserial`.
- Encoder, IMU, and motor control data were transferred over USB serial.
- ROS2 publishers and subscribers handled sensor feedback and motor commands.

### `mt`
> **Stage 2: Pixhawk + ROS2 + pymavlink**

- Shifted to using **Pixhawk** for robust control and telemetry.
- Used `pymavlink` for MAVLink protocol integration with ROS2.
- MAVLink message generation and parsing based on [ArduSub Developer Guide](https://www.ardusub.com/developers/pymavlink.html).
- Control signals sent from ROS2 directly to Pixhawk for motor operation and sensor feedback.

---

## ⚙️ Hardware Overview

### ✅ Cytron MDDS60 Motor Driver
- Dual-channel 60A brushed motor driver.
- Supports Serial, PWM, RC, and analog modes.
- Features current sensing, thermal protection, soft start, and easy interfacing.
- We used Serial Mode for integration with Pixhawk/companion computer.

> 💡 **Alternative**: Brushed ESCs commonly available in Bangladesh can be used for similar setups with minor software tweaks.

### ✅ Pixhawk
- Used for telemetry, sensor integration, and robust failsafe control.
- Interfaced with ROS2 via `pymavlink` and USB/Telem ports.

### ✅ Companion Computer
- Runs ROS2 Humble and all control scripts.
- Interfaces with Pixhawk and the motor driver.

---

## 🧑‍💻 Developer Notes

> MAVLink was initially challenging, but I received valuable documentation from the BRACU **Duburi Team**, which accelerated integration with Pixhawk.

---

## 📷 Media & Demonstrations

(Coming Soon: Images, Wiring Diagrams, and Demo Videos)

---

## 📚 References

- [ArduSub pymavlink documentation](https://www.ardusub.com/developers/pymavlink.html)
- [Cytron MDDS60 Documentation](https://docs.cytron.io/cytron-technologies-sdn-bhd/mdds60)
- [ROS2 Documentation](https://docs.ros.org/en/humble/index.html)

---

## 🏁 Future Work

- Add launch files for automated control.
- Integrate high-level navigation stack.
- Improve state estimation using EKF and encoder + IMU fusion.

---

## 🙌 Contributions

Built and tested as part of our work on the **University Rover Challenge (URC)** under **BRACU Mongol Tori**.  
Maintainer: [@mdJesan-08](https://github.com/mdJesan-08)

---


