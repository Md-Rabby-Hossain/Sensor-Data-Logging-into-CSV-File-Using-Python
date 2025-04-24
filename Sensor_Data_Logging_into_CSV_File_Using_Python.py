import serial
import csv
from datetime import datetime

ser = serial.Serial('COM4', 115200, timeout=1)

with open('MSA_data1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Time', 'Temperature (°C)', 'Humidity (%)'])

    print("Collecting data... Press Ctrl+C to stop.")
    try:
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                try:
                    temp, hum = line.split(',')
                    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow([now, temp, hum])
                    print(f"{now} -> Temp: {temp}°C, Humidity: {hum}%")
                except ValueError:
                    print("Skipping malformed line:", line)
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        ser.close()
