# Sensor Data Logging into CSV File Using Python

## 📖 Description
A simple project to log temperature and humidity data from a **DHT11 sensor** connected to an **ESP32**. Data is sent via **serial communication** and recorded in a **CSV file** using **Python**, with timestamps for each reading. This setup is useful for IoT data logging, environmental monitoring, and basic sensor data analysis.

---

## 📦 Features
- Real-time temperature and humidity data acquisition from DHT11
- Serial communication between ESP32 and PC
- Python-based data logger with automatic timestamping
- Saves data into a CSV file for further analysis

---

## 🛠️ Requirements

### Hardware:
- ESP32 Development Board
- DHT11 Temperature & Humidity Sensor
- USB Cable

### Software:
- Arduino IDE
- Python 3.x
- Python `pyserial` library

Install `pyserial`: pip install pyserial

---

## 📝 How It Works

1. The ESP32 reads data from the DHT11 sensor.
2. The data is sent via serial communication to the computer.
3. A Python script reads the serial data.
4. Each reading is saved to a CSV file with a timestamp.

---

## 📊 Example Data Format (CSV)

| Timestamp           | Temperature (°C) | Humidity (%) |
|:------------------|:----------------|:------------|
| 2025-04-21 14:30:22 | 33.00           | 85.00       |
| 2025-04-21 14:30:24 | 34.00           | 86.00       |

---

## 📃 License
This project is open-source and available for educational and personal use.


