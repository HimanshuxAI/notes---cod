# UNIT IV — END NODES & GATEWAYS FOR IOT

**Course:** 23CSE3013 – Internet of Things  
**Class:** T.Y. B.Tech CSE (AIEC), SEM-I  
**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Professor:** Prof. Ujjwala N. Salunkhe  
**Academic Year:** 2025-2026 SEM-I  

---

# TABLE OF CONTENTS

1. [ESP32 & ESP8266 NodeMCU](#1-esp32--esp8266-nodemcu)
   - [ESP32 Overview](#esp32-overview)
   - [ESP8266 Overview](#esp8266-overview)
   - [Comparison: ESP32 vs ESP8266](#comparison-esp32-vs-esp8266)
   - [Pinouts & Features](#pinouts--features)
   - [Modes of Operation](#modes-of-operation)
2. [Raspberry Pi](#2-raspberry-pi)
   - [Introduction](#introduction-to-raspberry-pi)
   - [GPIO Pins](#gpio-pins)
   - [Python Programming for GPIO](#python-programming-for-gpio)
   - [WiringPi Library](#wiringpi-library)
3. [Communication Channels on Raspberry Pi](#3-communication-channels-on-raspberry-pi)
   - [Serial Peripheral Interface (SPI)](#serial-peripheral-interface-spi)
   - [Inter-Integrated Circuit (I2C)](#inter-integrated-circuit-i2c)
   - [UART (Serial Communication)](#uart-serial-communication)
4. [Sensors & Actuators](#5-sensors--actuators)
5. [Quick Revision Cheat Sheet](#6-quick-revision-cheat-sheet)
6. [Exam Questions — Model Answers](#7-exam-questions--model-answers)

---

# 1. ESP32 & ESP8266 NODEMCU

## 1.1 ESP32 Overview

**ESP32** is a low-cost, low-power system on a chip (SoC) series created by Espressif Systems.

### Key Features:
- **Dual-core or single-core Tensilica Xtensa LX6 microprocessor** with clock rate up to **240 MHz**
- **Wi-Fi & dual-mode Bluetooth** capabilities
- **Host chip with integrated antenna switches, RF balun, power amplifier, low-noise receive amplifier, filters, and power management modules**
- **Touch-sensitive pins, built-in hall effect sensor, and temperature sensor**
- Designed for mobile devices, wearable electronics, and IoT applications
- **ESP32-WROOM-32** is a popular chip used for IoT applications
- Main part of this module is ESP32-D0WDQ6 chip
- Consists of on-chip WiFi module, Bluetooth low energy module, and Bluetooth module

### ESP32 Specifications:
| Feature | Specification |
|---------|---------------|
| Processor | Tensilica Xtensa LX6 (dual-core or single-core) |
| Clock Speed | Up to 240 MHz |
| RAM | 520 KB SRAM |
| Flash | 4 MB (typically) |
| Wi-Fi | 802.11 b/g/n |
| Bluetooth | Classic + BLE (dual-mode) |
| ADC | 12-bit, up to 18 channels |
| DAC | Yes (2 channels) |
| GPIO Pins | 30-36 |
| I2C Interfaces | 2 hardware interfaces |
| I2S Interfaces | 2 fully featured |
| CAN Interface | Available (some variants) |
| Touch Sensors | Up to 10 |
| Development Frameworks | ESP-IDF, Arduino, MicroPython |
| RTOS Support | Built-in FreeRTOS |
| Price Range | $4–$6 |

### ESP32 Modes of Operation:

| Mode | Description | Current Consumption |
|------|-------------|---------------------|
| **Active Mode** | All parts of Wi-Fi and Bluetooth transmitter and receiver are active | 80–260 mA |
| **Modem Sleep** | Processor is active but Wi-Fi and Bluetooth are disabled | 3–20 mA |
| **Light Sleep** | CPU stops working but RTC unit and ULP processor are still active | ~0.8 mA |
| **Deep Sleep** | Only RTC unit is active | 10–150 µA |
| **Hibernate** | Only RTC timer is active; RTC memory and some I/O pins connected to RTC can wake the chip | ~2.5 µA |

### ESP32 Advantages:
- Successor to ESP8266, easy on the pocket
- Ultra-low power consumption (fine resolution clock gating, multiple power modes, dynamic power scaling)
- More GPIOs than ESP8266
- Built-in dual-core processor
- Rich peripheral set

### ESP32 Disadvantages:
- Priced between $6 to $12 (slightly more than ESP8266 which costs $4 to $6)

### Applications:
- Smart home projects
- Sensor-based projects
- All-in-one ESP32 weather station shield
- Barometric sensor
- Data logging projects (e.g., recording temperature to MicroSD card)
- Web-based projects (setting up ESP32 Access Point for web server)

---

## 1.2 ESP8266 Overview

**ESP8266** is a low-cost Wi-Fi microchip with full TCP/IP stack and microcontroller capability, produced by Espressif Systems.

### Key Features:
- **Tensilica Xtensa 32-bit LX106 RISC microprocessor** operating at 80 to 160 MHz adjustable clock frequency
- Supports RTOS
- **128 KB RAM** and **4 MB Flash memory** (for program and data storage)
- Integrates **802.11 b/g/n HT40 Wi-Fi transceiver**
- Can connect to a WiFi network and interact with the Internet
- Can also set up a network of its own, allowing other devices to connect directly to it
- Low cost, reliability, and easy availability in the market

### ESP8266 Specifications:
| Feature | Specification |
|---------|---------------|
| Processor | Tensilica Xtensa LX106 (single-core) |
| Clock Speed | 80/160 MHz |
| RAM | 160 KB SRAM |
| Flash | 4 MB |
| Wi-Fi | 802.11 b/g/n HT40 |
| Bluetooth | Not available |
| ADC | 10-bit, 1 channel |
| DAC | Not available |
| Bluetooth | Not available |
| Touch Sensors | Not available |
| PWM Outputs | Limited GPIOs |
| I2C Interfaces | 1 (software-based) |
| I2S Interfaces | 1 (limited) |
| CAN Interface | Not available |
| GPIO Pins | 17 |
| Development Frameworks | Arduino, NodeMCU (Lua), MicroPython |
| RTOS Support | Limited (external only) |
| Price Range | $2–$4 |

### ESP8266 NodeMCU Pinouts:

**Power Pins:**
- Two 5V and 3.3V power supply pins
- 3 GND pins for ground
- 3.3V pin can be used to supply power to external components
- Power supplied via on-board MicroB USB connector or VIN pin (regulated 5V source)
- LDO voltage regulator keeps voltage steady at 3.3V, can supply up to 600mA

**ADC:**
- 16 ADC pins to convert analog voltages to digital
- Some connected to internal amplifier, measure small voltages with high precision

**DAC:**
- Not available on ESP8266

**Touchpads:**
- Not available on ESP8266

**SPI:**
- Two SPI interfaces to connect display, SD/microSD memory card module, external flash memory

**I2C:**
- Two I2C interfaces for I2C communication

**UART:**
- Two UART serial interfaces
- Can transfer information up to 5Mbps between two devices
- UART0 has CTS and RTS bases

**GPIO:**
- 32 GPIO pins to communicate with LEDs, switches, and other I/O devices
- Can pull-up or pull-down internally
- GPIO6 to GPIO11 (SCK/CLK, SDO/SD0, SDI/SD1, SHD/SD2, SWP/SD3, SCS/CMD) are used for SPI communication of internal flash memory — **not recommended for use**

**PWM:**
- Almost all GPIO pins can be used for PWM
- Can control motors, LEDs, light, color, etc.

**Enable Pin (EN):**
- Used to enable and disable the module
- HIGH to enable, LOW to disable

**Input/Output Pins (GPIO):**
- 32 GPIO pins
- Can communicate with LEDs, switches, and other I/O devices

**On-board Switches & LED Indicator:**
- Two buttons: RST (Reset) and FLASH (download button for firmware upgrade)
- One LED indicator (user programmable, connected to D0 pin)

**Serial Communication:**
- Includes CP2102 USB-to-UART Bridge Controller from Silicon Labs
- Converts USB signal to serial and allows computer to program and communicate with ESP8266 chip

### ESP8266 Advantages:
- Low cost, reliability, easily available
- Integrates Wi-Fi transceiver
- Can create its own network (Access Point mode)

### ESP8266 Disadvantages:
- Until recently, most documentation was in Mandarin (community has helped translate)
- Limited GPIO pins compared to ESP32
- No Bluetooth
- No DAC
- Limited ADC (1 channel)

### Applications:
- Tracking geolocation
- Building a wireless web server
- Pressure sensors on railway tracks to detect animal deaths
- Smart plugs, humidity and temperature monitoring
- Personal assistant (like SIRI, Google Assistant, Alexa)

---

## 1.3 Comparison: ESP32 vs ESP8266

| Feature | ESP32 | ESP8266 |
|---------|-------|---------|
| **CPU** | Dual-core Xtensa LX6 @ 160/240 MHz | Single-core Xtensa LX106 @ 80/160 MHz |
| **RAM** | 520 KB SRAM | 160 KB SRAM |
| **ADC Channels** | 12-bit, up to 18 channels | 10-bit, 1 channel |
| **DAC Support** | Yes (2 channels) | Not available |
| **Bluetooth** | Yes (Classic + BLE) | Not available |
| **Touch Sensors** | Yes (up to 10) | Not available |
| **PWM** | Available on all GPIOs | Limited GPIOs |
| **I2C Interfaces** | 2 hardware interfaces | 1 (software-based) |
| **I2S Interfaces** | 2 fully featured | 1 (limited) |
| **CAN Interface** | Available (some variants) | Not available |
| **GPIO Pins** | 30–36 | 17 |
| **Development Framework** | ESP-IDF, Arduino, MicroPython | Arduino, NodeMCU (Lua), MicroPython |
| **RTOS Support** | Built-in FreeRTOS | Limited (external only) |
| **Power Consumption** | Higher, more modes | Lower, fewer modes |
| **Typical Price** | $4–$6 | $2–$4 |

**When to Choose ESP32:** When you need Bluetooth, more GPIOs, ADC channels, DAC, dual-core processing, or built-in RTOS.

**When to Choose ESP8266:** For simple Wi-Fi enabled projects where cost is the primary concern and advanced features are not needed.

---

## 1.4 NodeMCU Modes of Operation

ESP devices (ESP8266 or ESP32) can operate in different modes depending on their role in a network:

### Station (STA) Mode / Wi-Fi Station:
- The ESP device connects to an existing Wi-Fi network as a client
- Behaves like smartphones or laptops — joins an established network and communicates with other devices
- Can access the internet or interact with other devices on the same network

### Access Point (AP) Mode / Wi-Fi Access Point:
- The ESP device functions as a Wi-Fi access point, creating its own network
- Other devices (smartphones, computers) can connect to this network and communicate directly with the ESP device
- Useful when you want the ESP device to act as a central hub

### STA + AP Mode:
- Combines both modes — ESP device connects to an existing network as a client while simultaneously hosting its own network for other devices to connect to
- Allows the ESP device to act as an intermediary between different networks or facilitate direct communication between devices

### Code Example — Station Mode:
```cpp
#include <ESP8266WiFi.h>  // Include the Wi-Fi library
const char *ssid     = "SSID";    // The SSID of the Wi-Fi network
const char *password = "PASSWORD"; // The password of the Wi-Fi network

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println('\n');
  WiFi.begin(ssid, password);  // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid);
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) {  // Wait for Wi-Fi to connect
    delay(1000);
    Serial.print(++i);
    Serial.print(' ');
  }
  Serial.println('\n');
  Serial.println("Connection established!");
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());  // Send the IP address of ESP8266 to computer
}

void loop() {}
```

### Code Example — Access Point Mode:
```cpp
#include <ESP8266WiFi.h>
const char *ssid = "Voyager31";    // The name of the Wi-Fi network that will be created
const char *password = "DivideByZero"; // The password required to connect (leave blank for open network)

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println('\n');
  WiFi.softAP(ssid, password);  // Start the access point
  Serial.print("Access Point \"");
  Serial.print(ssid);
  Serial.println("\" started");
  Serial.print("IP address:\t");
  Serial.println(WiFi.softAPIP());  // Send the IP address of ESP8266 to computer
}

void loop() {}
```

### Code Example — AP + STA Mode:
```cpp
#include <ESP8266WiFi.h>
#define WIFI_SSID "YOUR WIFI NETWORK SSID"    // Set WiFi credentials
#define WIFI_PASS "YOUR WIFI PASSWORD"
#define AP_SSID "ESP8266"                     // Set AP credentials
#define AP_PASS "magicword"

void setup() {
  Serial.begin(115200);
  Serial.println();
  WiFi.mode(WIFI_AP_STA);  // Begin Access Point
  WiFi.softAP(AP_SSID, AP_PASS);
  WiFi.begin(WIFI_SSID, WIFI_PASS);  // Begin WiFi
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("Connected!");
  Serial.print("IP address for network ");
  Serial.print(WIFI_SSID);
  Serial.print(" : ");
  Serial.println(WiFi.localIP());
  Serial.print("IP address for network ");
  Serial.print(AP_SSID);
  Serial.print(" : ");
  Serial.println(WiFi.softAPIP());
}

void loop() {}
```

---

# 2. RASPBERRY PI

## 2.1 Introduction to Raspberry Pi

**Raspberry Pi** is the most popular SBC (Small Board Computer) around the world. It can do pretty much everything that a desktop computer can do and is suitable for all ages who are keen to explore computing.

### Key Features:
- Comes with all the software required for basic computing
- Can extend functionalities by installing an OS
- OS is the most crucial program that helps develop and execute programs
- Enables hardware to communicate with software for generating meaningful interactions
- Manages CPU, memory, disk drives, printers, establishes user interface, and provides services for application software
- **Raspbian** is the official Raspberry Pi OS, but other alternative operating systems are available

### Raspberry Pi vs Arduino (earlier IoT platform):
- Earlier IoT platforms were programmable through Arduino IDE
- Raspberry Pi 3 supports an operating system, through which it can be programmed
- Raspberry Pi is a full-fledged computer, not just a microcontroller

---

## 2.2 GPIO Pins (General Purpose Input/Output)

GPIO pins can be used as input or output and allow Raspberry Pi to connect with general purpose I/O devices.

### GPIO Header:
- The Raspberry Pi offers its GPIO over a standard male header on the board
- Raspberry Pi 3 Model B board contains a single 40-pin expansion header labeled as 'J8' providing access to **28 GPIO pins**
- (Pins 1, 2, 39 & 40 are also labeled below)

### Pin Numbering Methods:

**1. GPIO Numbering:**
- Pin number refers to the number on Broadcom SoC (System on Chip)
- In RPi.GPIO, GPIO numbering is identified by **BCM**

**2. Physical Numbering:**
- Pin number refers to the pin of the 40-pin P1 header on Raspberry Pi Board
- Simple — count pin number on P1 header and assign it as GPIO
- In RPi.GPIO, Physical numbering is identified by **BOARD**

### Example:
```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)      # Use BCM numbering (GPIO.BCM)
GPIO.setmode(GPIO.BOARD)    # Use Physical numbering (GPIO.BOARD)

# Example: Using pin 40 of P1 header as GPIO output
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.OUT)    # BCM pin 21 = Physical pin 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)    # Physical pin 40
```

### Pin Capabilities:
- **PWM (Pulse-Width Modulation):** Software PWM available on all pins; Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19
- **SPI (Serial Peripheral Interface):**
  - SPI0: MOSI (GPIO10), MISO (GPIO9), SCLK (GPIO11), CE0 (GPIO8), CE1 (GPIO7)
  - SPI1: MOSI (GPIO20), MISO (GPIO19), SCLK (GPIO21), CE0 (GPIO18), CE1 (GPIO17), CE2 (GPIO16)
- **I2C (Inter-Integrated Circuit):**
  - Data: GPIO2; Clock: GPIO3
  - EEPROM Data: GPIO0; EEPROM Clock: GPIO1
- **Serial:**
  - TX: GPIO14; RX: GPIO15

---

## 2.3 Python Programming for GPIO

To use GPIO pins in Python, import the RPi.GPIO package:

```python
import RPi.GPIO as GPIO

# Set pin numbering system
GPIO.setmode(GPIO.BCM)      # BCM numbering
# OR
GPIO.setmode(GPIO.BOARD)    # Physical numbering

# Setup GPIO pin as output
GPIO.setup(channel, GPIO.OUT)

# Setup GPIO pin as input
GPIO.setup(channel, GPIO.IN)

# Setup with pull-up/down resistor
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set output state
GPIO.output(channel, GPIO.HIGH)
GPIO.output(channel, GPIO.LOW)

# Read input state
value = GPIO.input(channel)

# Disable warnings
GPIO.setwarnings(False)
```

### Example: Control LED using Switch (Python)

```python
import RPi.GPIO as GPIO

LED = 32        # pin no. as per BOARD, GPIO18 as per BCM
Switch_input = 29  # pin no. as per BOARD, GPIO27 as per BCM

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # set pin numbering format
GPIO.setup(LED, GPIO.OUT)  # set GPIO as output
GPIO.setup(Switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if (GPIO.input(Switch_input)):
        GPIO.output(LED, GPIO.LOW)
    else:
        GPIO.output(LED, GPIO.HIGH)
```

### GPIO Functions:

| Function | Description |
|----------|-------------|
| `GPIO.setmode(GPIO.BCM)` / `GPIO.setmode(GPIO.BOARD)` | Define pin numbering system |
| `GPIO.setup(channel, GPIO.OUT)` | Set GPIO pin as output |
| `GPIO.setup(channel, GPIO.IN)` | Set GPIO pin as input |
| `GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)` | Enable pull-up resistor |
| `GPIO.output(channel, GPIO.HIGH)` | Set output state HIGH |
| `GPIO.output(channel, GPIO.LOW)` | Set output state LOW |
| `GPIO.input(channel)` | Read value of GPIO pin |

---

## 2.4 WiringPi Library

**WiringPi** is a C library that provides easy access to the Raspberry Pi GPIO system. It's designed to provide similar functionality to the Wiring package (core of the Arduino input/output system).

### Features:
- Supports UART port, SPI, I2C, and PWM
- Provides Arduino-like functions (pinMode, digitalWrite, digitalRead)

### Example: Blinking LED using C (WiringPi)

```c
#include <WiringPi.h>
#include <stdio.h>

int LED = 26;        // GPIO26 as per wiringPi, GPIO12 as per BCM, pin no .32 *
int switch_input = 21; // GPIO21 as per Wiring Pi, GPIO5 as per BCM, pin no .29 *

int main() {
  wiringPiSetup();   // Initialize wiringPi setup
  pinMode(LED, OUTPUT);    // set GPIO as output
  pullUpDnControl(switch_input, PUD_UP);
  
  while (1) {
    if (digitalRead(switch_input))
      digitalWrite(LED, LOW);   // write LOW on GPIO
    else
      digitalWrite(LED, HIGH);  // write HIGH on GPIO
  }
}
```

### Example: Blinking LED using Python (WiringPi)

```python
import wiringpi
import time

ledPin = 6
wiringpi.wiringPiSetup()
wiringpi.pinMode(ledPin, 1)

while True:
    wiringpi.digitalWrite(ledPin, 1)
    time.sleep(1)
    wiringpi.digitalWrite(ledPin, 0)
    time.sleep(1)
```

---

# 3. COMMUNICATION CHANNELS ON RASPBERRY PI

Raspberry Pi supports communication with the external world through:
- **GPIO channels** (All digital)
- **SPI (Serial Peripheral Interface)**
- **I2C (Inter-Integrated Circuit)**
- **UART (Universal Asynchronous Receiver/Transmitter)**

## 3.1 SPI (Serial Peripheral Interface)

SPI is a synchronous serial interface for short distances. Developed by Motorola in 1979, sends 1 bit at a time via one channel.

### Key Characteristics:
- **Synchronous:** Data sent in blocks or frames, devices synchronized using a clock
- **Serial interface:** Devices send one bit at a time (unlike parallel communication)
- **Master-Slave:** One device is the "Master" (dictates clock cycle), the other is the "Slave"
- **Full-duplex:** Both devices can send data to each other at the same time via MOSI and MISO lines
- Raspberry Pi 4 has 7 SPI busses

### SPI Data Transmission:
1. Master sends a clock signal and selects a slave through the CS/SS (Chip Select/Slave Select) line
2. Master sends logic 0 to select a slave (this line is active low)
3. If a waiting period is required, master waits before sending clock signal
4. SPI is full-duplex — both master and slave can send data at the same time via MOSI and MISO lines respectively, synchronized by the serial clock
5. Provides flexibility to select rising or falling edge of the clock to sample or shift the data

### SPI Modes:
There are four different data transmission modes, differing in clock polarity and clock phase:
- **Clock Polarity (CPOL):** 0 = LOW idle state, 1 = HIGH idle state
- **Clock Phase (CPHA):** 0 = data sent on falling edge, 1 = data sent on rising edge

### SPI Advantages:
- Full duplex
- High speed
- Good signal integrity
- Simple hardware interfacing

### SPI Disadvantages:
- Requires more pins than I2C
- No formal standard
- Typically only one master
- No hardware slave acknowledgment

### Installing SPI on Raspberry Pi:
```bash
sudo apt-get install python3-spidev
sudo apt-get install python3-spidev python-spidev
```
Turn on SPI mode using configuration manager from desktop or use: `sudo raspi-config`

---

## 3.2 I2C (Inter-Integrated Circuit)

I2C is a serial bus interface connection protocol, also called **TWI (Two Wire Interface)** since it uses only two wires for communication.

### Key Characteristics:
- **Two wires:** SDA (Serial Data) and SCL (Serial Clock)
- **SDA:** Used for data exchange between master and slave device
- **SCL:** Clock signal; data is sent on clock tick event; only master device has control over this line
- **Open drain configuration:** Lines can pull the corresponding signal line low but cannot drive it high; hence lines go to unknown state; pull-up resistors need to be connected on SCL and SDA pins
- **Acknowledgment-based:** Transmitter checks for acknowledgment from receiver after transmitting data
- **Two modes:** Master mode and Slave mode
- **Addressing:** I2C device has 7-bit or 10-bit unique address; master must address devices by their unique address; slave device responds when addressed by master

### Applications:
- Reading RTC (Real-time clock)
- Accessing external EEPROM memory
- Sensor modules (gyro, accelerometer, etc.)

---

## 3.3 UART (Serial Communication)

UART (Universal Asynchronous Receiver/Transmitter) is used for serial communication.

### Raspberry Pi UART:
- Two UART serial interfaces on the ESP32 module (also applicable to Raspberry Pi context)
- Can transfer information up to 5Mbps between two devices
- UART0 has CTS and RTS bases

---

# 4. SENSORS & ACTUATORS

## 4.1 Sensors Mentioned:
- **Ultrasonic Sensor:** Distance measurement
- **PWM Servo motor:** Position control

## 4.2 PWM (Pulse-Width Modulation)

PWM can be used to control motors, LEDs, light, color, etc. Almost all ESP32 GPIO pins can be used for PWM. On Raspberry Pi, software PWM is available on all pins, hardware PWM on GPIO12, GPIO13, GPIO18, GPIO19.

---

# 5. QUICK REVISION CHEAT SHEET

| Topic | Key Point |
|-------|-----------|
| **ESP32** | Dual-core Xtensa LX6, Wi-Fi + Bluetooth, 520KB RAM, up to 240MHz, $4-6 |
| **ESP8266** | Single-core LX106, Wi-Fi only, 160KB RAM, 80/160MHz, $2-4 |
| **ESP32 Modes** | STA (station), AP (access point), STA+AP (both) |
| **Raspberry Pi** | SBC, runs OS (Raspbian), 40-pin GPIO header, 28 GPIO pins |
| **GPIO Numbering** | BCM (Broadcom SoC) vs BOARD (physical pin on P1 header) |
| **SPI** | Synchronous, master-slave, full-duplex, 3-4 wires (MOSI, MISO, SCLK, CS/SS) |
| **I2C** | Two-wire (SDA, SCL), open drain, needs pull-up resistors, 7-bit/10-bit addressing |
| **UART** | Asynchronous serial, up to 5Mbps, TX/RX pins |
| **Python GPIO** | RPi.GPIO library, GPIO.setmode(), GPIO.setup(), GPIO.output(), GPIO.input() |
| **WiringPi** | C library for GPIO, Arduino-like functions (pinMode, digitalWrite, digitalRead) |

---

# 6. EXAM QUESTIONS — MODEL ANSWERS

**Q1. Explain the features of ESP32 microcontroller.**

**Answer:**
ESP32 is a low-cost, low-power system on a chip (SoC) series from Espressif Systems. Key features:
- Dual-core or single-core Tensilica Xtensa LX6 microprocessor @ up to 240 MHz
- Wi-Fi & dual-mode Bluetooth (Classic + BLE)
- 520 KB SRAM, integrated antenna, RF balun, power amplifier
- Touch-sensitive pins, hall effect sensor, temperature sensor
- 12-bit ADC (up to 18 channels), 2 DAC channels
- 30-36 GPIO pins, 2 I2C, 2 I2S, CAN (some variants)
- Built-in FreeRTOS, supports ESP-IDF, Arduino, MicroPython
- Ultra-low power with multiple sleep modes (down to ~2.5 µA in deep sleep)

---

**Q2. Compare ESP32 and ESP8266.**

**Answer:**

| Feature | ESP32 | ESP8266 |
|---------|-------|---------|
| CPU | Dual-core LX6 @ 240 MHz | Single-core LX106 @ 160 MHz |
| RAM | 520 KB | 160 KB |
| Wi-Fi | Yes | Yes |
| Bluetooth | Yes (Classic + BLE) | No |
| ADC | 12-bit, 18 channels | 10-bit, 1 channel |
| GPIO | 30-36 | 17 |
| Price | $4-6 | $2-4 |

---

**Q3. Explain the different modes of operation of ESP32/ESP8266.**

**Answer:**
- **Station (STA) Mode:** ESP connects to existing Wi-Fi network as a client
- **Access Point (AP) Mode:** ESP creates its own Wi-Fi network, other devices connect to it
- **STA+AP Mode:** ESP connects to existing network while simultaneously hosting its own network

---

**Q4. Explain Raspberry Pi GPIO pins and their numbering systems.**

**Answer:**
Raspberry Pi 3 Model B has a 40-pin expansion header (J8) with 28 GPIO pins. Two numbering systems:
- **GPIO Numbering:** Based on Broadcom SoC pin numbers (BCM)
- **Physical Numbering:** Based on physical pin position on P1 header (BOARD)

**GPIO Capabilities:** PWM, SPI, I2C, UART, digital input/output

---

**Q5. Explain SPI communication protocol on Raspberry Pi.**

**Answer:**
SPI (Serial Peripheral Interface) is a synchronous serial interface developed by Motorola in 1979:
- Master-slave architecture, full-duplex communication
- Uses MOSI, MISO, SCLK, and CS/SS lines
- Four modes based on clock polarity (CPOL) and clock phase (CPHA)
- Raspberry Pi 4 has 7 SPI buses
- Requires `python3-spidev` library and enabling via `raspi-config`

---

**Q6. Explain I2C communication protocol.**

**Answer:**
I2C (Inter-Integrated Circuit), also called TWI (Two Wire Interface):
- Uses only two wires: SDA (Serial Data) and SCL (Serial Clock)
- Master-slave architecture with acknowledgment-based communication
- Open drain configuration — requires pull-up resistors on SCL and SDA lines
- 7-bit or 10-bit unique device addressing
- Used for RTC, EEPROM, sensor modules (gyro, accelerometer)

---

**Q7. Write Python code to control an LED using a switch on Raspberry Pi GPIO.**

**Answer:**
```python
import RPi.GPIO as GPIO

LED = 32         # pin no. as per BOARD, GPIO18 as per BCM
Switch_input = 29 # pin no. as per BOARD, GPIO27 as per BCM

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # set pin numbering format
GPIO.setup(LED, GPIO.OUT)  # set GPIO as output
GPIO.setup(Switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(Switch_input):
        GPIO.output(LED, GPIO.LOW)
    else:
        GPIO.output(LED, GPIO.HIGH)
```

---

**Good luck with your Unit 4 IoT exam!** Focus on understanding ESP32/ESP8266 features, GPIO programming, and communication protocols (SPI, I2C, UART) — these are high-yield topics.