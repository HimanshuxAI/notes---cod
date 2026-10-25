# EXPERIMENT No: 5 — Programming RPi using Python & WiringPi Library

**Course:** 23CSE3013 – Internet of Things (End Nodes & Gateways)  
**Experiment:** GPIO, I2C Sensor Reading (BMP280/MPU6050), UART between RPi & ESP32  
**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Professor:** Prof. Ujjwala N. Salunkhe  

---

## 📋 Aim of the Experiment

To program a Raspberry Pi using Python to:

1. Blink an LED using GPIO.
2. Read a digital sensor using GPIO.
3. Read an I2C sensor (BMP280 / MPU6050) using I2C.
4. Establish UART communication between Raspberry Pi and ESP32.

---

## ✅ Write-Up Question 1 — Explain the Procedure for Blinking an LED Using Raspberry Pi and Python

### Procedure

1. **Components Required:**
   - Raspberry Pi (3/4/5) with MicroSD card (16 GB+) and Raspberry Pi OS
   - LED (Red/Green)
   - 220 Ω or 330 Ω resistor
   - Breadboard and jumper wires

2. **Circuit Connection:**
   - GPIO17 (Physical Pin 11) → resistor → LED anode → LED cathode → GND (Physical Pin 6)

   ```
   Raspberry Pi
      GPIO17 (Pin 11)
          |
        Resistor
          |
         LED
          |
       GND (Pin 6)
   ```

3. **Software Setup:**
   - Open terminal / SSH into Raspberry Pi
   - Create Python file: `nano led_blink.py`

4. **Python Program:**

   ```python
   import RPi.GPIO as GPIO
   import time

   LED_PIN = 17

   GPIO.setmode(GPIO.BCM)
   GPIO.setup(LED_PIN, GPIO.OUT)

   try:
       while True:
           GPIO.output(LED_PIN, GPIO.HIGH)
           print("LED ON")
           time.sleep(1)

           GPIO.output(LED_PIN, GPIO.LOW)
           print("LED OFF")
           time.sleep(1)

   except KeyboardInterrupt:
       print("Program stopped")

   finally:
       GPIO.cleanup()
   ```

5. **Run the Program:**

   ```
   python3 led_blink.py
   ```

6. **Expected Output:**

   ```
   LED ON
   LED OFF
   LED ON
   LED OFF
   ```

   LED blinks ON/OFF at one-second intervals.

7. **Stop:** Press `Ctrl + C` → GPIO cleanup runs automatically.

### Conclusion

The GPIO pin was configured as output and used to switch the LED ON and OFF, demonstrating basic Raspberry Pi GPIO programming with Python.

---

## ✅ Write-Up Question 2 — Describe the Procedure for Interfacing a BMP280 Sensor with Raspberry Pi

### Procedure

1. **Connections:**

   ```
   Raspberry Pi        BMP280
   -----------------    ----------------
   3.3V                 VCC
   GND                 GND
   GPIO2 / Pin 3       SDA
   GPIO3 / Pin 5       SCL
   ```

2. **Enable I2C on Raspberry Pi:**

   ```
   sudo raspi-config
   → Interface Options
       → I2C
           → Enable
   sudo reboot
   ```

3. **Install and Scan I2C Bus:**

   ```
   sudo apt install i2c-tools
   i2cdetect -y 1
   ```

   - Expected address for BMP280: `76` or `77` (depending on configuration)

4. **Install BMP280 Library:**

   ```
   pip3 install adafruit-circuitpython-bmp280
   ```

5. **Python Program:**

   ```python
   import time
   import board
   import busio
   import adafruit_bmp280

   i2c = busio.I2C(board.SCL, board.SDA)
   bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

   while True:
       print("Temperature: {:.2f} °C".format(bmp280.temperature))
       print("Pressure: {:.2f} hPa".format(bmp280.pressure))
       print("--------------------------")
       time.sleep(2)
   ```

6. **Expected Output:**

   ```
   Temperature: 28.50 °C
   Pressure: 1008.45 hPa
   --------------------------
   Temperature: 28.60 °C
   Pressure: 1008.38 hPa
   --------------------------
   ```

### Conclusion

The BMP280 temperature and pressure sensor was successfully interfaced over I2C and data was read using Python.

---

## ✅ Write-Up Question 3 — Explain How UART Communication Can Be Established Between Raspberry Pi and ESP32

### Procedure

1. **Connection (Cross-connect):**

   ```
   Raspberry Pi         ESP32
   -----------------     ----------------
   GPIO14 TX (Pin 8)   → ESP32 RX
   GPIO15 RX (Pin 10)  → ESP32 TX
   GND                  → GND
   ```

2. **Important:** RPi TX → ESP32 RX; RPi RX → ESP32 TX; GND → GND. Both operate on 3.3 V logic, compatible for UART.

3. **Enable UART on Raspberry Pi:**

   ```
   sudo raspi-config
   → Interface Options
       → Serial Port
           → "Would you like a login shell to be accessible over serial?"
               → No
           → Enable the serial hardware
   sudo reboot
   ```

4. **Raspberry Pi Python Receiver (PySerial):**

   ```python
   import serial
   import time

   ser = serial.Serial(
       '/dev/serial0',
       9600,
       timeout=1
   )

   time.sleep(2)

   print("Waiting for data from ESP32...")

   try:
       while True:
           if ser.in_waiting > 0:
               data = ser.readline().decode('utf-8').strip()
               print("Received from ESP32:", data)

   except KeyboardInterrupt:
       print("UART communication stopped.")

   finally:
       ser.close()
   ```

5. **ESP32 Program (UART Sender):**

   ```cpp
   void setup() {
     Serial.begin(9600);
   }

   void loop() {
     Serial.println("Hello from ESP32");
     delay(2000);
   }
   ```

6. **Expected Output (Raspberry Pi):**

   ```
   Waiting for data from ESP32...
   Received from ESP32: Hello from ESP32
   Received from ESP32: Hello from ESP32
   Received from ESP32: Hello from ESP32
   ```

### Conclusion

UART communication between RPi and ESP32 was established using cross-connected TX/RX pins and PySerial on the RPi side, with serial communication enabled via `raspi-config`.

---

## ✅ Write-Up Question 4 — Compare GPIO, I2C, and UART Communication.

| Feature | GPIO | I2C | UART |
|---------|------|-----|------|
| **Full Form** | General Purpose Input/Output | Inter-Integrated Circuit | Universal Asynchronous Receiver/Transmitter |
| **Wires / Lines** | Single digital signal (or groups of GPIOs) | 2 wires: SDA + SCL | 2 wires: TX + RX (plus GND) |
| **Type** | Digital I/O (input or output) | Synchronous serial bus (Master/Slave) | Asynchronous serial (point-to-point) |
| **Addressing** | No addressing (GPIO per pin) | 7-bit or 10-bit device address | No addressing (TX→RX direct connection) |
| **Use** | LED control, digital sensors/switches, simple signals | Sensor interfacing (BMP280, MPU6050, EEPROM) | Device-to-device serial (RPi ↔ ESP32) |
| **Speed** | Low / bit-level | Higher than GPIO, slower than SPI | Moderate (up to several Mbps) |
| **Protocol** | Digital HIGH/LOW | Master controls clock (SCL), data via SDA, ACK-based | Asynchronous, start/stop bits, configurable baud rate |

### Key Differences in Simple Words:

- **GPIO** is a raw digital pin — you directly read/write HIGH/LOW signals to sensors or drive LEDs.
- **I2C** is a bus protocol using SDA+SCL with device addressing — used to talk to multiple sensors (BMP280/MPU6050) on the same two wires.
- **UART** is a simple point-to-point serial link — used between two devices (RPi ↔ ESP32) by cross-connecting TX→RX.

---

## ✅ Write-Up Question 5 — How Can Raspberry Pi be Used as an IoT Gateway to Collect Sensor Data from ESP32?

### Concept

The **Raspberry Pi acts as an IoT Gateway** that receives sensor data from the **ESP32 End Node** via **UART**, processes/collects it, and can further forward it to cloud/analytics systems or brokers.

### Working Flow

1. **ESP32 (End Node)** reads sensors:
   - Digital sensor via **GPIO**
   - I2C sensors (BMP280/MPU6050) via **I2C**
2. **ESP32 publishes** the readings over **UART (Serial)** to the Raspberry Pi.
3. **Raspberry Pi (Gateway)** uses **Python + PySerial** to receive the data via **UART** on `/dev/serial0`.
4. **Raspberry Pi** can:
   - Store / log the sensor data (CSV, database)
   - Trigger alerts (GPIO output — e.g., buzzer/LED)
   - Forward data to cloud platforms (MQTT broker, AWS/Azure services)

### Gateway Architecture Summary:

```
[ESP32 + Sensors (GPIO/I2C)] 
        │  UART (TX → RX, RX → TX, GND → GND)
        ▼
[Raspberry Pi (Python + PySerial) ← Gateway]
        │
        ├── GPIO → control actuators / alerts
        ├── Process → collect sensor readings
        └── Forward → cloud / analytics / dashboard
```

### Why RPi as Gateway?

- Full Linux OS → richer processing (Python, ML, dashboards)
- Bluetooth / Wi-Fi capability → can connect to cloud (AWS IoT, Azure IoT Hub, MQTT)
- Multiple protocols available (GPIO, I2C, UART, SPI, Wi-Fi, Bluetooth)
- Acts as bridge between constrained ESP32 nodes and cloud/enterprise systems

---

## 🧠 Quick Comparison — RPi as Gateway vs ESP32 as Node

| Role | Device | Protocols | Strength |
|------|--------|-----------|----------|
| **End Node** | ESP32 | GPIO, I2C, UART, Wi-Fi | Low cost, low power, constrained |
| **Gateway** | Raspberry Pi | GPIO, I2C, UART, SPI, Wi-Fi, Bluetooth | Full Linux processing power |

---

## 📚 Summary

The experiment successfully demonstrated:

- ✅ GPIO programming on Raspberry Pi using Python (`RPi.GPIO`) — LED blink, digital sensor read
- ✅ I2C interfacing with BMP280 / MPU6050 sensors
- ✅ UART communication between Raspberry Pi and ESP32
- ✅ Raspberry Pi as an **IoT Gateway** capable of collecting sensor data from ESP32 end nodes

---

**Good luck with your experiment viva & write-up!**
